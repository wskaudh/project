#coding=utf-8
from django.contrib import admin
import xadmin
from .models import *
from xadmin.layout import Main, Side, Fieldset, Row, AppendedText #引入xadmin 的fields及fieldset设置模块
# Register your models here.


#以下是架构体系基础资料---------1

#类别表注册
class CategoryAdmin(object):
	list_display = ('category',)
	exclude = ('isdelete',) #排除显示isdelede字段出来
	#hidden_menu = True
xadmin.site.register(CategoryTable, CategoryAdmin)


#区域表注册
class AreaAdmin(object):
	list_display = ('area',)
	exclude = ('isdelete',)

xadmin.site.register(AreaTable, AreaAdmin)

#公司表注册
class CompanyAdmin(object):
	list_display = ('company',)
	exclude = ('isdelete',)

xadmin.site.register(CompanyTable, CompanyAdmin)



#部门表注册
class DepartmentAdmin(object):
	list_display = ('department', 'category',)
	search_fields = ('department', )
	list_filter = ('category',)
	exclude = ('isdelete',) #排除显示isdelede字段出来

xadmin.site.register(DepartmentTable, DepartmentAdmin)

#以上是架构体系基础资料---------1



#注册职位表
class PositionAdmin(object):
	list_display = ('position',)
	exclude = ('isdelete',)

xadmin.site.register(PositionTable, PositionAdmin)

#注册工作级别表
class WorkLevelAdmin(object):
	list_display = ('work_level',)
	exclude = ('isdelete',)

xadmin.site.register(WorkLevelTable, WorkLevelAdmin)


#注册员工信息表
class EmployeeinfoAdmin(object):
	list_display = ('employee_id', 'name', 'position', 'work_level',)
	exclude = ('isdelete',)

	form_layout =(
		Fieldset('隶属部门',
			Row('area', 'company'),
			Row('department', 'category')

		),
		Fieldset('基本信息',
			Row('employee_id', 'name' ,'gender'),
			Row('position', 'work_level'),
			Row('work_status', 'start_date')
		),
		Fieldset('普通信息',
			Row('quit_date', 'age'),
			Row('marita_status', 'nation','household_register'),
			Row('tel', 'emergency_contact_person', 'emergency_contact_number')
		),
		Fieldset('学历及其它',
			Row('education', 'graduate_school'),
			Row('graduation_date', 'start_work_date'),
			Row('remarks')
		),
	)



xadmin.site.register(EmployeeinfoTable, EmployeeinfoAdmin)