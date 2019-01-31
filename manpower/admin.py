from django.contrib import admin
from .models import Manpower, ManpowerDetail

# Register your models here.

@admin.register(Manpower)
class ManpowerAdmin(admin.ModelAdmin):
	"""docstring for ManpowerAdmin"""
	list_display = (
		'pk',
		'name',
		'cost_per_hour',
	)
	search_fields = (
		'Manpower__name',
		'Manpower__cost_per_hour',
	)
	fieldsets = (
		('Manpower',{
			'fields':(
				('name','cost_per_hour',),
				('image',),
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

@admin.register(ManpowerDetail)
class ManpowerDetailAdmin(admin.ModelAdmin):
	list_display = (
		'pk',
		'manpower',
		'product',
		'time',
	)
	