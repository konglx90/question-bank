# /usr/bin/python
# encoding: utf-8
"""
    1.用于在阿里云服务器上自动化部署django应用
    2.基本上是对教程http://www.jianshu.com/p/e6ff4a28ab5a的脚本化
    3.服务器配置            :
                            Ubuntu14.04
    4.确保服务器上已经安装好:
                            git
                            django
                            pip
                            nginx
                            uwsgi及其依赖python-dev
    5.并维护好requirement.txt文件
    6.在本地将uwsgi_params, *_nginx.conf, *_uwsgi.ini准备好, 以及settings.py里的
      STATIC_ROOT = os.path.join(BASE_DIR, "static/")
    7.usage: fab -f fabfile.py update
    8.请手动测试uwsgi是否正常
    9.本地测试django项目是否正常
    10.请手动创建/home/wwwroot/目录
    11.可能需要修改/etc/nginx/nginx.conf里的use root;
"""
import os
from fabric.api import *
from fabric.contrib.console import confirm
from X_nginx_conf import NG
from X_uwsgi_ini import UW
from config import GIT_REMOTE, APPLICATION, APPLICATION_MAIN
from config import HOSTS, PASSWORD

# ssh要用到的参数
env.hosts = HOSTS
env.password = PASSWORD
# 参数end


# def input_application_name():
#     global APPLICATION, GIT_REMOTE, APPLICATION_MAIN
#     APPLICATION = raw_input("请输入应用名(一定要保证能够APPLICATION名是唯一的): ")
#     APPLICATION_MAIN = raw_input("请输入wsgi.py所在目录(一定要保证能够APPLICATION名是唯一的): ")
#     GIT_REMOTE = raw_input("请输入远程仓库地址: ")


@runs_once
@task
def local_task():
    """
    执行本地任务, 在web_server_set目录下进行
    """
    local('echo "starting task..."')
    local('echo "本地主机:"')
    local('uname -s')

    change = False
    print os.path.exists("../%s_nginx.conf" % APPLICATION)
    if not os.path.exists("../%s_nginx.conf" % APPLICATION):
        local('touch ../%s_nginx.conf' % APPLICATION)

        x = open("../%s_nginx.conf" % APPLICATION, "a+")
        x.write(NG.replace("$", APPLICATION).replace("@", APPLICATION_MAIN))
        x.close()
        change = True
    if not os.path.exists("../%s_uwsgi.ini" % APPLICATION):
        local('touch ../%s_uwsgi.ini' % APPLICATION)

        x = open("../%s_uwsgi.ini" % APPLICATION, "a+")
        x.write(UW.replace("$", APPLICATION).replace("@", APPLICATION_MAIN))
        x.close()
        change = True
    if change:
        local("git add ../*")
        local("git commit -am '生成服务器配置文件'")
        local("git push origin master")


@task
def remote_task():
    """
    远程部署任务
    """
    print "remote update..."
    # if not os.path.exists("/home/wwwroot"):
    #     abort("请手动建立目录 /home/wwwroot")
    with cd('/home/wwwroot'):
        """
        进入应用需放位置
        """
        # 远程操作用run
        print APPLICATION, GIT_REMOTE
        run('ls -l')
        # run('su -')
        if os.path.exists("/home/wwwroot/%s/" % APPLICATION):
            with cd("/home/wwwroot/%s" % APPLICATION):
                run("git pull origin master")
        else:
            run('sudo git clone %s' % GIT_REMOTE)
        # 一定要保证能够APPLICATION名是唯一的
        if not confirm("APPLICATION名是唯一的[Y/N]?"):
            abort("安全退出.")
        run('sudo ln -s /home/wwwroot/%s/%s_nginx.conf /etc/nginx/sites-enabled/' % (APPLICATION, APPLICATION))
        with cd('/home/wwwroot/%s/' % APPLICATION):
            # print "安装依赖包..."
            # run("pip install -r ../requirements.txt")
            print "收集静态资源..."
            run("sudo python manage.py collectstatic")
            print "重启nginx服务..."
            run("sudo /etc/init.d/nginx restart")
            print "启动uwsgi..."
            run("sudo uwsgi --ini %s_uwsgi.ini" % APPLICATION)


@task
def update():
    # usage: fab -f fabfile.py update
    # input_application_name()
    # local_task()
    remote_task()
