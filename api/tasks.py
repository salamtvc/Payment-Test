import requests
from django.conf import settings
from api.models import PaymentUpdate
import random, time
from payment_test.celery import app

@app.task
def retry_with_backoff(obj_id):
	retries = 10
	backoff_in_seconds = 1
	x = 0
	while x<retries:
		try:
			print("--------->>Try ")
			response = requests.post(settings.CHECK_STATUS_URL, json={"obj_id": obj_id})
			if response.status_code >= 500:
				print("--------->>Raise Error ")
				response.raise_for_status()
			print("----------->> Success")
		except (requests.exceptions.Timeout,requests.exceptions.ConnectionError,requests.exceptions.HTTPError) as e:
			if x == retries:
				raise
			else:
				sleep = (backoff_in_seconds * 2 ** x + random.uniform(0, 1))
				time.sleep(sleep)
				x += 1
				print("-------->> Retry")
