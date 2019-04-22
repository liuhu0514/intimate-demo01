from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import HeroInfo, BookInfo
from django.template import loader

# Create your views here.


def index(request):
    # return HttpResponse('首页')
    # 加载模板
    temp = loader.get_template('booktest/index.html')
    con = {'username': '希特勒'}
    temp = temp.render(con)
    username = request.session.get('username')
    print(username)
    return render(request, 'booktest/index.html', {'username': username})


def login(request):
    if request.method == 'GET':
        return render(request, 'booktest/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        request.session['username'] = username
        return redirect(reverse('booktest:index'))


def logout(request):
    request.session.clear()
    return redirect(reverse('booktest:index'))


def list(request):
    bs = BookInfo.objects.all()
    # temp = loader.get_template('booktest/list.html')
    con = {'booklist': bs}
    # result = temp.render(con)
    # return render(request, 'booktest/list.html', context=con)
    # return HttpResponse(result)
    return render(request, 'booktest/list.html', {'booklist': bs})


def detail(request, bid):
    book = BookInfo.objects.get(pk=bid)
    return render(request, 'booktest/detail.html', {'book': book})


def herodetail(request, hid):
    hero = HeroInfo.objects.get(pk=hid)
    return render(request, 'booktest/herodetail.html', {'hero': hero})


def add(request):
    return render(request, 'booktest/add.html')


def addhandle(request):
    btitle = request.POST['btitle']
    BookInfo.objects.create(btitle=btitle).save()
    return HttpResponseRedirect('/booktest/list/')


def delete(request, bid):
    BookInfo.objects.get(pk=bid).delete()
    bs = BookInfo.objects.all()
    # temp = loader.get_template('booktest/list.html')
    con = {'booklist': bs}
    # result = temp.render(con)
    # return render(request, 'booktest/list.html', context=con)
    # return HttpResponse(result)
    return redirect(reverse('booktest:booklist'), {'booklist': bs})


def addhero(request, bookid):
    book = BookInfo.objects.get(pk=bookid)
    return render(request, 'booktest/addhero.html', {'book': book})


def addherohandle(request, bookid):
    book = BookInfo.objects.get(pk=bookid)
    hname = request.POST['heroname']
    hgender = request.POST['hgender']
    hcontent = request.POST['hcontent']
    h = HeroInfo()
    h.hname = hname
    if hgender == '1':
        h.hgender = True
    else:
        h.hgender = False
    h.hcontent = hcontent
    h.hbook = book
    h.save()
    return HttpResponseRedirect('/booktest/detail/'+str(bookid)+'/', {'book': book})


def edit(request, bid):
    book = BookInfo.objects.get(pk=bid)
    return render(request, 'booktest/edit.html', {'book': book})


def edithandle(request, bid):
    book = BookInfo.objects.get(pk=bid)
    book.btitle = request.POST['btitle']
    book.save()
    return HttpResponseRedirect('/booktest/list/')


def edithero(request, hid):
    hero = HeroInfo.objects.get(pk=hid)
    return render(request, 'booktest/edithero.html', {'hero': hero})


def editherohandle(request, hid):
    hero = HeroInfo.objects.get(pk=hid)
    book = hero.hbook
    hero.hanme = request.POST['hname']
    if request.POST['hgender'] == '男':
        hero.hgender = True
    else:
        hero.hgender = False
    hero.hcontent = request.POST['hcontent']
    hero.hbook = book
    hero.save()
    return HttpResponseRedirect('/booktest/detail/'+str(book.id)+'/', {'book': book})


def deletehero(request, hid):
    hero = HeroInfo.objects.get(pk=hid)
    book = hero.hbook
    hero.delete()
    return HttpResponseRedirect('/booktest/detail/'+str(book.id)+'/', {'book': book})


from .models import Area


def area(request):
    a = Area.objects.get(title='郑州')
    return render(request, 'booktest/area.html', {'area': a})


"""
视图函数
将函数和路由绑定 
"""

