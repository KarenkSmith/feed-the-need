from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import date

class Item(models.Model):
	what = models.CharField("select an item", max_length=100)
	description = models.TextField(max_length=250)

	def __str__(self):
		return self.what

class NeededItem(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField(default=now())
	item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
	description = models.TextField(max_length=250)
	quantity = models.IntegerField(default=1)
	address = models.TextField(max_length=250)
	donated_by = models.ForeignKey(User, related_name="donated", null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.item.__str__()

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	org_name = models.CharField(max_length=50)
	address = models.TextField(max_length=250, null=True)
	phone_number = models.IntegerField
	org_description = models.TextField(max_length=250, null=True)
	org_url =  models.URLField(max_length=250, null=True)
	wish_list =  models.URLField(max_length=250, null=True)




