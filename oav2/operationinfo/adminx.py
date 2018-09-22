from django.contrib import admin
import xadmin
from .models import *


# Register your models here.

#1显示供应商
class SupplierAdmin(object):
    list_display = ('supplier_name', )
    exclude = ('isdelete', )  # 排除显示isdelede字段出来

xadmin.site.register(SupplierTable, SupplierAdmin)

#2显示联系人
class ContactsAdmin(object):
    list_display = ('area', 'supplier_name', 'contact_full_name', 'fixed_telephone', 'phone_number')
    exclude = ('isdelete',)  # 排除显示isdelede字段出来

xadmin.site.register(ContactsTable, ContactsAdmin)


#3注册光纤网络表
class FiberAndNetworkAdmin(object):
    list_display = ('area', 'company', 'supplier', 'fiber_number', 'accounts', 'password', 'ip_addr',  )
    exclude = ('isdelete', 'bak1', 'bak2', 'bak3', 'bak4')  # 排除显示isdelede/bak1/bak2/bak3/bak4字段出来

xadmin.site.register(FiberAndNetworkTable, FiberAndNetworkAdmin)


#4注册软件资源库
class SoftResourceLibraryAdmin(object):
    list_display = ('area','company','department','category','edition',)
    exclude = ('isdelete', 'bak1', 'bak2', 'bak3', 'bak4')  # 排除显示isdelede/bak1/bak2/bak3/bak4字段出来


xadmin.site.register(SoftResourceLibraryTable, SoftResourceLibraryAdmin)