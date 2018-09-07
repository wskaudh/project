from django.contrib import admin
import xadmin
from .models import *

# Register your models here.

class DepartmentAdmin(object):
    list_display = ('ddepartment', 'dcetagory',)
    search_fields = ('ddepartment', )
    list_filter = ('dcetagory',)
    exclude = ('isdelete',) #排除显示isdelede字段出来

xadmin.site.register(DepartmentTable, DepartmentAdmin)

class CetagoryAdmin(object):
    list_display = ('ccetagory',)
    exclude = ('isdelete',) #排除显示isdelede字段出来

xadmin.site.register(CetagoryTable, CetagoryAdmin)