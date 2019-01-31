from django.contrib import admin
from .models import RawMaterial, RawMaterialDetail

# Register your models here.

@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
	"""docstring for RawMaterialAdmin"""
	list_display = (
		'pk',
		'name',
		'cost',
		'unit_of_mesure',
	)
	list_display_links = ('pk',)
	list_editable = (
		'name',
		'cost',
	)
	search_fields = (
		'raw_material__name',
		'raw_material__description',
	)
	fieldsets = (
		('Raw Materials',{
			'fields':(
				('name','description',),
				('image','unit_of_mesure','cost',),
			)
		}),
		('Metadata',{
			'fields':(
				('created','modified',),
			)
		}),
	)

	readonly_fields = (
		'created',
		'modified',
	)

@admin.register(RawMaterialDetail)
class RawMaterialDetailAdmin(admin.ModelAdmin):
	list_display = (
		'pk',
		'raw_material',
		'product',
		'quantity',
		'cost',
	)
	fieldsets = (
		('Details',{
			'fields':(
				('raw_material','product',),
				('quantity','cost'),
			)
		}),
		('Metadata',{
			'fields':(
				('created','modified',),
			)
		}),
	)

	readonly_fields = (
		'created',
		'modified',
	)
