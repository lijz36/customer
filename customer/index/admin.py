from django.contrib import admin
from .models import *


# 定义用户后台管理类
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_phone','user_gender', 'user_avatar','user_createdat', 'user_active']
    date_hierarchy = 'user_createdat'
    list_filter = ['user_name', 'user_createdat']


class TitleAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo']


class TypesAdmin(admin.ModelAdmin):
    list_display = ['type_name']


class SecTypesAdmin(admin.ModelAdmin):
    list_display = ['sectype_name', 'types']


# 注册后台管理模块
admin.site.register(Title,TitleAdmin)
admin.site.register(Users, UserAdmin)

admin.site.register(Types,TypesAdmin)
admin.site.register(SecTypes,SecTypesAdmin)
