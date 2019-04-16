from django.db import models

# Create your models here.


class TeaInfo(models.Model):
    tname = models.CharField(max_length=20)
    tsubject = models.CharField(max_length=20)

    def __str__(self):
        return self.tname


class ClassInfo(models.Model):
    cname = models.CharField(max_length=20)
    ctea = models.ForeignKey('TeaInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.cname


class StuInfo(models.Model):
    sname = models.CharField(max_length=20)
    sage = models.IntegerField()
    sgender = models.BooleanField()
    # 外键
    sclass = models.ForeignKey('ClassInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.sname

