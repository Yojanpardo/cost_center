from django import forms
from .models import RawMaterialDetail, RawMaterial

class CreateRawMaterialDetailForm(forms.ModelForm):
	class Meta:
		model = RawMaterialDetail
		fields = ['raw_material','product','quantity','cost']

class RawMaterialCreateForm(forms.ModelForm):
	class Meta:
		model = RawMaterial
		fields = ['name','description','cost','image','unit_of_mesure']