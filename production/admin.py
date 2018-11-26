from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Generators)
class GeneratorsAdmin(admin.ModelAdmin):
    list_display = ('location', 'time_recorded')
    # list_filter = ('location', 'date_recorded')

    # fieldsets = (
    #     ('Date', {
    #         'fields': ('group_number', 'power_units', 'location')
    #     }),
    #     # ('Availability', {
    #     #     'fields': ('status', 'due_back')
    #     # }),
    # )


@admin.register(PowerAvailable)
class PowerAvailableAdmin(admin.ModelAdmin):
    list_display = ('location','power_units', 'time_recorded', 'date_recorded')

admin.site.register(Demand)
admin.site.register(Production)


