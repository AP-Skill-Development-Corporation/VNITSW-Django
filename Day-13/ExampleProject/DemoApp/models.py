from django.db import models

# Create your models here.

class Employee(models.Model):
	k = [
		('0','Select Your Designation'),
		('1','Junior Trainee'),
		('2','Senior Trainer'),
		('3','Intern'),
	]
	epid = models.CharField(max_length=10)
	ename = models.CharField(max_length=50)
	esal = models.IntegerField(default=15000)
	edesg = models.CharField(max_length=10,default='0',choices=k)
