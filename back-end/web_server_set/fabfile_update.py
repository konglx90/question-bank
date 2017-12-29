# /usr/bin/python
# encoding: utf-8

from fabric.api import local, cd, run, env
from config import HOSTS, PASSWORD

# ssh要用到的参数
env.hosts = HOSTS
env.password = PASSWORD


def setting_ci():
    local('echo "add and commit settings in local"')
    local('uname -s')


def update_setting_remote():
    print "remote update"
    with cd('/home/wwwroot/bwc_car'):  # cd用于进入某个目录
        run('ls')  # 远程操作用run
        run('git pull')
        # 有数据库字段修改时
        # run('python manage.py makemigrations')
        # run('python manage.py migrate')

        run("ps aux | grep 'bwc_car_uwsgi.ini$'| awk '{print $2}' | xargs kill -9")
        run("uwsgi --ini bwc_car_uwsgi.ini")


def update():
    setting_ci()
    update_setting_remote()

# usage: fab -f fabfile_update.py update
