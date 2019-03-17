from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
	what = models.CharField("select an item", max_length=100)
	description = models.TextField(max_length=250)

	def __str__(self):
		return self.what

class NeededItem(models.Model):
	item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
	description = models.TextField(max_length=250)
	quantity = models.IntegerField()
	location = models.TextField(max_length=250)

	def __str__(self):
		return self.item
