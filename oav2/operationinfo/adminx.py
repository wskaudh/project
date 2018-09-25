from django.contrib import admin
import xadmin
from .models import *
from xadmin.layout import Main, Side, Fieldset, Row, AppendedText#引入xadmin 的fields及fieldset设置模块
from xadmin.views import BaseAdminPlugin, ModelFormAdminView, DetailAdminView, filter_hook
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

# class ContactsInline(xadmin.StackedInline):
#     models = ContactsTable
#     extra = 1



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


#5注册硬件资源库
class HardwareResourceLibratyAdmin(object):
    list_display = ('Fixed_assets_number', 'brand', 'category', 'model')
    exclude = ('isdelete', 'bak1', 'bak2', 'bak3', 'bak4')  # 排除显示isdelede/bak1/bak2/bak3/bak4字段出来


xadmin.site.register(HardwareResourceLibratyTable, HardwareResourceLibratyAdmin)



#test注册
class HeroAdmin(object):
    list_display = ('name', 'gender' , 'hbook' )


xadmin.site.register(Heroinfo, HeroAdmin)


class Heroinline(object):
    model = Heroinfo
    extra = 0


class BookAdmin(object):
    list_display = ('btitle', 'binfo')

    inlines = [Heroinline]



    form_layout = (
        Fieldset("书本",
            Row('btitle', 'binfo')
        ),
    )

xadmin.site.register(Bookinfo, BookAdmin)