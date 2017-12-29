# -*-coding:utf-8 -*-
from django.http.response import HttpResponse, JsonResponse
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime, date, timedelta

import json
from bson import json_util
from car_manage.models import Question, Option, Paper
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from random import randint, choice
from car_manage.ga_me import output

# 预约车辆首页
@login_required
def car_index(request):
    return render_to_response('car_management/car_index.html',
                            context_instance=RequestContext(request))


def question_list(request):
    page = request.GET.get('page')  # 获取页码

    limit = 10  # 每页10道题
    questions = Question.objects.all()
    total = len(questions)
    paginator = Paginator(questions, limit)  # 实例化一个分页对象

    cur_page = 1

    try:
        questions = paginator.page(page)  # 获取某页对应的记录
        cur_page = page
    except PageNotAnInteger:  # 如果页码不是个整数
        questions = paginator.page(1)  # 取第一页的记录
        cur_page = 1
    except EmptyPage:  # 如果页码太大，没有相应的记录
        questions = paginator.page(paginator.num_pages)  # 取最后一页的记录
        cur_page = paginator.num_pages

    data = []

    for question in questions:
        options = [option.toDict() for option in question.option.all()]
        ex_q = question.toDict()
        ex_q.update({'options': options})
        data.append(ex_q)

    data = json.dumps({
        'data': data,
        'num_pages': paginator.num_pages,
        'total': total,
        'cur_page': cur_page

    }, default=json_util.default)
    return HttpResponse(data)

def create_questions(request):
    return HttpResponse(False)
    for i in range(500):
        id = i

        # 试题难度取0.3 到 1 之间随机值
        difficulty = randint(3, 10) * 0.1

        # 单选题3分
        if i < 101:
            topic = u'中性点经消弧线圈接地系统中一般采用'+unicode(i)
            _type = 1
            score = 3
            ques = Question.objects.create(
                topic=topic,
                difficulty=difficulty,
                score=score,
                _type=_type
            )
            option = Option.objects.create(
                question=ques,
                topic=u'欠补偿形式',
                is_right=True,
            )
            option = Option.objects.create(
                question=ques,
                topic=u'过补偿形式',
                is_right=False,
            )

        # 多选题5分
        if 100 < i < 201:
            topic = u'在标么制中，只需选定两个基准，常选的是' + unicode(i)
            _type = 2
            score = 5
            ques = Question.objects.create(
                topic=topic,
                difficulty=difficulty,
                score=score,
                _type=_type
            )
            option = Option.objects.create(
                question=ques,
                topic=u'电压、电流',
                is_right=True,
            )
            option = Option.objects.create(
                question=ques,
                topic=u'电压、功率',
                is_right=True,
            )

        # 判断题4分
        if 200 < i < 301:
            topic = u'电力系统的综合用电负荷加上网络中的供电损耗称为供电负荷' + unicode(i)
            _type = 3
            score = 4
            ques = Question.objects.create(
                topic=topic,
                difficulty=difficulty,
                score=score,
                _type=_type,
                is_right=True
            )

        # 填空题1-4分
        if 300 < i < 401:
            topic = '电力网某条线路额定电压为UN=110KV，则它表示的是' + unicode(i)
            _type = 4
            score = randint(1, 5)
            ques = Question.objects.create(
                topic=topic,
                difficulty=difficulty,
                score=score,
                _type=_type,
                answer=u'线电压'
            )

        # 问答题分数为难度系数*10
        if 400 < i < 501:
            topic = '电力网络是指在电力系统中由变压器、电力线路等变换、输送、分配电能设备所组成的部分' + unicode(i)
            _type = 5
            ques = Question.objects.create(
                topic=topic,
                difficulty=difficulty,
                score=score,
                _type=_type,
                answer=u'电力网络是指在电力系统中由变压器、电力线路等变换、输送、分配电能设备所组成的部分'
            )

        # 每题1到4个知识点
        points = []
        count = randint(1, 5)
        for j in range(count):
            points.append(randint(1, 100))
        print ("xxxxxxxxxxxxxxxx")
        ques.set_points(points)
        ques.save()

    return HttpResponse(count)


def create_paper(request):

    total_score = int(request.GET.get('total_score', 100))
    difficulty = float(request.GET.get('difficulty', 0.72))

    each_type_count=[10, 4, 5, 5, 2]

    data = output(total_score, difficulty)

    print total_score, difficulty

    if data is False:
        return HttpResponse(0)

    q = Question.objects.all()
    p = Paper.objects.create(
        title=u'电力系统分析(2017-2018)' + str(randint(0, 999)),
        difficulty=data[2][-2],
        sum_score=total_score,
        adaptation_degree=data[2][-1],
        p_coverage=data[2][-3]
    )

    x = []
    for i in range(2):
        x.append(choice(q[:101]).pk)
    for i in range(5):
        x.append(choice(q[101:201]).pk)
    for i in range(5):
        x.append(choice(q[201:301]).pk)
    for i in range(4):
        x.append(choice(q[301:401]).pk)
    for i in range(10):
        x.append(choice(q[401:501]).pk)

    p.set_question_list(x)
    p.save()

    return HttpResponse(json.dumps({
        'data': data,
        'paper': {
            'title': p.title,
            'sum_score': p.sum_score,
            'difficulty': p.difficulty,
            'question_count': 26,
            'id': p.pk
        }
    }))

def paper_list(request):
    page = request.GET.get('page')  # 获取页码

    limit = 10  # 每页10道题
    papers = Paper.objects.all()
    total = len(papers)
    paginator = Paginator(papers, limit)  # 实例化一个分页对象

    cur_page = 1

    try:
        papers = paginator.page(page)  # 获取某页对应的记录
        cur_page = page
    except PageNotAnInteger:  # 如果页码不是个整数
        papers = paginator.page(1)  # 取第一页的记录
        cur_page = 1
    except EmptyPage:  # 如果页码太大，没有相应的记录
        papers = paginator.page(paginator.num_pages)  # 取最后一页的记录
        cur_page = paginator.num_pages

    data = []

    for paper in papers:
        ex_q = paper.toDict()
        data.append(ex_q)

    data = json.dumps({
        'data': data,
        'num_pages': paginator.num_pages,
        'total': total,
        'cur_page': cur_page

    }, default=json_util.default)
    return HttpResponse(data)

def get_one_paper(request):
    # question_pks = request.GET.get('questions')
    paper_id = int(request.GET.get('id'))
    # pk_list = json.loads(question_pks)
    pk_list = Paper.objects.get(pk=paper_id).get_question_list()
    print pk_list

    data = []
    for pk in pk_list:
        q = Question.objects.get(pk=pk)
        ex_q = q.toDict()
        if q._type == 1 or q._type == 2:
            options = [option.toDict() for option in q.option.all()]
            ex_q.update({'options': options})
        data.append(ex_q)

    data = json.dumps({
        'data': data,
    }, default=json_util.default)
    return HttpResponse(data)
