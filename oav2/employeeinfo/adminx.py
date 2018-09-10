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
	exclude = ('isdelete',) #排除显示isdelede字段出来

xadmin.site.register(DepartmentTable, DepartmentAdmin)

#以上是架构体系基础资料---------1




#注册职位表
class PositionAdmin(object):
    list_display = ('pposition',)
    exclude = ('isdelete',)

xadmin.site.register(PositionTable, PositionAdmin)

#注册工作级别表
class WorkLevelAdmin(object):
    list_display = ('wwork_level',)
    exclude = ('isdelete',)

xadmin.site.register(WorkLevelTable, WorkLevelAdmin)


#注册员工信息表
class EmployeeinfoAdmin(object):
    list_display = ('Eemployee_id', 'Ename', 'Eposition', 'Ework_level',)
    exclude = ('isdelete',)

    form_layout =(
        Fieldset('隶属部门',
            Row('Earea', 'Ecompany'),
            Row('Edepartment', 'Ecetagory')

        ),
        Fieldset('基本信息',
            Row('Eemployee_id', 'Ename' ,'Egender'),
            Row('Eposition', 'Ework_level'),
            Row('Ework_status', 'Estart_date')
        ),
        Fieldset('普通信息',
            Row('Equit_date', 'Eage'),
            Row('Emarita_status', 'Enation','Ehousehold_register'),
            Row('Etel', 'Eemergency_contact_person', 'Eemergency_contact_number')
        ),
        Fieldset('学历及其它',
            Row('Eeducation', 'Egraduate_school'),
            Row('Egraduation_date', 'Estart_work_date'),
            Row('Eremarks')
        ),
    )



xadmin.site.register(EmployeeinfoTable, EmployeeinfoAdmin)