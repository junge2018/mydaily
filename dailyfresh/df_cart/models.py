from django.db import models

# Create your models here.

# from df_user.models import *
# from df_goods.models import *

class Cart_info(models.Model):
	user = models.ForeignKey('df_user.User_info')
	goods = models.ForeignKey('df_goods.Goods_info')
	count = models.IntegerField()
