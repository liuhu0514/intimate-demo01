from django.db import models

# Create your models here.


class SubjectInfo(models.Model):
    sname = models.CharField(max_length=20)


class ClaInfo(models.Model):
    cname = models.CharField(max_length=20)


class TeaInfo(models.Model):
    tname = models.CharField(max_length=20)
    tage = models.IntegerField()
    tgender = models.BooleanField()
    tsub = models.ForeignKey('SubjectInfo', on_delete=models.CASCADE)
    tcla = models.ForeignKey('ClaInfo', on_delete=models.CASCADE)


class StuInfo(models.Model):
    sname = models.CharField(max_length=20)
    sage = models.IntegerField()
    sgender = models.BooleanField()
    scla = models.ForeignKey('ClaInfo', on_delete=models.CASCADE)
