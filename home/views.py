from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

from django.contrib.auth import login
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # logs in the user immediately
            return redirect('notes.list')  # or wherever you want
    else:
        form = SignUpForm()

    return render(request, 'home/signup.html', {'form': form})

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class Homeview(TemplateView):
    template_name = 'home/index.html'
    extra_context = {'today': datetime.today()}

class Authorizedview(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = 'admin/'
