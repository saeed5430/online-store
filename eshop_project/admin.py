from django.contrib import admin
from . import models


class productAdmin(admin.ModelAdmin):
    list_filter = ['category','is_active']
    list_display = ['title','price','is_active','is_delete']
    list_editable = ['price','is_active']

admin.site.register(models.Product,productAdmin)
admin.site.register(models.productcategory)
admin .site.register(models.productTag)
admin.site.register(models.productBrand)