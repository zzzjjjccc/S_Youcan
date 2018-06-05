from django.conf.urls import url
from django.contrib import admin
from . import views

'''
@author: jichang
@date: 2018/1/24
@email: 2218982471@qq.com
@describ: Manage url for all project
'''

urlpatterns = [
	url(r'^register', views.rigester),
	url(r'^login', views.login),
	url(r'^getUsers', views.get_users),
	url(r'^getUser', views.get_user),
	url(r'^addUserDetail', views.add_user_detail),
	url(r'^addSubscribe', views.add_subscribe),
	url(r'^isIdol', views.is_idol),
	url(r'^getIdols', views.get_idols),
	url(r'^getFans', views.get_fans),
	url(r'^addContent', views.add_content),
	url(r'^share', views.share),
	url(r'^discover', views.discover),
]