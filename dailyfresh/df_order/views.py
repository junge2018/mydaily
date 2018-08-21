#coding=utf-8
from django.shortcuts import render, redirect

# Create your views here.

from df_user import user_decorator
from df_user.models import *
from df_goods.models import *
from df_cart.models import *
from models import *
from django.db import transaction  #引入事务
from datetime import *
from decimal import Decimal

"""
事务：一旦操作失败或者中途放弃则全部回退
1.创建订单对象
2.判断商品库存
3.创建详单对象
4.修改商品库存
5.删除购物车
"""
@user_decorator.login
def order(request):
	#查询用户
	user = User_info.objects.get(id=request.session['user_id'])
	#根据用户查询购物车
	get = request.GET
	cart_ids = get.getlist('cart_id', [])
	if len(cart_ids)==0:
		return redirect('/cart/?goods_no=未选中任何商品');
	cart_ids_tem = [int(item) for item in cart_ids]
	carts = Cart_info.objects.filter(id__in=cart_ids_tem)
	cur_address = user.uaddress + ' &nbsp;(' + user.ureceive + ') <收> &nbsp; ' + user.uphone

	context = {'cur_address':cur_address,
				'user':user,
				'carts':carts,
				'cart_ids':','.join(cart_ids)}
	return render(request, 'df_order/place_order.html', context)


@transaction.atomic()  #事务判断处理
@user_decorator.login
def order_handle(request):
	# 创建一个事务原始点
	trans_id = transaction.savepoint()
	post = request.POST
	# 接收购物车编号
	cart_ids = post.get('cart_ids') #'5,6,8'以逗号分割的字符串
	try:
		# 创建订单对象
		order = Order_info()
		uid = request.session['user_id']
		now = datetime.now()
		order.oid = '%s%d'%(now.strftime('%Y%m%d%H%M%S'),uid)
		order.user_id = uid
		order.ois_pay = '0'
		order.ototal = Decimal(post.get('total'))
		order.oaddress = post.get('address')
		order.save()
		# 创建详单对象
		cart_ids_tem = [int(item) for item in cart_ids.split(',')]
		for cart_num in cart_ids_tem:
			detail = Order_detail_info()
			detail.order_id = order.oid
			# 查询购物车信息
			cart = Cart_info.objects.get(id=cart_num)
			# 判断商品库存
			good = cart.goods
			if good.gstorge >= cart.count:
				# 库存大于商品购买量，减少库存量
				good.gstorge -= cart.count
				good.save()
				# 完善详单信息
				detail.goods_id = good.id
				detail.price_fina = good.gprice
				detail.count = cart.count
				detail.trans_states = '已提交,未付款'
				detail.save()
				# 购买后删除购物车
				cart.delete()
			else:   # 如果库存小于购买量
				transaction.savepoint_rollback(trans_id)
				return redirect('/cart/')
		transaction.savepoint_commit(trans_id)

	except Exception as e:
		print '====================%s'%e
		transaction.savepoint_rollback(trans_id)

	return redirect('/order/pay_handle/?oid='+order.oid)

def pay_handle(request):
	oid = request.GET.get('oid')
	context = {'oid':oid}
	return render(request, 'df_order/pay_handle.html', context)

def pay(request, oid):
	order_pay = Order_info.objects.get(oid=oid)
	order_pay.ois_pay = '1' #'0'未付款,'1'已付款
	order_pay.save()

	order_detail = Order_detail_info.objects.filter(order_id=oid)
	order_count = order_detail.count()
	for detail_tem in order_detail:
		detail_tem.trans_states = '已付款'
		detail_tem.save()
	context = {'order_pay':order_pay, 'order_count':order_count}
	return render(request, 'df_order/pay.html', context)