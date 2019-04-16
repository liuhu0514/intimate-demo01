from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(auto_now_add=True)


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=50)
    # 外键 第一个参数为表名  第二个参数代表删除类型
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)


"""
django MVT M
ORM 对象中的 O
需要定义实体类
"""

