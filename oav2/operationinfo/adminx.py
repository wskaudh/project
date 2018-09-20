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