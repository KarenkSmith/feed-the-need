from django.db import models

class Item(models.Model):
	what = models.CharField(max_length=100)
	description = models.TextField(max_length=250)

	def __str__(self):
		return self.what
