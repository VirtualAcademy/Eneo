from __future__ import unicode_literals

import logging
from django.db import models

from django.utils.translation import ugettext, ugettext_lazy as _
# Create your models here.

log = logging.getLogger('models')


# class Category(models.Model):
#     DEFAULT_SEPARATOR = '>'
#     HFO = "Heavy Fuel"
#     LFO = "Light Fuel"
#     THERM = "Thermal"
#     HYDRO = "Hydro"
#     TYPES = (("HFO",HFO), ("LFO",LFO),("HYDR",HYDRO),("THERM",THERM),)
#
#     # public_id = models.CharField(
#     #     verbose_name=_("Public Category ID"), max_length=30, unique=True,
#     #     blank=True,
#     #     help_text=_("Public ID to identify a individual category."))
#     parent = models.ForeignKey(
#         "self", on_delete=models.CASCADE, verbose_name=_("Parent"),
#         blank=True, null=True, default=None, related_name='children',
#         help_text=_("The parent to this category if any."))
#     name = models.CharField(
#         verbose_name=_("Name"), max_length=250,
#         help_text=_("The name of this category."))
#     path = models.CharField(
#         verbose_name=_("Full Path"), max_length=1000, editable=False,
#         help_text=_("The full hierarchical path of this category."))
#     level = models.SmallIntegerField(
#         verbose_name=_("Level"),
#         help_text=_("The location in the hierarchy of this category."))

    # objects = CategoryManager()
    #
    # def clean(self):
    #     # Populate the public_id on record creation only.
    #     if self.pk is None and not self.public_id:
    #         self.public_id = generate_public_key()
    #
    #     if hasattr(self, 'product'):
    #         self.path = self._get_category_path()
    #         self.level = self.path.count(self.DEFAULT_SEPARATOR)
    #         delimiter = self.DEFAULT_SEPARATOR
    #
    #         # Check that the separator is not in the name.
    #         if delimiter in self.name:
    #             raise ValidationError(
    #                 {'name': _("A category name cannot contain the category "
    #                            "delimiter '{}'.").format(delimiter)})
    #
    #         if self.parent:
    #             # Check that this category is not a parent.
    #             parents = Category.objects.get_parents(
    #                 self.product, self.parent)
    #             parents.append(self.parent)
    #
    #             for parent in parents:
    #                 if parent.name == self.name:
    #                     raise ValidationError(
    #                         {'name': _("A category in this tree with name "
    #                                    "[{}] already exists.").format(
    #                              self.name)})
    #         # Check that a root level name does not already exist for this
    #         # product on a create only.
    #         elif self.pk is None and Category.objects.filter(
    #             name=self.name, product=self.product, level=0).count():
    #             raise ValidationError(
    #                 {'name': _("A root level category name [{}] already "
    #                            "exists.").format(self.name)})
    #
    # def _get_category_path(self, current=True):
    #     parents = Category.objects.get_parents(self.product, self)
    #     if current: parents.append(self)
    #     return self.DEFAULT_SEPARATOR.join([parent.name for parent in parents])
    #
    # def get_children(self):
    #     """
    #     Returns a list of Category objects that are children of this category.
    #     """
    #     children = Category.objects.get_child_tree_from_list(
    #         self.product, (self,), with_root=False)
    #     return children
    #
    # def get_children_and_root(self):
    #     """
    #     Return a list of Category objects that are children of this category
    #     including this category.
    #     """
    #     children = Category.objects.get_child_tree_from_list(
    #         self.product, (self,))
    #     return children[0]
    #
    # def parents_producer(self):
    #     return self._get_category_path(current=False)
    # parents_producer.short_description = _("Category Parents")
    #
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     # Fix all children if any.
    #     for child in self.children.all():
    #         child.save()

    # def __str__(self):
    #     return self.name #"{}".format(self.path)
    #
    # class Meta:
    #     # unique_together = ('product', 'parent', 'name',)
    #     ordering = ('path',)
    #     verbose_name = _("Category")
    #     verbose_name_plural = _("Categories")


class Powerplant(models.Model):

    THERM = "Thermal"
    HYDRO = "Hydro"
    TYPES = (("HYDR",HYDRO),("THERM",THERM))

    # plant_id = models.IntegerField(unique=True,primary_key=True,auto_created=True)
    plant_name = models.CharField(
        verbose_name=_("Power Plant Name"), max_length=1000,
        help_text=_("The name power plant concerned .e.g. Limbe Power plant."))
    location = models.CharField(
        verbose_name=_("PowerPlant location"), max_length=1000,
        help_text=_("The location of the power plant concerned."))
    production_capacity = models.CharField(
        verbose_name=_("Production Capacity"),max_length=1000,
        help_text=_("The production capacity."), blank=True)
    # available_power = models.PositiveIntegerField()
    category = models.CharField(
        verbose_name=_("Category"), max_length=256,
        help_text=_("The plant category: hydro or thermal"),choices=TYPES)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"),
    #     help_text=_("The Power Plant category."))

    def __str__(self):
        return self.plant_name

    def getcat(self):
        return self.category

    class Meta:
    #     # unique_together = ('product', 'parent', 'name',)
    #     ordering = ('path',)
        verbose_name = _("Power Plant")
        verbose_name_plural = _("Power Plants")


class Fuel(models.Model):

    HFO = "Heavy Fuel"
    LFO = "Light Fuel"
    TYPES = (("HFO",HFO), ("LFO",LFO))

    # fuel_id = models.IntegerField(unique=True,primary_key=True,auto_created=True)
    fuel_name = models.CharField(
        verbose_name=_("Fuel Name"), max_length=1000,
        help_text=_("The name of fuel type concerned."))
    fdiscription = models.TextField(
        verbose_name=_("Description"), max_length=1000, null=True, blank=True,
        help_text=_("Fuel description."))
    category = models.CharField(
        verbose_name=_("Category"), max_length=256,
        help_text=_("The plant category: HFO or LFO"), choices=TYPES)

    # category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"),
    #     help_text=_("The Fuel."))
    # storage_unit = models.ForeignKey(Storageunit, on_delete=models.CASCADE, verbose_name=_("Storage"),
    #     help_text=_("The fuel reservoir."))

    def getcat(self):
        return self.category

    def __str__(self):
        return """{} > {}""".format(self.fuel_name,self.getcat())

    class Meta:
    #     # unique_together = ('product', 'parent', 'name',)
    #     ordering = ('path',)
        verbose_name = _("Fuel")
        verbose_name_plural = _("Fuel")



class Storageunit(models.Model):
    # storage_id = models.IntegerField(unique=True,primary_key=True,auto_created=True)
    storage_name = models.CharField(
        verbose_name=_("Fuel Tank"), max_length=1000,
        help_text=_("The name of power plant storage unit .e.go LLP starage."))
    # stockvariation = models.ForeignKey('Stockvariation', on_delete=models.CASCADE, verbose_name=_("Inventory Changes"),
    #     help_text=_("The changes or variation in fuel stored in the reservoir location or power plant."))
    capacity = models.CharField(
        verbose_name=_("Storage Unit"),max_length=1000,
        help_text=_("The storage unit for fuel."), blank=True)
    measurement = models.CharField(verbose_name=_("Measurement"), max_length=256,help_text=_("Units of measurement"))
    facility = models.ForeignKey(Powerplant, on_delete=models.CASCADE, verbose_name=_("Storage Facility"),
        help_text=_("The fuel reservoir location or power plant."))
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE, verbose_name=_("Fuel"),
        help_text=_("The fuel product in the reservoir location or power plant."))


    def __str__(self):
        return self.storage_name

    class Meta:
    #     # unique_together = ('product', 'parent', 'name',)
    #     ordering = ('path',)
        verbose_name = _("Storage Unit")
        verbose_name_plural = _("Storage Units")


class Stockvariation(models.Model):
    # sv_id = models.IntegerField(unique=True, primary_key=True, auto_created=True)
    record_date = models.DateTimeField()
    storage_unit = models.ForeignKey(Storageunit, on_delete=models.CASCADE, verbose_name=_("Storage Facility"),
        help_text=_("The record changes in inventory."))
    iniial_qty = models.CharField(verbose_name=_("Initial Quantity"),
        help_text=_("The quantity left of the inventory on previous day."), max_length=1000, blank=True)
    qty_added = models.CharField(verbose_name=_("Quantity Supplied"),
        help_text=_("The quantity added from supply."), max_length=1000, blank=True)
    qty_removed = models.CharField(verbose_name=_("Quantity Consumed"),
        help_text=_("The quantity to be consumed."), max_length=1000, blank=True)
    qty_left = models.CharField(verbose_name=_("Quantity on Hand"),
        help_text=_("The quantity left before consumption."), max_length=1000, blank=True)
    minimum_qty = models.CharField(verbose_name=_("Threshold"),
        help_text=_("The threshold quantity that can't be consumed."), max_length=1000, blank=True)



    def __str__(self):
        return "Recorded on {}".format(self.record_date)

    class Meta:
    #     # unique_together = ('product', 'parent', 'name',)
    #     ordering = ('path',)
        verbose_name = _("Inventory Variation")
        verbose_name_plural = _("Inventory Varations")

    def addstock(self):
        #Storageunit.object.all()
        return

class Consumption(models.Model):
    consumer = models.ForeignKey(Powerplant, on_delete=models.CASCADE, verbose_name=_("Consumer"),
        help_text=_("The fuel reservoir."))
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE, verbose_name=_("Fuel Consumed"),
        help_text=_("The fuel removed from reservoir."))
    quantity = models.CharField(verbose_name=_("Quantity"),
        help_text=_("The quantity that has been consumed."), max_length=1000, blank=True)
    measurement = models.CharField(verbose_name=_("Measurement"), max_length=256,help_text=_("Units of measurement"))
    date = models.DateTimeField()

    def __str__(self):
        return """ {} {} consumed""".format(self.quantity, self.measurement)

class Supplier(models.Model):
    supplier_name = models.CharField(verbose_name=_("Fuel Supplier's Name"), max_length=256,
        help_text=_("The name of the fuel supplier."))

    def __str__(self):
        return self.supplier_name


    class Meta:
    #     # unique_together = ('product', 'parent', 'name',)
    #     ordering = ('path',)
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")


class Supply(models.Model):

    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE, verbose_name=_("Fuel Supplied"),
        help_text=_("The fuel added to reservoir."))
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name=_("Fuel Supplier"),
        help_text=_("The fuel supplied to reservoir."))
    destined_to = models.ForeignKey(Storageunit, on_delete=models.CASCADE, verbose_name=_("Fuel Receptacle"),
        help_text=_("The fuel storage unit."))
    quantity = models.CharField(verbose_name=_("Quantity Supplied"),
        help_text=_("The Supplied quantity."), max_length=1000, blank=True)
    measurement = models.CharField(verbose_name=_("Measurement"), max_length=256,help_text=_("Units of measurement"))
    date = models.DateTimeField()

    def __str__(self):
        return """{} {} Supplied""".format(self.quantity,self.measurement)

    #
    class Meta:
        # unique_together = ('product', 'parent', 'name',)
        # ordering = ('path',)
        verbose_name = _("Supply")
        verbose_name_plural = _("Supplies")
