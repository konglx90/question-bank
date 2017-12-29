# -*-coding:utf-8 -*-
from datetime import datetime, date
from django.db.models import Q


# 防止数据库中出现空的申请列表
def clean_data():
    for obj in list:
        obj.delete()


# 按进校时间生成预约码
def apply_number(date):
    a += 1
    if a <= 9:
        num = '000' + str(a)
    elif a > 9 and a <= 99:
        num = '00' + str(a)
    elif a > 99 and a <= 999:
        num = '0' + str(a)
    else:
        num = str(a)
    return num

# 200成功
# 500失败

# 处理分页
def handle_page(request, object, onepage=10):
    nowpage = request.GET.get('nowpage', 1)
    allpage = request.GET.get('allpage', 1)
    type = request.GET.get('type', '')

    # 第一次进入本页面时，判断总页数
    if allpage == 1 and nowpage == 1:
        sum = object.objects.filter(Q(in_time__startswith=date.today())).count()
        allpage = sum / onepage + (sum % onepage > 0)

    if type == 'up':
        nowpage -= 1
    elif type == 'down':
        nowpage += 1
    start = (nowpage - 1) * onepage
    end = start + onepage
    list = object.objects.filter(Q(in_time__startswith=date.today()))[start:end]

    return {'lists': list, 'allpage': allpage, 'nowpage': nowpage}
