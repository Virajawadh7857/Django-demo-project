from django.contrib import admin
from .models import Product

class AdminProduct(admin.ModelAdmin):
    list_display = ['pid','pname','pcost','pcolor','pmfd','pexd']

admin.site.register(Product,AdminProduct)
