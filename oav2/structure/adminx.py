#coding=utf-8
from django.contrib import admin
import xadmin
from .models import *
from xadmin.layout import Main, Side, Fieldset, Row, AppendedText #引入xadmin 的fields及fieldset设置模块


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
	#exclude = ('isdelete',) #排除显示isdelede字段出来
	# fieldsets = [
	# 	("base info", {'fields': ['Ddepartment']}),
	# 	("Content", {'fields': ['Dcetagory', 'isdelete']})
	# ]  #在xadmin分组还要使用xadmin的分组方法

#xadmin的fields及fieldsets的方法实现
	#以下第一个方法是在form_layout里面再分两边栏Main与Side,如果只要一分栏的话就不要使用Mian与Side参数，例如第二种方法
	# form_layout = (
	# 	Main(
	# 		Fieldset('基础信息',Row('Ddepartment', 'Dcetagory', 'Dcetagory')), #在一行显示两个字段
	# 		# Fieldset('超级信息', 'Dcetagory')
	# 	),
	# 	Side(
	# 		Fieldset('其它', 'Ddepartment'),
	# 	),
	# 	Side(
	# 		Fieldset('其它', 'Ddepartment'),
	# 	)
	# )

#第二种form的方法
	form_layout = (
		Fieldset('基础信息',Row('Ddepartment', 'Dcetagory', 'Dcetagory')), #在一行显示两个字段
		Fieldset('超级信息', 'Dcetagory')
		# Side(
		# 	Fieldset('其它', 'Ddepartment'),
		# ),
		# Side(
		# 	Fieldset('其它', 'Ddepartment'),
		# ), #显示在右边的小栏上
	)



xadmin.site.register(DepartmentTable, DepartmentAdmin)

#架构体系表注册
class FrameAdmin(object):
	list_display = ('Farea', 'Fcompany', 'Fdepartment',)
	search_fields = ('Fdepartment',)
	list_filter = ('Fcompany',)
	exclude = ('isdelete',)

xadmin.site.register(FrameTable, FrameAdmin)


#以上是架构体系基础资料---------1