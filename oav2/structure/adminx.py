#coding=utf-8
from django.contrib import admin
import xadmin
from .models import *
#from xadmin.layout import Main, Side, Fieldset, Row, AppendedText #引入xadmin 的fields及fieldset设置模块


# Register your models here.


#以下是架构体系基础资料---------1

#类别表注册
class CetagoryAdmin(object):
	list_display = ('Ccetagory',)
	exclude = ('isdelete',) #排除显示isdelede字段出来
	#hidden_menu = True
xadmin.site.register(CetagoryTable, CetagoryAdmin)


#区域表注册
class AreaAdmin(object):
	list_display = ('Aarea',)
	exclude = ('isdelete',)

xadmin.site.register(AreaTable, AreaAdmin)

#公司表注册
class CompanyAdmin(object):
	list_display = ('Ccompany',)
	exclude = ('isdelete',)

xadmin.site.register(CompanyTable, CompanyAdmin)



#部门表注册
class DepartmentAdmin(object):
	list_display = ('Ddepartment', 'Dcetagory',)
	search_fields = ('Ddepartment', )
	list_filter = ('Dcetagory',)
	exclude = ('isdelete',) #排除显示isdelede字段出来

xadmin.site.register(DepartmentTable, DepartmentAdmin)

#架构体系表注册
class FrameAdmin(object):
	list_display = ('Farea', 'Fcompany', 'Fdepartment',)
	search_fields = ('Fdepartment',)
	list_filter = ('Fcompany',)
	exclude = ('isdelete',)

xadmin.site.register(FrameTable, FrameAdmin)


#以上是架构体系基础资料---------1