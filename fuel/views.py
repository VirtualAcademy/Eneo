from django.shortcuts import render, redirect, render_to_response
from django.views.generic import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import *

# Create your views here.


def storage(request):
    storage = Storageunit.objects.all()
    variation = Stockvariation.objects.all()

    template = 'fuel/storage.html'
    kwvars = {
        'svar': variation,
    }
    print(storage)
    return render_to_response(template, context=kwvars)

def home(request):
    return render(request,'index.html')


def userdashboard(request, username):
    context = {'username':username}
    return render(request, 'fuel/dashboard.html', context=context)


def profile(request):
     if request.user.is_authenticated:
         user_groups = request.user.groups.values_list('name', flat=True)
         if request.user.is_superuser:
             return redirect("/admin")
         else:
             url = reverse('userdashboard', kwargs={'username': request.user})
             return HttpResponseRedirect(url)


class FuelDetailsView(DetailView):
    model = Storageunit
    context_object_name = 'fuel_details'
    template_name = 'fuel/fuel_details.html'

