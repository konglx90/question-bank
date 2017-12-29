# -*- coding:utf-8 -*-
from django.conf.urls import url, patterns

urlpatterns = patterns('accounts',
                       url(r'^$', 'views.login', name='login'),
                       url(r"^logout", 'views.logout', name='logout'),
                       url(r'^changepass', 'views.change_pwd', name='changepassword')
                       )
