from django.urls import path
from . import views
urlpatterns = [
	path('new/',views.RawMaterialCreateView.as_view(), name='new'),
	path('add-to/<int:pk>/', views.RawMaterialDetailCreateView.as_view(), name='add_raw_material'),
]