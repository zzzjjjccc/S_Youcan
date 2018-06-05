from django.db import models

# Create your models here.

class User(models.Model):

	# Create User table for youcan

	id_youcan = models.AutoField(primary_key=True,)
	phone = models.CharField(max_length=11, unique=True, null=False,)
	password = models.CharField(max_length=30, null=False,)
	school = models.CharField(max_length=80,)
	major = models.CharField(max_length=80,)
	name = models.CharField(max_length=80,)
	sex = models.CharField(max_length=5,)

class Open(models.Model):

	# Create Open table for youcan

	id_youcan = models.AutoField(primary_key=True,)
	phone = models.CharField(max_length=11, null=False,)
	date = models.CharField(max_length=30, null=False,)
	open_to = models.CharField(max_length=11, null=False,)


class Content(models.Model):

	# Create Content table for youcan

	id_youcan = models.AutoField(primary_key=True,)
	phone = models.CharField(max_length=11, null=False,)
	date = models.CharField(max_length=30, null=False,)
	content = models.TextField(null=False,)


class Fan(models.Model):

	# Create Fans table for youcan

	id_youcan = models.AutoField(primary_key=True,)
	phone = models.CharField(max_length=11, null=False,)
	fan = models.CharField(max_length=11, null=False,)

class Subscribe(models.Model):

	# Create Idols table for youcan

	id_youcan = models.AutoField(primary_key=True,)
	phone = models.CharField(max_length=11, null=False,)
	idol = models.CharField(max_length=11, null=False,)
