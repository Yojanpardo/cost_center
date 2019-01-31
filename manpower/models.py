from django.db import models

# Create your models here.

class Manpower(models.Model):
	name = models.CharField(max_length=50)
	cost_per_hour = models.DecimalField(max_digits=9, decimal_places=3)
	image = models.ImageField(upload_to='manpower/images', blank=True, null=True)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class ManpowerDetail(models.Model):
	manpower = models.ForeignKey(Manpower, on_delete=models.CASCADE)
	product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
	time = models.DecimalField(max_digits=5, decimal_places=3)
	cost = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)