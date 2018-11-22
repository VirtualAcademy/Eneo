from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Demand)
admin.site.register(Generators)
admin.site.register(PowerAvailable)
admin.site.register(Production)


