# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from forms import LoginForm
from django.contrib.auth import login as usr_login, logout as usr_logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


@csrf_exempt
def login(request):  # 首页
    redirect_addr = request.GET.get('next', '')
    print redirect_addr, "re"
    if request.user.is_authenticated():
        return render_to_response('car_management/car_index.html', context_instance=RequestContext(request))
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if username == '':
            return JsonResponse({'message': u'用户名不能为空', 'status': 500})
        if password == '':
            return JsonResponse({'message': u'密码不能为空', 'status': 500})
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'message': u'该用户不存在', 'status': 500})
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            usr_login(request, user)
            request.session['_auth_user_id'] = user.id
            user.save()
            if redirect_addr == '':
                return JsonResponse({'message': u'登陆成功', 'status':200, 'redirect': redirect_addr})
                # return render_to_response('car_management/car_index.html', context_instance=RequestContext(request))
            else:
                return JsonResponse({'message': u'登陆成功', 'status':200, 'redirect': redirect_addr})
                # return HttpResponseRedirect(redirect_addr)
        else:
            return JsonResponse({'message': u'密码不正确', 'status': 500})
    else:
        return render_to_response('accounts/login.html', context_instance=RequestContext(request))


@require_GET
def logout(request):  # 登出
    usr_logout(request)
    return HttpResponseRedirect('/')


@csrf_exempt
@login_required
def change_pwd(request):
    if request.method == "POST":
        current_password = request.POST['current_password']
        password = request.POST['password']
        conform = request.POST['confirm_password']
        if not request.user.check_password(current_password):
            s = u'初始密码填写错误\n'
            return JsonResponse({'message': s, 'status': 500})
        if password != conform:
            s = u'两次密码不一致请重新输入\n'
            return JsonResponse({'message': s, 'status': 500})
        request.user.set_password(password)
        s = u'修改成功！\n'
        request.user.save()
        return JsonResponse({'message': s, 'status': 200})
    return render_to_response('accounts/change_password.html', context_instance=RequestContext(request))
