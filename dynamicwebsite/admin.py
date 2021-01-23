from django.contrib import admin

# Register your models here.
from .models import products,productsadmin,people,peopleadmin
admin.site.register(products,productsadmin)
admin.site.register(people,peopleadmin)