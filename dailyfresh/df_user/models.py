from django.db import models

# Create your models here.
import sys
default_encoding = "utf-8"
if sys.getdefaultencoding() != default_encoding:
	reload(sys)
	sys.setdefaultencoding(default_encoding)

class User_info(models.Model):
	"""en"""
	uname = models.CharField(max_length=20)
	upwd = models.CharField(max_length=40)
	uemail = models.CharField(max_length=30, blank=True)
	ureceive = models.CharField(max_length=50, null=True,)
	uaddress = models.CharField(max_length=100, null=True,)
	upost = models.CharField(max_length=6, blank=True, null=True)
	uphone = models.CharField(max_length=14, null=True,)
	isdelete = models.BooleanField(default=False)
	udate_time = models.DateTimeField(blank=True)
	utest1 = models.CharField(max_length=100, null=True,)
	class Meta():
		db_table = "dailyfresh_table"

	def __str__(self):
		return self.uname.encode('utf-8')