from django.db import models
from django.db import connection
from django.utils import timezone

# Create your models here.
class AttenderManager(models.Manager):
	def create_attender(self, name_, surname_, organization_, email_, phone_, date_):
		attender = Attender(name = name_, surname = surname_, organization = organization_, email = email_, phone = phone_, date = date_)		
		return attender

	def insert_attender(self, name_, surname_, organization_, email_, phone_):
		cursor = connection.cursor()
		cursor.execute("INSERT INTO ciaia_attender(name, surname, organization, email, phone) VALUES (%s %s %s %s %s)", [name_, surname_, organization_, email_, phone_])
		attender = cursor.fetchall()
		return attender

	def get_attender(self, param_):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM  ciaia_attender WHERE (email = %s OR phone = %s)", [param_, param_] )
		attenders = cursor.fetchall()
		return attenders

	def get_attenders(self):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM  ciaia_attender;")
		attenders = cursor.fetchall()
		return attenders

class Attender(models.Model):
	name = models.CharField(max_length=40)
	surname = models.CharField(max_length=40)
	organization = models.CharField(max_length=50) 
	email = models.CharField(max_length=40)
	phone = models.CharField(max_length=40)
	date = models.DateTimeField(default = timezone.now)
	attenders = AttenderManager()



class CategoryManager(models.Manager):
	def create_category(self, name_, description_):
		category = Category(name = name_, description = description_)		
		return category

	def get_category(self, name_):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM  ciaia_category WHERE name = %s", [name_] )
		category = cursor.fetchall()
		return category

	def get_categories(self):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM  ciaia_category")
		attenders = cursor.fetchall()
		return categories


class Category(models.Model):
	name = models.CharField(max_length=40)
	description = models.TextField()
	categories = CategoryManager()
	
