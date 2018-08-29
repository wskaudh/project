from django.contrib import admin
import xadmin
from .models import *
# Register your models here.
from xadmin import views



class GlobalSettings(object):
	site_title = "運維信息管理系統"
	site_footer = 'wskaudh'
	menu_style = "accordion"  #选项卡折叠效果


xadmin.site.register(views.CommAdminView, GlobalSettings)