# coding=utf-8
from django.shortcuts import render, redirect

# Create your views here.

# from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from models import *
from django.core.paginator import Paginator, Page

def index(request):
	# 查询最新的最热的4条商品信息，倒序查询
	typelist = Type_info.objects.all()
	type0 = typelist[0].goods_info_set.order_by('-id')[0:4]
	type01 = typelist[0].goods_info_set.order_by('-gclick_num')[0:4]
	type1 = typelist[1].goods_info_set.order_by('-id')[0:4]
	type11 = typelist[1].goods_info_set.order_by('-gclick_num')[0:4]
	type2 = typelist[2].goods_info_set.order_by('-id')[0:4]
	type21 = typelist[2].goods_info_set.order_by('-gclick_num')[0:4]
	type3 = typelist[3].goods_info_set.order_by('-id')[0:4]
	type31 = typelist[3].goods_info_set.order_by('-gclick_num')[0:4]
	type4 = typelist[4].goods_info_set.order_by('-id')[0:4]
	type41 = typelist[4].goods_info_set.order_by('-gclick_num')[0:4]
	type5 = typelist[5].goods_info_set.order_by('-id')[0:4]
	type51 = typelist[5].goods_info_set.order_by('-gclick_num')[0:4]
	context = {	'type0':type0, 'type01':type01,
				'type1':type1, 'type11':type11,
				'type2':type2, 'type21':type21,
				'type3':type3, 'type31':type31,
				'type4':type4, 'type41':type41,
				'type5':type5, 'type51':type51,}
	return render(request, 'df_goods/index.html', context)


def list(request, tid, pindex, sort):
	typeinfo = Type_info.objects.get(id=int(tid))
	news = typeinfo.goods_info_set.order_by('-id')[0:2]
	if sort == '1':   # 默认排序，最新
		good_list = Goods_info.objects.filter(gtype_id=int(tid)).order_by('-id')
	elif sort == '2':   # 价格排序
		good_list = Goods_info.objects.filter(gtype_id=int(tid)).order_by('gprice')
	elif sort == '3':   # 人气排序，点击量
		good_list = Goods_info.objects.filter(gtype_id=int(tid)).order_by('-gclick_num')
	else:
		return redirect('/list'+tid+'_'+pindex+'_1/')
	paginator_page = Paginator(good_list, 10)
	page = paginator_page.page(int(pindex))
	context = {	'page':page,
				'paginator_page':paginator_page,
				'typeinfo':typeinfo,
				'tid':tid,
				'pindex':pindex,
				'sort':sort,
				'news':news,}
	return render(request, 'df_goods/list.html', context)

def detail(request, id):
	goods = Goods_info.objects.get(id=int(id))
	goods.gclick_num += 1
	goods.save()
	news = goods.gtype.goods_info_set.order_by('-id')[0:2]
	context = {'g':goods, 'news':news, 'id':id, 'title':goods.gtype.ttitle, 'tid':goods.gtype.id}
	response = render(request, 'df_goods/detail.html', context)

	#记录最近浏览的产品，在用户中心使用
	goods_ids = request.COOKIES.get('goods_ids', '')
	goods_id = id
	if goods_ids != "":
		goods_ids_tem = goods_ids.split(',') # 以逗号切割字符串为列表
		if goods_ids_tem.count(goods_id) >= 1:
			goods_ids_tem.remove(goods_id)
		goods_ids_tem.insert(0,goods_id)
		if len(goods_ids_tem) >=6:
			del goods_ids_tem[5]
		goods_ids = ','.join(goods_ids_tem) # 拼接为字符串，便于存储和取值切割
	else:
		goods_ids = goods_id

	response.set_cookie('goods_ids', goods_ids)  #存入detail页面的cookie
	return response



