from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import date

class Item(models.Model):
	what = models.CharField("select an item", max_length=100)
	description = models.TextField(max_length=250)

	def __str__(self):
		return self.what

class NeededItem(models.Model):
	date = models.DateField(default=now())
	item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
	description = models.TextField(max_length=250)
	quantity = models.IntegerField()
	address = models.TextField(max_length=250)
	# fulfilled_by = 

	def __str__(self):
		return self.item.__str__()
