from django.contrib import admin
from .models import Item, NeededItem

# Register models here
admin.site.register(Item)
admin.site.register(NeededItem)