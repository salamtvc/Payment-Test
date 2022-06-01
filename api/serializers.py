from rest_framework import serializers

from api.models import PaymentUpdate


class PaymentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentUpdate
        fields = [
            "user", "created_at", "price", "status"
        ]