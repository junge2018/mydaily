# coding=utf-8

from django.http import HttpResponseRedirect

# 如果未登录则转到登录页面

def login(func):
	def login_func(request, *args, **kwargs):
		if request.session.has_key('user_id'):
			return func(request, *args, **kwargs)
		# 如果登录则原样信息返回到下一步函数
		else:
			rend = HttpResponseRedirect('/user/login/')
			rend.set_cookie('url', request.get_full_path())
			return rend

	return login_func

"""
http://127.0.0.1:8000/index/?uname=junge
request.path表示当前路径:/index/
request.get_full_path表示当前完整路径:/index/?uname=junge
"""

