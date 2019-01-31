from django.db import models

# Create your models here.

class Product(models.Model):
	"""docstring for Product"""
	name = models.CharField(max_length=30)
	description = models.TextField(max_length=255,blank=True,null=True)
	image = models.ImageField(blank=True,null=True)
	quantity = models.IntegerField()

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.name