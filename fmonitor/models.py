from __future__ import unicode_literals

import logging

from django.core.exceptions import ValidationError
from django.db import models

from django.utils.translation import ugettext, ugettext_lazy as _

#### ----------------------  SUPPLIER MODEL  ---------------- #########


from common import generate_public_key
from common.model_mixins import (
    StatusModelMixin, StatusModelManagerMixin, ValidateOnSaveMixin,
    UserModelMixin, TimeModelMixin, StatusModelMixin, StatusModelManagerMixin,
    ValidateOnSaveMixin)


log = logging.getLogger('models')


#
# Country
#
class CountryManager(StatusModelManagerMixin, models.Manager):
    pass


class Country(StatusModelMixin):
    """
    This model implements country codes.
    """
    country = models.CharField(
        verbose_name=_("Country"), max_length=100,
        help_text=_("The country name."))
    code = models.CharField(
        verbose_name=_("Code"), max_length=2, db_index=True,
        unique=True, help_text=_("The two character country code."))

    objects = CountryManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return "{} ({})".format(self.country, self.code)

    class Meta:
        ordering = ('country',)
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")


#
# Subdivision
#
class SubdivisionManager(StatusModelManagerMixin, models.Manager):
    pass


class Subdivision(StatusModelMixin):
    """
    This model implements country subdivision codes.
    """
    subdivision_name = models.CharField(
        verbose_name=_("State"), max_length=130,
        help_text=_("The subdivision of the country."))
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, verbose_name=_("Country"),
        db_index=False, related_name='subdivisions',
        help_text=_("The country."))
    code = models.CharField(
        verbose_name=_("State Code"), max_length=10,
        help_text=_("The subdivision code."))

    objects = SubdivisionManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subdivision_name

    class Meta:
        unique_together = ('country', 'code')
        ordering = ('country', 'subdivision_name',)
        verbose_name = _("Subdivision")
        verbose_name_plural = _("Subdivisions")


#
# Language
#
class LanguageManager(StatusModelManagerMixin, models.Manager):
    pass


class Language(StatusModelMixin, ValidateOnSaveMixin, models.Model):
    """
    This model implements language codes.
    """
    locale = models.CharField(
        verbose_name=_("Locale"), max_length=5, unique=True, blank=True,
        help_text=_("The language and country codes."))
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, verbose_name=_("Country"),
        related_name='languages', help_text=_("The country."))
    code = models.CharField(
        verbose_name=_("Language Code"), max_length=2,
        help_text=_("The two character language code."))

    objects = LanguageManager()

    def clean(self):
        if self.pk is None:
            self.locale = "{}-{}".format(self.code, self.country.code.upper())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.locale

    class Meta:
        ordering = ('locale',)
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")


#
# TimeZone
#
class TimeZoneManager(StatusModelManagerMixin, models.Manager):
    pass


class TimeZone(StatusModelMixin):
    """
    This model implements timezone codes.
    """
    zone = models.CharField(
        verbose_name=_("Timezone"), max_length=40,
        help_text=_("The timezone (zoneinfo)."))
    coordinates = models.CharField(
        verbose_name=_("Coordinates"), max_length=20,
        help_text=_("Latitude & Longitude."))
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, verbose_name=_("Country"),
        db_index=False, related_name='timezones', help_text=_("The country."))
    desc = models.TextField(
        verbose_name=_("Description"), null=True, blank=True,
        help_text=_("Zone description."))

    objects = TimeZoneManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.zone

    class Meta:
        unique_together = ('country', 'zone',)
        ordering = ('zone',)
        verbose_name = _("Time Zone")
        verbose_name_plural = _("Time Zones")


#
# Currency
#
class CurrencyManager(StatusModelManagerMixin, models.Manager):
    pass


class Currency(StatusModelMixin):
    """
    This model implements currency codes.
    """
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, verbose_name=_("Country"),
        db_index=False, help_text=_("Country or region name."))
    currency = models.CharField(
        verbose_name=_("Corrency"), max_length=50,
        help_text=_("Name of the currency."))
    alphabetic_code = models.CharField(
        verbose_name=_("Alphabetic Code"), max_length=3,
        help_text=_("3 digit alphabetic code for the currency."))
    numeric_code = models.PositiveSmallIntegerField(
        verbose_name=_("Numeric Code"),
        help_text=_("3 digit numeric code."))
    minor_unit = models.PositiveSmallIntegerField(
        verbose_name=_("Minor Unit"),
        help_text=_("Number of digits after the decimal separator."))
    symbol =  models.CharField(
        verbose_name=_("Symbol"), max_length=6, null=True, blank=True,
        help_text=_("The symbol representing this currency."))

    objects = CurrencyManager()

    def __str__(self):
        # TODO -- This needs to be cached.
        return "{} ({})".format(self.country.country, self.currency)

    class Meta:
        unique_together = ('country', 'alphabetic_code',)
        ordering = ('country__country', 'currency',)
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")

### ------------------------------------------------------########


class SupplierManager(StatusModelManagerMixin, models.Manager):
    pass


class Supplier(TimeModelMixin, UserModelMixin, StatusModelMixin,
               ValidateOnSaveMixin, models.Model):
    """
    Supplier, can be either a manufacturer or a distributor based on the `type`
    field.
    """
    BOTH_MFG_DIS = 0
    MANUFACTURER = 1
    DISTRIBUTOR = 2
    SUPPLIER_TYPE = (
        (BOTH_MFG_DIS, _('MFG & Dist')),
        (MANUFACTURER, _('Manufacturer')),
        (DISTRIBUTOR, _('Distributor')),
        )

    public_id = models.CharField(
        verbose_name=_("Public Supplier ID"), max_length=30, unique=True,
        blank=True,
        help_text=_("Public ID to identify a individual supplier."))
    # product = models.ForeignKey(
    #     Product, on_delete=models.CASCADE, verbose_name=_("Product"),
    #     related_name='suppliers', db_index=False,
    #     help_text=_("The product that owns this record."))
    name = models.CharField(
        verbose_name=_("Name"), max_length=250,
        help_text=_("The name of the supplier."))
    address_01 = models.CharField(
        verbose_name=_("Address 1"), max_length=50, null=True, blank=True,
        help_text=_("Address line one."))
    address_02 = models.CharField(
        verbose_name=_("Address 2"), max_length=50, null=True, blank=True,
        help_text=_("Address line two."))
    city = models.CharField(
        verbose_name=_("City"), max_length=30, null=True, blank=True,
        help_text=_("The city of the supplier."))
    subdivision = models.ForeignKey(
        Subdivision, on_delete=models.CASCADE,
        verbose_name=_("State/Province"), null=True, blank=True,
        help_text=_("The subdivision in the country."))
    postal_code = models.CharField(
        verbose_name=_("Postal Code"), max_length=15, null=True, blank=True,
        help_text=_("The postal code in the country."))
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, verbose_name=_("Country"),
        null=True, blank=True, help_text=_("The country."))
    phone = models.CharField(
        verbose_name=_("Phone"), max_length=20, null=True, blank=True,
        help_text=_("The phone number of the supplier."))
    fax = models.CharField(
        verbose_name=_("FAX"), max_length=20, null=True, blank=True,
        help_text=_("The fax number of the supplier"))
    email = models.EmailField(
        verbose_name=_("Email"), null=True, blank=True,
        help_text=_("The email of the supplier."))
    url = models.URLField(
        verbose_name=_("URL"), null=True, blank=True,
        help_text=_("The web site of the supplier."))
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, verbose_name=_("Language"),
        null=True, blank=True, help_text=_("The language code."))
    timezone = models.ForeignKey(
        TimeZone, on_delete=models.CASCADE, verbose_name=_("Timezone"),
        null=True, blank=True, help_text=_("The timezone."))
    stype = models.SmallIntegerField(
        verbose_name=_("Supplier Type"), choices=SUPPLIER_TYPE,
        help_text=_("The type of supplier."))

    objects = SupplierManager()

    def clean(self):
        # Populate the public_id on record creation only.
        if self.pk is None and not self.public_id:
            self.public_id = generate_public_key()

        # Populate the name_lower field.
        self.name = self.name.strip()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        # unique_together = ('product', 'name',)
        ordering = ('name',)
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")

    def url_producer(self):
        result = _("No URL")

        if self.url:
            result = ('<a href="{0}">{0}</a>').format(self.url)

        return result
    url_producer.short_description = _("Company URL")
    url_producer.allow_tags = True


# Create your models here.
# class Userprofile(models.Model):
#     userpid = models.CharField(verbose_name=_("Public User ID"), max_length=30, unique=True,
#                                blank=True, help_text=_("Public ID to identify a individual category."))
#     role
#     dob
#     address



class CategoryManager(models.Manager):

    def create_category_tree(self, product, user, cat_name_tree, parents=None):
        """
        Gets and/or creates designated category, creating parent categories
        as necessary. Returns a list of objects in category order or an empty
        list if `cat_name_tree` is the wrong data type.
        """
        tree = []

        if parents is None or isinstance(parents, self.model):
            parents = [parents]

        if not isinstance(cat_name_tree, (list, tuple)):
            cat_name_tree = [cat_name_tree]

        len_parents = len(parents)
        len_roots = len(cat_name_tree)

        if len_roots > 1:
            if not len_parents:
                msg = _("Multiple roots need at least one parent.")
                raise ValueError(msg)

            if len_parents > 1 and len_parents != len_roots:
                msg = _("If multiple roots the number parents must be one, "
                        "or equal to the number of roots.")
                raise ValueError(msg)

        for idx, item in enumerate(cat_name_tree):
            parent = parents[0] if len_parents == 1 else parents[idx]
            nodes, junk = self._recurse_names(product, user, item, parent)
            tree.append(nodes)

        return tree

    def _recurse_names(self, product, user, item, parent):
        tree = []
        node = None
        outer_parent = parent

        if isinstance(item, (list, tuple)):
            if len(item) > 1:
                hold = all([isinstance(x, (list, tuple)) for x in item])
            else:
                hold = False

            for next in item:
                parent = outer_parent if hold else parent
                nodes, parent = self._recurse_names(
                    product, user, next, parent)
                tree.append(nodes)
        else:
            kwargs = {}
            kwargs['creator'] = user
            kwargs['updater'] = user
            node, created = self.get_or_create(product=product, parent=parent,
                                               name=item, defaults=kwargs)
            tree = node

        return tree, node

    def delete_category_tree(self, product, node_list):
        """
        Deletes the category tree back to the beginning, but will stop if
        there are other children on the category. The result is that it
        will delete whatever was just added. This is useful for rollbacks.
        The 'node_list' should be a flat list of end level categories. A
        list of strings is returned representing the deleted nodes.
        """
        paths = []

        if not isinstance(node_list, (models.QuerySet, list, tuple)):
            node_list = [node_list]

        for node in node_list:
            if node.product != product:
                msg = _("Trying to delete category '{}' with invalid product, "
                        "updater: {}, updated: {}, product: {}, "
                        "invalid product: {}").format(
                    node, node.updater, node.updated, node.product, product)
                log.error(ugettext(msg))
                raise ValueError(msg)

            deleted = self._recurse_delete(node)

            if len(deleted) > 0:
                paths.append(deleted)

        return paths

    def _recurse_delete(self, node):
        paths = []

        if node.children.count() <= 0:
            parent = node.parent
            paths.append(node.path)
            node.delete()

            if parent:
                [paths.append(path) for path in self._recurse_delete(parent)]

        return paths

    def get_parents(self, product, category):
        """
        Get all the parents to this category object.
        """
        if category.product != product or not category.product.public:
            msg = _("Trying to access a category '{}' with an invalid "
                    "product, updater: {}, updated: {}, product: {}, invalid "
                    "product: {}").format(
                category, category.updater, category.updated,
                category.product, product)
            log.error(ugettext(msg))
            raise ValueError(msg)

        parents = self._recurse_parents(category)
        parents.reverse()
        return parents

    def _recurse_parents(self, category):
        parents = []

        if category.parent:
            parents.append(category.parent)
            parents.extend(self._recurse_parents(category.parent))

        return parents

    def get_child_tree_from_list(self, product, node_list, with_root=True):
        """
        Given a list of Category objects, return a list of all the
        Categories plus all the Categories' children, plus the children's
        children, etc. For example, if the ['Arts', 'Color'] Categories
        are passed in `node_list`, this function will return
        [['Arts', [['Arts>Music', 'Arts>Music>Local']]],
         ['Color', [['Color>Blue','Color>Green', 'Color>Red']]]] objects.
        Lists are compressed if they only have a single value.
        """
        tree = []

        if not isinstance(node_list, (models.QuerySet, list, tuple)):
            node_list = [node_list]

        for node in node_list:
            if node.product != product or not node.product.public:
                msg = _("The category '{0}' is not in the '{1}' product or "
                        "the '{0}' product is not public."
                        ).format(node, product)
                raise ValueError(msg)

            children = self._recurse_children(node)

            if with_root:
                nodes = []
                nodes.append(node)
                nodes.append(children)
            else:
                nodes = children

            tree.append(nodes)

        return tree

    def _recurse_children(self, item):
        tree = []

        for child in item.children.all():
            nodes = self._recurse_children(child)
            nodes.insert(0, child)
            len_nodes = len(nodes)

            if len_nodes == 1:
                tree.append(nodes[0])
            elif len_nodes > 1:
                tree.append(nodes)

        return tree

    def get_all_root_trees(self, product, name):
        """
        Given a category 'name' and 'product' return a list of trees where
        each tree has the category 'name' as one of its members.
        ex. [[<color>, <color>red>, <color>green>], [<light>, <light>red>]]
        Red is in both trees.
        """
        result = []
        records = self.filter(product=product, name=name)

        if len(records) > 0:
            result[:] = [self.get_parents(product, record)
                         for record in records]

        return result


class Category(TimeModelMixin, UserModelMixin, ValidateOnSaveMixin,
               models.Model):
    DEFAULT_SEPARATOR = '>'

    public_id = models.CharField(
        verbose_name=_("Public Category ID"), max_length=30, unique=True,
        blank=True,
        help_text=_("Public ID to identify a individual category."))
    # product = models.ForeignKey(
        # Product, on_delete=models.CASCADE, verbose_name=_("Product"),
        # related_name='categories', db_index=False,
        # help_text=_("The product that owns this record."))
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name=_("Parent"),
        blank=True, null=True, default=None, related_name='children',
        help_text=_("The parent to this category if any."))
    name = models.CharField(
        verbose_name=_("Name"), max_length=250,
        help_text=_("The name of this category."))
    path = models.CharField(
        verbose_name=_("Full Path"), max_length=1000, editable=False,
        help_text=_("The full hierarchical path of this category."))
    level = models.SmallIntegerField(
        verbose_name=_("Level"), editable=False,
        help_text=_("The location in the hierarchy of this category."))

    objects = CategoryManager()

    def clean(self):
        # Populate the public_id on record creation only.
        if self.pk is None and not self.public_id:
            self.public_id = generate_public_key()

        if hasattr(self, 'product'):
            self.path = self._get_category_path()
            self.level = self.path.count(self.DEFAULT_SEPARATOR)
            delimiter = self.DEFAULT_SEPARATOR

            # Check that the separator is not in the name.
            if delimiter in self.name:
                raise ValidationError(
                    {'name': _("A category name cannot contain the category "
                               "delimiter '{}'.").format(delimiter)})

            if self.parent:
                # Check that this category is not a parent.
                parents = Category.objects.get_parents(
                    self.product, self.parent)
                parents.append(self.parent)

                for parent in parents:
                    if parent.name == self.name:
                        raise ValidationError(
                            {'name': _("A category in this tree with name "
                                       "[{}] already exists.").format(
                                 self.name)})
            # Check that a root level name does not already exist for this
            # product on a create only.
            elif self.pk is None and Category.objects.filter(
                name=self.name, product=self.product, level=0).count():
                raise ValidationError(
                    {'name': _("A root level category name [{}] already "
                               "exists.").format(self.name)})

    def _get_category_path(self, current=True):
        parents = Category.objects.get_parents(self.product, self)
        if current: parents.append(self)
        return self.DEFAULT_SEPARATOR.join([parent.name for parent in parents])

    def get_children(self):
        """
        Returns a list of Category objects that are children of this category.
        """
        children = Category.objects.get_child_tree_from_list(
            self.product, (self,), with_root=False)
        return children

    def get_children_and_root(self):
        """
        Return a list of Category objects that are children of this category
        including this category.
        """
        children = Category.objects.get_child_tree_from_list(
            self.product, (self,))
        return children[0]

    def parents_producer(self):
        return self._get_category_path(current=False)
    parents_producer.short_description = _("Category Parents")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Fix all children if any.
        for child in self.children.all():
            child.save()

    def __str__(self):
        return "{}".format(self.path)

    class Meta:
        # unique_together = ('product', 'parent', 'name',)
        ordering = ('path',)
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Role(models.Model):
    role_id = models.CharField(verbose_name=_("Public Role ID"), max_length=30, unique=True,
                               blank=True, help_text=_("Public ID to identify a individual role."))
    role_name = models.CharField(
        verbose_name=_("Name"), max_length=250,
        help_text=_("The name of this category."))
    role_descr  = models.TextField(
        verbose_name=_("Description"), max_length=1000, null=True, blank=True,
        help_text=_("Role description."))

    def __str__(self):
        return "{}".format(self.path)

    class Meta:
        verbose_name = _("Role")
        verbose_name_plural = _("Roles")


class Product(models.Model):
    pdt_id = models.CharField(verbose_name=_("Public Product ID"), max_length=30, unique=True,
                               blank=True, help_text=_("Public ID to identify a individual role."))
    pdt_name = models.CharField(
        verbose_name=_("Name"), max_length=250,
        help_text=_("The name of this product."))
    pdt_descr = models.TextField(
        verbose_name=_("Description"), max_length=1000, null=True, blank=True,
        help_text=_("Product description."))
    supplier  = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, verbose_name=_("Supplier"),
        db_index=False, related_name='invoices',
        help_text=_("The Distributor or manufacturer that supplied the item."))
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name=_("Supplier"),
        db_index=False,
        help_text=_("The Distributor or manufacturer that supplied the item."))
#     unitsinstock
#     unitsonorder
#     pdtavailable
#     reorderlevel
#     currentorder
#     note
#
# # class Category(models.Model):
# #     catid
# #     catname = models.CharField(
# #         verbose_name=_("Name"), max_length=250,
# #         help_text=_("The name of this category."))
# #     catdescr  = models.TextField(
# #         verbose_name=_("Description"), max_length=1000, null=True, blank=True,
# #         help_text=_("Category description."))
#
# class Order(models.Model):
#     orderid
#     user
#     customer = models.ForeignKey(
#         Customer, on_delete=models.CASCADE, verbose_name=_("Customer"),
#         related_name='categories', db_index=False,
#         help_text=_("The customer that owns this record."))
#     orderdate
#     dispatchdate
#     errormsg
#     deleted
#
#
# class OrderDetails(models.Model):
#     orddetailid
#     order
#     product
#     ordqty
#     delqty
#     orderdate
#     dispatchdate
#     total

# class Supplier(models.Model):
#     supplerid
#     companyname = models.CharField(
#         verbose_name=_("Name"), max_length=250,
#         help_text=_("The name of the company."))
#     address

