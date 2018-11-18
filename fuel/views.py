from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import *

# Create your views here.


def home(request):
    return render(request,'index.html')


def userdashboard(request, username):
    return render(request, 'fuel/dashboard.html')


def profile(request):
     if request.user.is_authenticated:
         user_groups = request.user.groups.values_list('name', flat=True)
         if request.user.is_superuser:
             return redirect("/admin")
         else:
             url = reverse('userdashboard', kwargs={'username': request.user})
             return HttpResponseRedirect(url)
             # return HttpResponseRedirect("/dashboard/{}".format(request.user))


class FuelDetailsView(DetailView):
    model = Storageunit
    context_object_name = 'fuel_details'
    template_name = 'fuel/fuel_details.html'

