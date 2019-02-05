from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.contrib.auth.mixins import LoginRequiredMixin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="home.html"),name='home'),
    path('products/', include(('products.urls','products'),namespace='products')),
    path('raw-materials/', include(('raw_materials.urls','raw_materials'),namespace='raw_materials')),
    path('accounts/',include(('accounts.urls','accounts'),namespace='accounts')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
