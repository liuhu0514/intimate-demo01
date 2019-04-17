from django.shortcuts import render
from django.http import HttpResponse
from .models import HeroInfo, BookInfo
from django.template import loader

# Create your views here.


def index(request):
    # return HttpResponse('首页')
    # 加载模板
    temp = loader.get_template('booktest/index.html')
    con = {'username': '希特勒'}
    temp = temp.render(con)
    return HttpResponse(temp)


def list(request):
    bs = BookInfo.objects.all()
    temp = loader.get_template('booktest/list.html')
    con = {'booklist': bs}
    result = temp.render(con)
    return render(request, 'booktest/list.html', context=con)
    # return HttpResponse(result)


def detail(request,id):
    try:
        b = BookInfo.objects.get(pk=int(id))
        temp = loader.get_template('booktest/detail.html')
        con = {'book': b}
        result = temp.render(con)
        return HttpResponse(result)
    except Exception as e:
        print(e)


def herodetail(request,id):
    hero = HeroInfo.objects.get(pk=id)
    temp = loader.get_template('booktest/herodetail.html')
    con = {'hero': hero}
    temp = temp.render(con)
    return HttpResponse(temp)


"""
视图函数
将函数和路由绑定 
"""

