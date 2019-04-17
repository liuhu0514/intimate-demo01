from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.btitle

    def num(self):
        return self.pk

    num.short_description = '编号'

    def title(self):
        return self.btitle

    title.short_description = '书名'

    def pub_date(self):
        return self.bpub_date

    pub_date.short_description = '出版时间'


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=50)
    # 外键 第一个参数为表名  第二个参数代表删除类型
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.hname

    def num(self):
        return self.pk

    num.short_description = '编号'

    def name(self):
        return self.hname

    name.short_description = '名字'

    def sex(self):
        return self.hgender

    sex.short_description = '性别'

    def content(self):
        return self.hcontent

    content.short_description = '技能'

    def book(self):
        return self.hbook

    book.short_description = '所属图书'


"""
django MVT M
ORM 对象中的 O
需要定义实体类
"""

