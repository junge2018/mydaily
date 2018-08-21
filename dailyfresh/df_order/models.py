from django.db import models

# Create your models here.

import sys
default_encoding = "utf-8"
if sys.getdefaultencoding() != default_encoding:
	reload(sys)
	sys.setdefaultencoding(default_encoding)


class Order_info(models.Model):
	oid = models.CharField(max_length=20, primary_key=True)
	user =models.ForeignKey('df_user.User_info')
	ocreat_date =models.DateTimeField(auto_now_add=True)
	omodified_date =models.DateTimeField(auto_now=True)
	ois_pay =models.CharField(max_length=3, null=True,blank=True)
	ototal =models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
	oaddress =models.CharField(max_length=150, null=True,blank=True)
	oback1 = models.CharField(max_length=100, null=True,blank=True)
	class Meta():
		db_table = 'order_info'

	def __str__(self):
		return self.oid


class Order_detail_info(models.Model):
	order = models.ForeignKey('Order_info')
	goods = models.ForeignKey('df_goods.Goods_info')
	price_fina = models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
	count = models.IntegerField(null=True)
	trans_states = models.CharField(max_length=100, null=True,blank=True)

	class Meta():
		db_table = 'order_detail'

	def __str__(self):
		return self.order_id
