from django.contrib import admin

# Register your models here.

from models import *

class Type_infoAdmin(admin.ModelAdmin):
	list_display = ['id', 'ttitle',]

class Goods_infoAdmin(admin.ModelAdmin):
	list_display = ['id', 'gtitle', 'gprice', 'gunit', 'gclick_num','gstorge', 'gcreate_date', 'gmodify_date', 'gtype']
	list_per_page = 20

admin.site.register(Type_info, Type_infoAdmin)
admin.site.register(Goods_info, Goods_infoAdmin)
