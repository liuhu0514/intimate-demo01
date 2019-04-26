from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class StuUser(User):
    # 学院
    college = models.CharField(max_length=30, blank=True, null=True)
    # 学号
    sno = models.IntegerField(max_length=16, blank=True, null=True, unique=True)

    def __str__(self):
        return self.username

    def name(self):
        return self.username
    name.short_description = '用户昵称'

    def pwd(self):
        return self.password

    pwd.short_description = '密码'

    def e(self):
        return self.email
    e.short_description = '邮箱'

    def col(self):
        return self.college
    col.short_description = '学院'

    def s(self):
        return self.sno
    s.short_description = '学号'


class BookInfo(models.Model):
    # 图书编号
    isbn = models.IntegerField(unique=True)
    # 书名
    title = models.CharField(max_length=30)
    # 作者
    author = models.CharField(max_length=20)
    # 出版社
    press = models.CharField(max_length=50)
    # 出版时间
    pub_time = models.DateTimeField()
    # 状态 False未借出 True已经借出
    is_borrow = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class History(models.Model):
    # 借阅时间
    bor_time = models.DateTimeField(auto_now_add=True)
    # 归还时间
    re_time = models.DateTimeField(blank=True, null=True)
    # 是否归还 False未归还，True已归还
    is_re = models.BooleanField(default=False)
    # 借阅人
    user = models.ForeignKey(StuUser, on_delete=models.CASCADE)
    # 借阅书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.book
