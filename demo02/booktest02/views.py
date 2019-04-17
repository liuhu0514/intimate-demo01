from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TeaInfo, ClassInfo, StuInfo

# Create your views here.


def index(request):
    temp = loader.get_template('booktest02/index.html')
    temp = temp.render()
    return HttpResponse(temp)


def list(request):
    teas = TeaInfo.objects.all()
    temp = loader.get_template('booktest02/tealist.html')
    con = {'teas': teas}
    temp = temp.render(con)
    return HttpResponse(temp)


def cla(request,id):
    tea = TeaInfo.objects.get(pk=id)
    temp = loader.get_template('booktest02/cla.html')
    con = {'tea': tea}
    temp = temp.render(con)
    return HttpResponse(temp)


def student(request, id):
    clas = ClassInfo.objects.get(pk=id)
    temp = loader.get_template('booktest02/student.html')
    con = {'clas': clas}
    temp = temp.render(con)
    return HttpResponse(temp)

