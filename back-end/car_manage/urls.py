# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('car_manage',
                       url(r'^$', 'views.car_index', name='car_index'),  # 首页
                       url(r'^dapi/question$', 'views.question_list', name='question_list'),
                       url(r'^dapi/paper$', 'views.paper_list', name='paper_list'),
                       url(r'^dapi/create_questions', 'views.create_questions', name='create_questions'),
                       url(r'^dapi/create_paper', 'views.create_paper', name='create_paper'),
                       url(r'^dapi/get_one_paper', 'views.get_one_paper', name='get_one_paper')
                       )
