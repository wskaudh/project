#coding=utf-8
from django.contrib import admin
import xadmin
from .models import *
from xadmin.layout import Main, Side, Fieldset, Row, AppendedText #引入xadmin 的fields及fieldset设置模块
# Register your models here.

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
        Fieldset('基本信息',
            Row('Eemployee_id', 'Ename' ,'Egender'),
            Row('Eposition', 'Ework_level'),
            Row('Ework_status', 'Estart_date')
        ),
        Fieldset('其它信息',
            Row('Equit_date', 'Eage'),
            Row('Emarita_status', 'Enation','Ehousehold_register')
        ),
    )



xadmin.site.register(EmployeeinfoTable, EmployeeinfoAdmin)