# 使用 


## 安装 docker

直接到官网下载应用包安装即可。

添加PATH:

```sh
export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin/"
```

## 运行

```sh
$ docker-compose up -d 
$ python manage.py migrate
```

## 创建模型后，生成迁移脚本

```sh
$ poetry shell
$ python manage.py makemigrations
```

恢复迁移
```sh
$ python manage.py migrate tasks zero
```
由于这是初始迁移，因此我们需要使用 zero 。否则，需要指定迁移编号对应的迁移文件名前缀。

Django会自动检测模型的变化，并制作适合数据库的迁移代码。

要将这些更改应用于数据库，请运行migrate命令：

```sh
python manage.py migrate
```

```sh
$ python manage.py dbshell
>>> \d+ tasks_task # 最后一个命令应该输出创建的数据库，显示列、主键、索引和外键。
```

> 'dbshell' 命令提供了对 settings.py 中配置的数据库的直接访问，使其便于在开发期间进行故障排除和验证修改。


```sh
$ python manage.py makemigrations tasks --empty
```

上述命令将创建一个空迁移。然后，我们可以指示迁移系统执行某些Python操作




## Django的数据库API

Django自带了一个shell，允许你操作对象。

```sh
python manage.py shell
```

## 添加新应用

进入虚拟环境

```shell
$ poetry shell
$ django-admin startproject taskmanager # 创建一个新项目
$ cd taskmanager
$ python manager.py startapp tasks # 创建一个django 应用
$ python manage.py makemigrations tasks # 验证设置是否正确
$ python manage.py runserver 0.0.0.0:3000 # 运行服务器，并不适用于生产用途
```

## MVT 模式

Model-View-Template

使用服务层 Service 扩展MVT模式。

服务层提供到模型的接口。

## 模型

在Django中设计模型时，正确设置每个字段的null和blank属性至关重要。作为一般指导原则，建议尽量减少使用空值。限制空值可以使软件更健壮，因为您不必在查询中处理 IS NULL 或 IS NOT NULL 条件。这也确保了属性总是有一个值。

通常不建议同时允许字段为空和null。这可能会产生歧义，因为NULL和空字符串都被认为是 empty 或 no data 状态的表示，从而使数据完整性和查询逻辑变得复杂。

```py
owner = models.ForeignKey(
    User,
    related_name="owned_tasks",
    on_delete=models.SET_NULL,
    null=True,
    db_comment="Foreign Key to the User who currently owns the task.",
)
```

通过外键的User模型。它可以设置为null，特别是在创建任务时未确定任务的所有者时。当所有者对象被删除时，所有者被设置为null以防止删除Task对象

### on_delete 

* Aggregation 聚合：在聚合中，一个类（称为 whole ）可以包含另一个类（ part ）的实例，但 part 也可以在没有 whole 的情况下存在。在Django中，这类似于 models.SET_NULL 、 models.SET_DEFAULT 或 models.SET() （返回值的函数）。如果 whole 被删除， part 仍然存在，但外键分别被设置为 NULL 、其默认值或提供的函数的结果。

* Composition 组合：在组合中，一个类（ whole ）拥有或包含另一个类（ parts ）的对象，其中 parts 没有 whole 就不能存在。在Django中，这类似于 models.CASCADE 。如果 whole 被删除， parts 也会被删除。
* PROTECT，如果尝试删除关联对象，引发ProtectedError异常，防止删除
* SET()，当关联对象被删除时，调用一个指定的函数或者传入指定的值来设置字段的值
* DO_NOTHING， 什么也不做，仅在数据库层面执行，Django不会做任何处理。
* RESTRICT，类似于PROTECT，在某些数据库中的行为略有不同。

### CURD

Django提供了两种与数据库交互的主要方式：使用对象的 .save() 方法和对象管理器。每个Django模型都有一个管理器，你可以通过 Model.objects 访问它，它可以用来检索模型的实例。


### 迁移

Django有一个惊人的迁移系统，可以检测应用程序模型的变化。如果您创建或修改模型，Django的迁移系统会检测这些更改，并创建版本化文件来捕获模式更改。迁移是原子性的，这意味着每个迁移都被视为数据库的单个事务。


每个Django应用程序都有一个 'migrations' 目录，其中包含跟踪增量模式更改的文件。

```shell
$ python manage.py makemigrations
$ python manage.py migrate
```

通过手动写迁移脚本进行迁移

```shell
$ python manage.py makemigrations tasks --empty
```

### Django Admin 页面

tasks/admin.py 添加相关类

```shell
$ poetry shell 
$ python manage.py ceatesupperuser # 创建超管
```

Django的框架包括一个内置的身份验证系统，允许您为每个用户设置和验证特定的权限

Django使用双下划线是一种表示法，用于表示查询中的分隔

如果你需要使用OR操作符，你需要使用Django的Q，它通常用于创建复杂的查询.


### 一对多关系

```py
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

这意味着一个作者可以有多本书，但一本书只能有一个作者. on_delete=models.CASCADE是外键字段的一个参数，它指定了当与这个外键关联的对象被删除时的行为。在这里，CASCADE表示当与Book关联的Author对象被删除时，与之相关的所有Book对象也会被删除。

### 一对一关系

一个1对1关系的经典例子是一个用户（User）有一个用户资料（Profile）。在这个例子中，每个用户只有一个用户资料，而每个用户资料只能属于一个用户

```py
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
```

每个用户（User）可以有一个相关的用户资料（Profile），而每个用户资料（Profile）也只能属于一个用户（User），构成了一个1对1的关系。
on_delete=models.CASCADE指定了当与User关联的Profile对象的关联User对象被删除时，相关的Profile对象也会被删除。

### 多对多关系

```py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField('Course')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


student1 = Student.objects.create(name='Alice')
student2 = Student.objects.create(name='Bob')

course1 = Course.objects.create(name='Math')
course2 = Course.objects.create(name='Science')

student1.courses.add(course1)
student1.courses.add(course2)
student2.courses.add(course2)
```

Student模型代表了学生，Course模型代表了课程。Student模型有一个courses字段，它是一个多对多关系字段（ManyToManyField），关联到Course模型。

在Django中，当你定义了一个多对多关系字段时，Django会自动创建一个中间表来跟踪关联。这个中间表通常是隐式创建的，并且包含了两个外键，分别指向关联的两个模型。

### 反项外键

在Django中，反向外键（Reverse ForeignKey）是指在模型之间建立了一对多关系时，Django自动为目标模型（Many模型）添加一个属性，用于访问与之关联的一模型的实例。

假设我们有两个模型：Author（作者）和Book（书籍），一个作者可以写多本书，而一本书只能有一个作者。在Book模型中，我们可以添加一个外键字段指向Author模型，例如：

```py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

在这个例子中，Book模型有一个外键字段author，它指向Author模型，表示了一本书对应一个作者，是一个一对多关系。

在Django中，当你使用ForeignKey定义这样的关系时，Django会自动在目标模型（在这里是Author）中添加一个反向外键，通常会以小写的模型名称加上_set后缀作为属性名，用于访问与之关联的一模型的实例。

所以，在这个例子中，Author模型会自动添加一个名为book_set的属性，通过它你可以访问一个作者写过的所有书籍。例如：

```py
author = Author.objects.get(pk=1)
books_written_by_author = author.book_set.all()
```

这样，book_set就是反向外键，它允许你从Author模型访问与之关联的Book模型的实例。







## 模板引擎

* 若应用和工程的模板模板都包含被重写的模板，默认的 Django 模板加载器会先尝试加载工程目录下的模板。换句话说，先查找 DIRS，其次 APP_DIRS。












