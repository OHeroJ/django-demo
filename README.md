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











