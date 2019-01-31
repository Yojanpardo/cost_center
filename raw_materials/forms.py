from django import forms
from .models import RawMaterialDetail
class CreateRawMaterialDetailForm(forms.ModelForm):
	class Meta:
		model = RawMaterialDetail
		fields = ['raw_material','product','quantity','cost']