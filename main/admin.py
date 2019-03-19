from django.contrib import admin
from .models import Item, NeededItem, Profile, Photo

# Register models here
admin.site.register(Item)
admin.site.register(NeededItem)
admin.site.register(Profile)
admin.site.register(Photo)