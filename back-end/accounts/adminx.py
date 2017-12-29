# -*- coding:utf-8 -*-
from xadmin import views
import xadmin

xadmin.autodiscover()


class GlobalSetting(object):
    site_title = u'电子科技大学 电力系统题库'
    site_footer = u'电子科技大学能源学院'
    apps_label_title = {
        'car_manage': u'题库管理',
        'auth': u'账户',
    }


xadmin.site.register(views.CommAdminView, GlobalSetting)
