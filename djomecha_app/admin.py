from django.contrib import admin
from djomecha_app.models import *

class ItemsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemsAdmin)        
# Register your models here.
