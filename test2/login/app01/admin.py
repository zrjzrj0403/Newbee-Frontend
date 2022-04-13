from django.contrib import admin
from app01 import models


# Register your models here.

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.User2)
class User2Admin(admin.ModelAdmin):
    list_display = ('user2_name',)
