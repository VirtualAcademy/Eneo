from __future__ import unicode_literals

import logging
from django.db import models
from datetime import datetime, time

from django.utils.translation import ugettext, ugettext_lazy as _
from fuel.models import Powerplant

# Create your models here.

log = logging.getLogger('models')

# Create your models here.


class Generators(models.Model):
    group_number = models.PositiveIntegerField(
        verbose_name=_("Generator Number"),
        help_text=_("Number given to identify the generator"), default=1)
    power_units = models.BigIntegerField(
        verbose_name=_("Power Available"),
        help_text=_("Amount of power that can be generated"), default=0)
    location = models.CharField(verbose_name=_("Plant Location"), max_length=256,
                                help_text=_("The power plant ocation of the generator"))
    date_recorded = models.DateField(default=datetime.today, blank=False)
    time_recorded = models.TimeField(default=datetime.today, blank=False)


    def __str__(self):
        return "Groupe {}".format(self.group_number)


    class Meta:
        verbose_name = _("Power Plant Generator")
        verbose_name_plural = _("Power Plant Generators")


class PowerAvailable(models.Model):

    power_plant = models.ForeignKey(Powerplant, on_delete=models.CASCADE, verbose_name=_("Power Plant"), help_text=_("The power plant making declaration"))
    power_units = models.BigIntegerField(
        verbose_name=_("Power Available"),
        help_text=_("Amount of power that can be generated"), default=0)
    location = models.CharField(verbose_name=_("Plant Location"), max_length=256,
                                help_text=_("The power plant ocation of the generator"))
    date_recorded = models.DateField(default=datetime.today, blank=False)
    time_recorded = models.TimeField(default=datetime.today, blank=False)

    def __str__(self):
        return "Power available at {} on {}".format(self.power_plant, self.date_recorded.isoformat(),
                                                    self.time_recorded.isoformat())


    class Meta:
        verbose_name = _("Total Power Available")
        verbose_name_plural = _("Total Power Available")



class Demand(models.Model):
    power_consumer= models.CharField(verbose_name=_("Power Consumer"), max_length=256,help_text=_("The name of power consumer."))
    power_units = models.BigIntegerField(
        verbose_name=_("Power Available"),
        help_text=_("Amount of power that can be generated"), default=0)
    unit_measurement = models.CharField(verbose_name=_("Unit of measurement"), max_length=256,
                                        help_text=_("The unit of measurement in which power is quantified"))
    date_recorded = models.DateField(default=datetime.today, blank=False)
    time_recorded = models.TimeField(default=datetime.today, blank=False)

    def __str__(self):
        return "Deamand from {}".format(self.power_consumer)


    class Meta:
        verbose_name = _("Consumer")
        verbose_name_plural = _("Consumers")


class Production(models.Model):
    power_plant = models.ForeignKey(Powerplant, on_delete=models.CASCADE, verbose_name=_("Power Plant"), help_text=_("The power plant making declaration"))
    power_units = models.BigIntegerField(
        verbose_name=_("Power Available"),
        help_text=_("Amount of power that can be generated"), default=0)
    location = models.CharField(verbose_name=_("Plant Location"), max_length=256,
                                help_text=_("The power plant ocation of the generator"))
    date_recorded = models.DateField(default=datetime.today, blank=False)
    time_recorded = models.TimeField(default=datetime.today, blank=False)


    def __str__(self):
        return "Power available at {} on {}".format(self.power_plant, self.date_recorded.isoformat(),
                                                    self.time_recorded.isoformat())

    class Meta:
        verbose_name = _("Production")
        verbose_name_plural = _("Productions")


