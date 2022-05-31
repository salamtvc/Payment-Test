import uuid
from django.db import models

from django.contrib.auth.models import User

STATUS_CHOICES = (
	('pending', 'Pending'),
	('completed', 'Completed'),	
	('failed', 'Failed')
)

class PaymentUpdate(models.Model):

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	price = models.DecimalField(max_digits=20, decimal_places=2)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

	class Meta:
		verbose_name = 'Payment Update'