from django.db import models

# Create your models here.

class RawMaterial(models.Model):
	UNITS =(
		('m','Metros'),
		('g','Gramos'),
		('l','Litros'),
		('m^2','Metros cuadrados'),
		('m^3','Metros cúbicos'),
	)
	name = models.CharField(max_length=50, unique=True)
	description = models.TextField(max_length=255)
	cost = models.DecimalField(max_digits=12, decimal_places=2)
	image = models.ImageField(upload_to='raw_materials/images',blank=True,null=True)
	unit_of_mesure = models.CharField(max_length=3, choices=UNITS)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} ({})'.format(self.name,self.unit_of_mesure)

class RawMaterialDetail(models.Model):
	"""docstring for RawMateriaDetail"""
	raw_material = models.ForeignKey('raw_materials.RawMaterial', on_delete=models.CASCADE)
	product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
	quantity = models.DecimalField(max_digits=12,decimal_places=3)
	cost = models.DecimalField(max_digits=12,decimal_places=2, blank=True,null=True)
	
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)