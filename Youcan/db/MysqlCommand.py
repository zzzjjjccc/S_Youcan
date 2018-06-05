#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
from Youcan.models import *

'''
@author: jichang
@date: 2018/1/24
@email: 2218982471@qq.com
@describ: Manage data for all project
'''

class MysqlCommand(object):

	# This Class be used to manage Mysql data for youcan

	def __init__(self):
		pass

	def add_user(self, phone, password):

		# Use this method to add user for youcan, return success if add success, otherwise return message of error

		if not self.is_exist_phone(phone):
			user = User()
			user.phone = phone
			user.password = password
			user.save()
			return 'success'
		else:
			return 'Register fail, phone number you given have be registered'
		

	def is_exist_phone(self, phone):

		# if the phone number already exists. phone already exists, return True, otherwise return False

		try:
			user = User.objects.get(phone = phone)
			print(user)
			if user != None:
				print(user.phone)
				return True
			else:
				return False
		except:
			return False

	def verify_password(self, phone, password):

		# if password is right return True, otherwise return False
		
		try: 
			user = User.objects.get(phone = phone)
			print('Phone : ' + phone, 'Password : ' + password)
			if user != None:
				if user.password == password:
					return True
				else:
					print("verify_password user.password != password")
					return False
			else:
				print("verify_password user == None")
				return False
		except:
			print("verify_password except")
			return False


	def login_verification(self, phone, password):

		# if the phone number already exists, and password is right return success, otherwise return message of error
		
		if self.is_exist_phone(phone):
			if self.verify_password(phone, password):
				return "success"
			else:
				return "Password is wrong"
		else:
			return "Phone number not be registered"

	def get_users(self):

		# Get user info, return a string with '_'
		
		try:
			users = User.objects.all()
			result = ''
			for user in users:
				result += user.phone
				result += '_'
				result += user.school
				result += '_'
				result += user.major
				result += '_'
				result += user.name
				result += '_'
				result += user.sex
				result += '|'
			return result
		except:
			return "Get user's information failed"


	def get_user(self, phone):

		# Get an user detail information
		
		try:
			user = User.objects.get(phone = phone)
			if user != None:
				result = []
				result.append(user.school)
				result.append(user.major)
				result.append(user.name)
				result.append(user.sex)
				print('_'.join(result))
				return '_'.join(result)
			else:
				return "User number you given not be registered"
		except:
			return "Server connect failed"
		

	def add_user_detail(self, phone, school="", major="", name="", sex=""):

		# Add user detail
		
		try:
			user = User.objects.get(phone = phone)
			user.school = school
			user.major = major
			user.name = name
			user.sex = sex
			user.save()
			return "success"
		except:
			return "Server connect failed"


	def add_subscribe(self, phone, idol):

		# Add subscribe information, inlcude table youcan_fan and youcan youcan_diol
		
		print('phone : ' + phone +'diol : ' + idol)
		
		if self.is_exist_phone(idol):
			subscribe = Subscribe()
			subscribe.phone = phone
			subscribe.idol = idol

			fan = Fan()
			fan.phone = idol
			fan.fan = phone

			subscribe.save()
			fan.save()
			return 'success'
		else:
			return 'Subscribe fail, phone number you given not be registered'

	def is_idol(self, phone, idol):

		# Judge if given phone number is your idol
		print("phone : ===========" + phone + "idol: ============" + idol)
		try :
			ido = Subscribe.objects.get(phone=phone, idol=idol)
			if ido != None:
				print("yes")
				return "yes"
			else:
				return "no"
		except:
			print("no")
			return "no"

	def get_idols(self, phone):

		# Get your idols through you gived phone number
		
		print("phone : ===========" + phone)
		try:
			idos = Subscribe.objects.all().filter(phone = phone)
			result = []
			for ido in idos:
				print(ido.idol)
				result.append(ido.idol + '_' + self.get_user(ido.idol))
			return '|'.join(result)
				
		except:
			return "Get user's information failed"

	def get_fans(self, phone):

		# Get your fans through you gived phone number
		
		print("phone : ===========" + phone)
		try:
			fans = Fan.objects.all().filter(phone = phone)
			result = []
			for fa in fans:
				print(fa.fan)
				result.append(fa.fan + '_' + self.get_user(fa.fan))
			return '|'.join(result)
				
		except:
			return "Get user's information failed"

	def add_content(self, phone, date, content):

		# Add a content
		
		print("add_content:phone:" + phone+content)
		result = self.get_a_content(phone, date)
		if result == None or len(result) == 0:
			print("create a content")
			con = Content()
			con.phone = phone
			con.date = date
			con.content = content
			con.save()
		else:
			print("pass")
			pass
		return "success"

	def get_a_content(self, phone, date):

		# Get a content according to phone number and date with name
		print("get_a_content's phone:" + phone)
		try:
			user = User.objects.get(phone = phone)
			con = Content.objects.all().filter(phone = phone, date = date)
			result = ''
			for co in con:
				if co != None:
					result += user.name + '#' + co.date + '#' + co.content
					result += '|'
			print(result)
			return result	
		except:
			print("get_a_content wrong")
			return None

	def share(self, phone, date, open_to):

		# Share a content to other person
		
		ops = open_to.split('_')  # The result of split is phone nubmer
		for op in ops:
			if op != '':
				o = Open()
				o.phone = phone
				o.date = date
				o.open_to = op
				o.save()
			
		return "success"
		
	def discover(self, phone):

		# Get discover for app, query diol's content according to they share
		print(phone)
		try:
			ops = Open.objects.all().filter(open_to = phone)
			result = ''
			for op in ops:
				if op != None:
					result += self.get_a_content(op.phone, op.date)
					result += "|"
			return result
		except:
			return "Get content failed"

