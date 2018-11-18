from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import *

# Create your views here.


def home(request):
    return render(request,'index.html')


def profile(request):
     if request.user.is_authenticated:
         user_groups = request.user.groups.values_list('name', flat=True)
         if request.user.is_superuser:
             return redirect("/admin")
         else:
             return redirect("/dashboard/{}".format(user_groups[0]))


class FuelDetailsView(DetailView):
    model = Storageunit
    context_object_name = 'fuel_details'
    template_name = 'fuel/fuel_details.html'

