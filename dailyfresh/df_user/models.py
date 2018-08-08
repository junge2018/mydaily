from django.db import models

# Create your models here.

class User_info(models.Model):
	"""en"""
	uname = models.CharField(max_length=20)
	upwd = models.CharField(max_length=40)
	uemail = models.CharField(max_length=30, null=True, blank=True)
	ureceive = models.CharField(max_length=50)
	uaddress = models.CharField(max_length=100)
	upost = models.CharField(max_length=6, blank=True, null=True)
	uphone = models.CharField(max_length=14)
	isdelete = models.BooleanField(default=False)
	udate_time = models.DateTimeField()
	utest1 = models.CharField(max_length=100)
	class Meta():
		db_table = "dailyfresh_table"