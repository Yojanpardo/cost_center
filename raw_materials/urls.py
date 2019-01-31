from django.urls import path
from . import views
urlpatterns = [
	path('add-to/<int:pk>/', views.RawMaterialDetailCreateView.as_view(), name='add_raw_material'),
]