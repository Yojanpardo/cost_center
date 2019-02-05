from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class LoginView(auth_views.LoginView):
	template_name='accounts/login.html'
	redirect_authenticated_user = True

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout View."""