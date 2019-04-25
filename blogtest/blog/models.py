from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

    def name(self):
        return self.username
    name.short_description = '用户昵称'

    def pwd(self):
        return self.password
    pwd.short_description = '密码'


class Classify(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def cname(self):
        return self.name
    cname.short_description = '类名'


class Label(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def lname(self):
        return self.name
    lname.short_description = '标签名'


class Article(models.Model):
    title = models.CharField(max_length=50)
    major = models.TextField()
    content = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    num = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cls = models.ForeignKey(Classify, on_delete=models.CASCADE)
    label = models.ManyToManyField('Label')

    def __str__(self):
        return self.title

    # def increseview(self):
    #     self.views += 1
    #     self.save()

    def a_title(self):
        return self.title
    a_title.short_description = '文章题目'

    def a_abstract(self):
        return self.major
    a_abstract.short_description = '摘要'

    def a_content(self):
        return self.content
    a_content.short_description = '文章内容'

    def a_pub_time(self):
        return self.add_time
    a_pub_time.short_description = '发表时间'

    def a_modify_time(self):
        return self.modify_time
    a_modify_time.short_description = '修改时间'

    def a_num(self):
        return self.num
    a_num.short_description = '阅读次数'

    def a_author(self):
        return self.author
    a_author.short_description = '作者'

    def a_cls(self):
        return self.cls
    a_cls.short_description = '分类'

    def a_label(self):
        return self.label
    a_label.short_description = '标签'
