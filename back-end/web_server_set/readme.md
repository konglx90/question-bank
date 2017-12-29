###nginx与uwsgi配置文件的模板及fabric自动部署服务器脚本
#### $代表applcation的名字 @代表wsgi.py是在目录
#### 请自己手动修改config.py里的数据, 及fabfile_set.py 里的env.hosts, env.password
#### 请自行维护好requirements.txt
1. $_nginx.conf
2. $_uwsgi.ini
3. fabric_set.py 部署脚本
4. fabric_update 更新代码脚本
###Usage:

1. 部署服务器fab -f fabfile_set.py update
2. 更新代码 fab -f fabfile_update.py update

####pip freeze > requirements.txt
####pip install -r requirements.txt
