from django.shortcuts import render
from django.http import HttpResponse
from Youcan.db import MysqlCommand

'''
@author: jichang
@date: 2018/1/24
@email: 2218982471@qq.com
@describ: Manage data for all project
'''

# Create your views here.

manager = MysqlCommand.MysqlCommand()

def rigester(request):

	# Use this method to rigester user for youcan

	phone = request.POST['phone']
	password = request.POST['password']

	if phone != None and password != None:
		print('Phone : ' + phone, 'Password : ' + password)
		result = manager.add_user(phone, password)
		return HttpResponse(result)
	else :
		return HttpResponse(result)

def login(request):

	# Use this method to verify user if have registered and password right, if True return "success", otherwise return "fail"
	
	phone = request.POST['phone']
	password = request.POST['password']
	if phone != None and password != None:
		print('Phone : ' + phone, 'Password : ' + password)
		result = manager.login_verification(phone, password)
		return HttpResponse(result)
	else :
		return HttpResponse("Somthing wrong")

def get_users(request):

	# Use this method to get users for app, all users
	
	result = manager.get_users();
	print(result)
	return HttpResponse(result)

def add_user_detail(request):

	# Add detail information of user to user table

	phone = request.POST['phone']
	school = request.POST['school']
	major = request.POST['major']
	name = request.POST['name']
	sex = request.POST['sex']
	if phone != None:
		result = manager.add_user_detail(phone, school, major, name, sex)
		return HttpResponse(result)

def get_user(request):

	# Get detail information of user, example school, major, name, sex

	phone = request.POST['phone']
	if phone != None:
		result = manager.get_user(phone)
		return HttpResponse(result)

def add_subscribe(request):

	# Add subscribe information, inlcude table youcan_fan and youcan youcan_diol
	
	phone = request.POST['phone']
	idol = request.POST['idol']
	if phone != None and idol != None:
		result = manager.add_subscribe(phone, idol)
		return HttpResponse(result)


def is_idol(request):

	# Judge if given phone number is your idol

	phone = request.POST['phone']
	idol = request.POST['idol']
	if phone != None:
		result = manager.is_idol(phone, idol)
		return HttpResponse(result)

def get_idols(request):

	# Get your idols through you gived phone number
	
	phone = request.POST['phone']
	if phone != None:
		result = manager.get_idols(phone)
		return HttpResponse(result)

def get_fans(request):

	# Get your fans through you gived phone number
	
	phone = request.POST['phone']
	if phone != None:
		result = manager.get_fans(phone)
		return HttpResponse(result)

def add_content(request):

	# Add a content
	
	phone = request.POST['phone']
	date = request.POST['date']
	content = request.POST['content']

	print("add_content")
	print(phone)
	print(date)
	print(content)

	empty = phone == None or date == None or content == None
	if not empty:
		print("add_content run")
		result = manager.add_content(phone, date, content)
		return HttpResponse(result)

def share(request):

	# Share a content to other person
	
	phone = request.POST['phone']
	date = request.POST['date']
	open_to = request.POST['open']

	empty = phone == None or date == None or open_to == None
	if not empty:
		result = manager.share(phone, date, open_to)
		return HttpResponse(result)

def discover(request):

	# Get discover for app, query diol's content according to they share
	
	phone = request.POST['phone']

	empty = phone == None
	if not empty:
		result = manager.discover(phone)
		return HttpResponse(result)
	
