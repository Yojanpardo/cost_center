from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from .models import Product
from raw_materials.models import RawMaterialDetail
from manpower.models import ManpowerDetail
from .forms import CreateProductForm
from django.urls import reverse_lazy

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = "products/list.html"
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/detail.html"
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        raw_material_cost = 0
        manpower_cost = 0
        product = self.get_object()
        raw_materials = RawMaterialDetail.objects.filter(product=product)
        manpower = ManpowerDetail.objects.filter(product=product)

        for raw_material in raw_materials:
        	raw_material.cost = round(raw_material.raw_material.cost * raw_material.quantity, 2)
        	raw_material_cost = round(raw_material_cost + raw_material.cost,2)

        for worker in manpower:
            worker.cost = round(worker.manpower.cost_per_hour * worker.time, 2)
            manpower_cost = round(manpower_cost + worker.cost,2)

        cost = manpower_cost + raw_material_cost
        context['manpower'] = manpower
        context['manpower_cost'] = manpower_cost
        context['cost_per_unit'] = round(cost/product.quantity, 2)
        context['raw_materials_cost'] = raw_material_cost
        context['raw_materials'] = raw_materials
        return context

class ProductCreateView(CreateView):
    model = Product
    template_name = "products/new.html"
    form_class = CreateProductForm
    success_url = reverse_lazy('home')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/delete.html"
    context_object_name = "product"
    success_url = reverse_lazy('products:list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name','description','image','quantity']
    template_name = "products/update.html"
    context_object_name = 'product'

    def get_success_url(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return reverse_lazy('products:cost',kwargs={'pk':pk})
