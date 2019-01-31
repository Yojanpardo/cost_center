from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nit = models.CharField(max_length=20)
	name = models.CharField(max_length=100)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = 'Companies'
		
	def __str__(self):
		return self.name

