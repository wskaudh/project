#coding=utf-8
from django.contrib import admin
import xadmin
from .models import *
# Register your models here.
from xadmin import views



class GlobalSettings(object):
	site_title = "運維信息管理系統"
	site_footer = 'wskaudh'
	menu_style = "accordion"  #选项卡折叠效果

# #自定菜单，目前只能做到二层菜单，三层菜单还暂时不知道是否可以实现
# 	def get_site_menu(self):
# 		return (
# 			{
# 				'title': '基础资料0',
# 				'menus': [
# 					{'title': '架构体系1', 'url': self.get_model_url(FrameTable, 'changelist'), 'menus': [{'title': 'wskaudh'}],
# #							#'url'是指明了链接到哪个模型类去
# 					 },
# # 			],
# 			},
# 		)

xadmin.site.register(views.CommAdminView, GlobalSettings)


