from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CreateRawMaterialDetailForm, RawMaterialCreateForm
from .models import RawMaterialDetail, RawMaterial
from products.models import Product
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class RawMaterialCreateView(LoginRequiredMixin,CreateView):
    model = RawMaterial
    template_name = "raw_materials/new.html"
    form_class = RawMaterialCreateForm
    success_url = reverse_lazy('home')
    
class RawMaterialDetailCreateView(LoginRequiredMixin,CreateView):
    model = RawMaterialDetail
    template_name = "raw_materials/add_raw_material.html"
    form_class = CreateRawMaterialDetailForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_pk = self.kwargs.get(self.pk_url_kwarg)
        product = Product.objects.get(pk=product_pk)
        raw_materials = RawMaterial.objects.all()
        context['raw_materials'] = raw_materials
        context['product'] = product
        return context

    def get_success_url(self):
    	product_pk = self.kwargs.get(self.pk_url_kwarg)
    	return reverse_lazy('products:cost',kwargs={'pk':product_pk})