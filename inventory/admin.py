from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Family)
class FamilyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass
