from django.db import models

# Create your models here.


class User(models.Model):
    """
    用户表
    """
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    def name(self):
        return self.username
    name.short_description = '用户昵称'

    def pwd(self):
        return self.password
    pwd.short_description = '密码'


class Classify(models.Model):
    """
    分类表
    """
    cname = models.CharField(max_length=30)

    def __str__(self):
        return self.cname

    def name(self):
        return self.cname
    name.short_description = '类名'


class Label(models.Model):
    """
    标签
    """
    l_name = models.CharField(max_length=20)

    def __str__(self):
        return self.l_name

    def name(self):
        return self.l_name
    name.short_description = '标签名'


class Article(models.Model):
    """
    文章
    """
    # 标题
    title = models.CharField(max_length=100)
    # 摘要
    abstract = models.TextField()
    # 内容
    content = models.TextField()
    # 时间
    pub_time = models.DateTimeField(auto_now_add=True)
    # 阅读量
    num = models.IntegerField(default=0)
    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 分类
    cls = models.ForeignKey(Classify, on_delete=models.CASCADE)
    # 标签
    label = models.ManyToManyField('Label')

    def __str__(self):
        return self.title

    def a_title(self):
        return self.title
    a_title.short_description = '文章题目'

    def a_abstract(self):
        return self.abstract
    a_abstract.short_description = '摘要'

    def a_content(self):
        return self.content
    a_content.short_description = '文章内容'

    def a_pub_time(self):
        return self.pub_time
    a_pub_time.short_description = '发表时间'

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


class Comment(models.Model):
    """
    评论
    """
    # 评论人
    cname = models.CharField(max_length=20)
    # 评论内容
    content = models.TextField()
    # 评论时间
    pub_time = models.DateTimeField(auto_now_add=True)
    # 评论网址
    www = models.URLField()
    # 评论邮箱
    email = models.EmailField()
    # 评论文章
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.cname

    def name(self):
        return self.cname
    name.short_description = '评论人'

    def c_content(self):
        return self.content
    c_content.short_description = '评论内容'

    def c_pub(self):
        return self.pub_time
    c_pub.short_description = '评论时间'

    def c_www(self):
        return self.www
    c_www.short_description = '评论网址'

    def c_email(self):
        return self.email
    c_email.short_description = '评论邮箱'

    def c_article(self):
        return self.article
    c_article.short_description = '评论文章'
