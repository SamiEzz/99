from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Provider)
admin.site.register(Costumer)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Incident)
admin.site.register(globalConfig)
admin.site.register(ProductCategory)