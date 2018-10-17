from django.contrib import admin
from .models import Attender
from .models import Category

#user: admin #pass: admin12345

# Register your models here.
admin.site.register(Attender)
admin.site.register(Category)
