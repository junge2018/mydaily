# coding=utf-8
from django.shortcuts import render, redirect

# Create your views here.

from models import *
from df_user.models import *
from df_goods.models import *
from django.http import JsonResponse
from df_user import user_decorator

@user_decorator.login
def cart(request):
	uid = request.session['user_id']
	carts = Cart_info.objects.filter(user_id=uid)
	context = {'carts':carts, }
	return render(request, 'df_cart/cart.html', context)

@user_decorator.login
def add(request, gid, count):
	uid = request.session['user_id']
	gid = int(gid)
	count = int(count)

	carts = Cart_info.objects.filter(user_id=uid, goods_id=gid)
	if len(carts)>=1:
		cart = carts[0]
		cart.count += count
	else:
		cart = Cart_info()
		cart.user_id = uid
		cart.goods_id = gid
		cart.count = count
	cart.save()

	# 如果是ajax请求则返回json，否则重定向
	if request.is_ajax():
		count_type = Cart_info.objects.filter(user_id=uid).count()
		return JsonResponse({'count_type':count_type})
	else:
		return redirect('/cart/')

@user_decorator.login
def edit(request,cart_id, count):
	try:
		cart = Cart_info.objects.get(pk=int(cart_id))
		count_tem = cart.count = int(count)
		cart.save()
		data = {'ok':0}
	except Exception as e:
		data = {'ok':count_tem}
	return JsonResponse(data)


@user_decorator.login
def delete(request, cart_id):
	try:
		cart = Cart_info.objects.get(pk=int(cart_id))
		cart.delete()
		data = {'ok':1}
	except Exception as e:
		data = {'ok':0}
	return JsonResponse(data)


