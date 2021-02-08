from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from saleor.saleor.ccs.models import User

admin.site.register(User, UserAdmin)
