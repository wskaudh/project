#coding=utf-8
from django.contrib import admin
import xadmin
from .models import *
# Register your models here.

#注册员工信息表
class EmployeeinfoAdmin(object):
    list_display = ('Eemployee_id', 'Ename', 'Eposition', 'Ework_level',)
    exclude = ('isdelete',)
    fieldsets = [
        ('base', {'fields':['Employeein_id', 'Ename']}),
        ('super',{'fields':['Egender', 'Eage']})

    ]



xadmin.site.register(EmployeeinfoTable, EmployeeinfoAdmin)