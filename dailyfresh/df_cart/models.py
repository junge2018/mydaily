from django.db import models

# Create your models here.

from df_user.models import *
from df_goods.models import *

import sys
default_encoding = "utf-8"
if sys.getdefaultencoding() != default_encoding:
	reload(sys)
	sys.setdefaultencoding(default_encoding)

class Cart_info(models.Model):
	user = models.ForeignKey('df_user.User_info')
	goods = models.ForeignKey('df_goods.Goods_info')
	count = models.IntegerField()
