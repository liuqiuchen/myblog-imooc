启动服务

`python manage.py runserver`

访问localhost:9999，默认是localhost:8000

`python manage.py runserver 9999`

创建应用

`python manage.py startapp blog`

添加应用名到`settings.py`中的`INSTALLED_APPS`里

Django中不同App下Templates目录中的同名.html文件会造成冲突

###解决Templates冲突方案

在APP的Templates目录下创建以APP名为名称的目录

###Django中的Models是什么？

通常，一个Model对应数据库的一张数据表，Django中Models
以类的形式表现，包含了一些基本字段以及数据的一些行为

###ORM

对象关系映射（object relation mapping），
实现了对象和数据库之间的映射，隐藏了数据访问的细节，不需要编写SQL语句。

###生成数据表
python manage.py makemigrations app名(app名可以不写)
python manage.py migrate
python manage.py sqlmigrate 应用名 文件id // 查看SQL语句

###Django数据库操作文档：

https://docs.djangoproject.com/en/1.10/ref/models/fields/

使用第三方软件`SQLite Expert Personal`(轻量级、免费)查看并编辑db.sqlite3

###配置Admin

创建用户
`python manage.py createsuperuser` // 创建超级用户

改变后台管理系统为中文：修改`settings.py`中的LANGUAGE_CODE = 'zh-Hans'  

###Django Shell  

python manage.py shell



























