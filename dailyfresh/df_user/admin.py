from django.contrib import admin

# Register your models here.

from models import *

class User_infoAdmin(admin.ModelAdmin):
	list_display = ['id', 'uname', 'uemail', 'ureceive', 'uaddress', 'uphone', 'udate_time']
	list_per_page = 20

admin.site.register(User_info, User_infoAdmin)
