from django.db import models
from datetime import datetime


class Upload(models.Model):
	name = models.CharField(max_length=32)
	Filesie = models.CharField(max_length=10)
	path = models.CharField(max_length=32)
	Datetime = models.DateTimeField(default=datetime.now)
	code = models.CharField(max_length=8)
	DownloadDocount = models.IntegerField(default=0)
	PCIP = models.CharField(max_length=32)

	def __str__(self):
		return self.name
