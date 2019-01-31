from django.urls import path
from . import views

urlpatterns = [
	path('',views.ProductListView.as_view(),name='list'),
	path('new/',views.ProductCreateView.as_view(), name='new'),
	path('detail/<int:pk>', views.ProductDetailView.as_view(), name='cost'),
	path('update/<int:pk>', views.ProductUpdateView.as_view(), name='update'),
	path('delete/<int:pk>', views.ProductDeleteView.as_view(), name='delete'),
]