# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

import os


class LoginForm(forms.Form):  # 登陆表单
    account = forms.CharField(max_length=100, error_messages={'required': u'请填写你的用户名！'},
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'账号'}))
    password = forms.CharField(max_length=20, error_messages={'required': u'请填写你的密码！'},
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': u'密码'}))

    def clean_username(self):
        account = self.cleaned_data['account']
        try:
            User.objects.get(username=account)
        except User.DoesNotExist, e:
            print e
            raise forms.ValidationError(u'该账号并不存在！')
        return account

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password

