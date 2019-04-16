from django.db import models

# Create your models here.


class TeaInfo(models.Model):
    tname = models.CharField(max_length=20)
    tsubject = models.CharField(max_length=20)

    def skill(self):
        return self.tname
    skill.short_description = '名字'

    def subject(self):
        return self.tsubject
    subject.short_description = '课程'

    def id1(self):
        return self.pk
    id1.short_description = '编号'

    def __str__(self):
        return self.tname


class ClassInfo(models.Model):
    cname = models.CharField(max_length=20)
    ctea = models.ForeignKey('TeaInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.cname

    def id1(self):
        return self.pk
    id1.short_description = '编号'

    def skill(self):
        return self.cname
    skill.short_description = '班级名'

    def tea(self):
        return self.ctea
    tea.short_description = '教师'


class StuInfo(models.Model):
    sname = models.CharField(max_length=20)
    sage = models.IntegerField()
    sgender = models.BooleanField()
    # 外键
    sclass = models.ForeignKey('ClassInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.sname

    def id1(self):
        return self.pk
    id1.short_description = '编号'

    def skill(self):
        return self.sname
    skill.short_description = '名字'

    def age(self):
        return self.sage
    age.short_description = '年龄'

    def gender(self):
        return self.sgender
    gender.short_description = '性别'

    def sc(self):
        return self.sclass
    sc.short_description = '班级'

