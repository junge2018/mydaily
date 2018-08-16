# coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from hashlib import sha1
from models import *
from datetime import *

from . import user_decorator
# import user_decorator

from df_goods.models import *

# Create your views here.

def register(request):
	return render(request, "df_user/register.html")

def register_handle(request):
	post = request.POST
	uname = post.get('user_name')
	upwd = post.get('pwd')
	ucpwd = post.get('cpwd')
	uemail = post.get('email')

	if upwd != ucpwd:
		return redirect('/user/register/')

	s1 =sha1()
	s1.update(upwd)
	upwd_sha1 = s1.hexdigest()

	user = User_info()
	user.uname = uname
	user.upwd = upwd_sha1
	user.uemail = uemail
	user.isdelete = 0
	user.udate_time = datetime.now()
	user.save()

	return redirect('/user/login/')

def register_exist(request):
	uname = request.GET.get('uname')
	count = User_info.objects.filter(uname=uname).count()
	context = {'count': count}
	return JsonResponse(context)

def login(request):
	uname = request.COOKIES.get('uname', '')
	context = {'error_name':0, 'error_pwd':0, 'uname':uname, 'upwd':'',}
	return render(request, 'df_user/login.html', context)

def logout(request):
	request.session.flush()
	return redirect('/')

def login_handle(request):
	post = request.POST
	uname = post.get('username')
	upwd = post.get('pwd')
	ureme_name = post.get('reme_name', 0)

	user = User_info.objects.filter(uname=uname)
	length = len(user)  # [] or [{},]

	if length==1:
		s1 = sha1()
		s1.update(upwd)
		upwd_tem = s1.hexdigest()

		if user[0].upwd == upwd_tem:
			url = request.COOKIES.get('url', '/')
			rend = HttpResponseRedirect(url)
			# 记住用户名
			if ureme_name != 0:
				rend.set_cookie('uname', uname)
			else:
				rend.set_cookie('uname', '', max_age=-1) 
				#cookie值为空，-1是立即过期

			request.session['user_id'] = user[0].id
			request.session['user_name'] = user[0].uname
			#将用户id和用户名存在session数据表中,默认两周后过期删除

			return rend
		else:
			context = {'error_name':0, 'error_pwd':1, 'uname':uname, 'upwd':upwd, }
			return render(request, 'df_user/login.html', context)
	else:
		context = {'error_name':1, 'error_pwd':0, 'uname':uname, 'upwd':upwd, }
		return render(request, 'df_user/login.html', context)

@user_decorator.login
def info(request):
	user = User_info.objects.get(id=request.session['user_id'],)
	#最近浏览产品
	goods_ids = request.COOKIES.get('goods_ids', '')
	if goods_ids != '':
		goods_ids_tem = goods_ids.split(',')
		goods_list = []
		# Goods_info.objects.filter(id__in=goods_ids_tem) 
		# 字段查询，选出在列表中id的对象集
		for gid in goods_ids_tem:
			goods_list.append(Goods_info.objects.get(id=int(gid)))
	else:
		goods_list = Goods_info.objects.all().order_by('-id')[0:5]

	if user:
		user_email = user.uemail
		user_address = user.uaddress
		context = { 'uname':request.session['user_name'], 
					'uemail':user_email, 
					'uaddress':user_address,
					'goods_list':goods_list, }
		return render(request, 'df_user/user_center_info.html', context)
	else:
		return redirect('/user/login/')

@user_decorator.login
def order(request):
	context = {'uname':request.session['user_name'], 'date_time':datetime.now(), }
	return render(request, 'df_user/user_center_order.html', context)

@user_decorator.login
def site(request):
	user = User_info.objects.get(id=request.session['user_id'])
	if request.method=='POST':
		post = request.POST
		user.ureceive = post.get('ureceive')
		user.uaddress = post.get('uaddress')
		user.upost = post.get('upost')
		user.uphone = post.get('uphone')
		user.save()
	cur_address = str(user.uaddress) +" &nbsp;(" + str(user.ureceive) + ') <收> &nbsp; ' + str(user.uphone)
	context = {'user':user, 'cur_address':cur_address, }
	return render(request, 'df_user/user_center_site.html', context )
