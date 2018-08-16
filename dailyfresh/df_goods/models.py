from django.db import models

# Create your models here.
from tinymce.models import HTMLField

import sys
default_encoding = "utf-8"
if sys.getdefaultencoding() != default_encoding:
	reload(sys)
	sys.setdefaultencoding(default_encoding)


class Type_info(models.Model):
	ttitle = models.CharField(max_length=20)
	isdelete = models.BooleanField(default=False)
	def __str__(self):
		return self.ttitle.encode('utf-8')

	class Meta():
		db_table = "dailyfresh_type"

class Goods_info(models.Model):
	gtitle = models.CharField(max_length=20)
	gpic = models.ImageField(upload_to='df_goods')
	gprice = models.DecimalField(max_digits=5, decimal_places=2)
	isdelete = models.BooleanField(default=False)
	gunit = models.CharField(max_length=10,default='500g',null=True)
	gclick_num = models.IntegerField(null=True)
	gdesc = models.CharField(max_length=200, null=True)
	gstorge = models.IntegerField(null=True)
	gcontent = HTMLField(null=True)
	gcreate_date = models.DateTimeField(auto_now_add=True)
	gmodify_date = models.DateTimeField(auto_now=True)
	gtype = models.ForeignKey('Type_info')
	def __str__(self):
		return self.gtitle.encode('utf-8')
	class Meta():
		db_table = "dailyfresh_goods"
