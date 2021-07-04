from django.contrib import admin
from rest_framework.authtoken.admin import User

from.models import (Category, Product)



admin.site.register(Category)
admin.site.register(Product)