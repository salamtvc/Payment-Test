from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from api.models import PaymentUpdate
from api.tasks import retry_with_backoff
from api.utils import get_random_number


class UpdatePaymentView(APIView):
	permission_classes = [IsAuthenticated]

	def post(self, request):
		response = {}
		response["status"] = "success"
		amount = request.POST.get('amount', '')
		if amount:
			obj = PaymentUpdate.objects.create(user=self.request.user, price=amount)
			retry_with_backoff.delay(obj.id)
		else:
			response["status"] = "failed"
			response["message"] = "invalid amount"
		return Response(response, status=status.HTTP_200_OK)

	def get(self, request):
		response = {}
		response["status"] = "success"
		response["object_list"] = PaymentUpdate.objects.all()
		return Response(response, status=status.HTTP_200_OK)


class CheckPaymentSatusView(APIView):
	permission_classes = []

	def post(self, request):
		response = {}
		response["status"] = "success"

		_id = request.POST.get('obj_id', '')
		random_number = get_random_number()
		print("-----Random-Number------>> ", random_number)
		if random_number == 5:
			try:
				obj = PaymentUpdate.objects.get(id=_id)
				obj.status = 'completed'
				obj.save()
				response["object"] = obj
				print("----Status-updated-success---->>>")
			except:
				response["status"] = "failed"
			return Response(response, status=status.HTTP_200_OK)
		return Response(response, status=status.HTTP_502_BAD_GATEWAY)



# HTTP_500_INTERNAL_SERVER_ERROR
# HTTP_501_NOT_IMPLEMENTED
# HTTP_502_BAD_GATEWAY
# HTTP_503_SERVICE_UNAVAILABLE
# HTTP_504_GATEWAY_TIMEOUT
# HTTP_505_HTTP_VERSION_NOT_SUPPORTED
# HTTP_506_VARIANT_ALSO_NEGOTIATES
# HTTP_507_INSUFFICIENT_STORAGE
# HTTP_508_LOOP_DETECTED
# HTTP_509_BANDWIDTH_LIMIT_EXCEEDED
# HTTP_510_NOT_EXTENDED
