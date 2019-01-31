from django import forms
from .models import Product 
class CreateProductForm(forms.ModelForm):
	"""Here is the way to create a form"""
	class Meta:
		model = Product
		fields = ['name','description','image','quantity']