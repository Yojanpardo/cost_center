from django.contrib import admin
from .models import Company

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	list_display = (
		'pk',
		'name',
		'nit',
		'user',
	)
	search_fields = (
		'company__name',
		'company__user',
	)
	fieldsets = (
		('Company',{
			'fields':(
				('user','name','nit',),
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