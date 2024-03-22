from django.db import models

# Create your models here.

class Employee(models.Model):
	epid = models.CharField(max_length=10)
	ename = models.CharField(max_length=50)
	esal = models.IntegerField(default=15000)
	edesg = models.CharField(max_length=50)
