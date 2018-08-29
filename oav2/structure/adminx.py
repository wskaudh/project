from django.contrib import admin
import xadmin
from .models import *

# Register your models here.

class DepartmentAdmin(object):
    list_display = ('ddepartment', 'dcetagory', 'disdelete')
    search_fields = ('ddepartment', 'dcetagory',)
    list_display = ("ddepartment",)

xadmin.site.register(DepartmentTable, DepartmentAdmin)