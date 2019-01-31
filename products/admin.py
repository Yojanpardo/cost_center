from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'description',
		'image',
		'quantity',
	)
	fieldsets = (
		('Product',{
			'fields':(
				('name','quantity','image',),
				('description',),
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