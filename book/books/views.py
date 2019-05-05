from django.shortcuts import render, reverse, redirect
from .models import StuUser, BookInfo, History, HotPic
from django.http import HttpResponse
from datetime import datetime, timedelta
from manager.models import Article
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, JSONWebSignatureSerializer
from PIL import Image, ImageDraw, ImageFont
import random
import io
from django.views.decorators.cache import cache_page

# Create your views here.


def get_user(request):
    uid = request.session.get('uid')
    user = StuUser.objects.get(pk=uid)
    return user


# @cache_page(60*5)
def index(request):
    return render(request, 'index.html')


def mail(request):
    try:
        if request.method == 'GET':
            return render(request, 'mail.html')
        else:
            recipient = request.POST['recipient']
            print(recipient, type(recipient))
            title = request.POST['title']
            message = request.POST['message']
            print('!!!!!!!!!!!!!!!!!!!!!!!!')
            send_mail(title, message, settings.DEFAULT_FROM_EMAIL, [recipient])
            print('###############################################')
            return redirect(reverse('books:mail'))
    except Exception as e:
        print(e)
        return HttpResponse('发送失败！')


def user_login(request):
    if request.method == 'GET':
        return render(request, 'reader_login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['password']
        verifycode = request.POST['verifycode'].lower()
        verifycode1 = request.session['verifycode'].lower()
        if verifycode == verifycode1:
            users = StuUser.objects.all()
            for user in users:
                if user.username == username and pwd == user.password:
                    if user.is_active:
                        request.session['uid'] = user.id
                        return redirect(reverse('books:reader'))
                    else:
                        error = '您的账户未激活，赶紧去激活登录吧'
                        return render(request, 'reader_login.html', {'error': error})
            else:
                error = '您的密码或者用户名错误！请重新输入'
                return render(request, 'reader_login.html', {'error': error})
        else:
            error = '验证码错误，请重新输入'
            return render(request, 'reader_login.html', {'error': error})


def verify(request):
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 25
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0asdfghjklqwertyuiopmnbvcxz'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('LCALLIG.TTF', random.randrange(20, 25))
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # # 绘制4个字
    draw.text((5, 1), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 1), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 1), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 1), rand_str[3], font=font, fill=fontcolor)

    # draw.text((5, 2), rand_str[0], )
    # draw.text((25, 2), rand_str[1], )
    # draw.text((50, 2), rand_str[2],)
    # draw.text((75, 2), rand_str[3],)
    # 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        try:
            name = request.POST['username']
            res = StuUser.objects.filter(username=name)
            if len(res) == 0:
                pwd = request.POST['password']
                pwd2 = request.POST['password2']
                if pwd == pwd2:
                    sno = request.POST['number']
                    res1 = StuUser.objects.filter(sno=sno)
                    if len(res1) == 0:
                        college = request.POST['college']
                        email = request.POST['email']
                        StuUser.objects.create(username=name, password=pwd2,
                                               college=college, sno=sno, email=email, is_active=False).save()
                        sid = StuUser.objects.get(username=name).id
                        serutil = Serializer(settings.SECRET_KEY, 600)
                        uid = serutil.dumps({'uid': sid}).decode('utf-8')
                        send_mail('账号激活', '<a href="http://192.168.12.162:8000/books/active/%s">点我激活账号</a>'
                                  % (uid, ), settings.DEFAULT_FROM_EMAIL, [email])
                        return redirect(reverse('books:user_login'))
                    else:
                        error = '学号已经存在'
                        return render(request, 'register.html', {'error': error})
                else:
                    error = '密码输入不一致'
                    return render(request, 'register.html', {'error': error})
            else:
                error = '用户名已经存在'
                return render(request, 'register.html', {'error': error})
        except:
            error = '注册失败,可能您的输入不合法,请重新注册'
            return render(request, 'register.html', {'error': error})


def active(request, sid):
    try:
        dserutil = Serializer(settings.SECRET_KEY, 600)
        obj = dserutil.loads(sid)
        sid = obj['uid']
        user = StuUser.objects.get(pk=sid)
        user.is_active = True
        user.save()
        return redirect(reverse('books:user_login'))
    except SignatureExpired as e:
        return HttpResponse('过期了')


def reader(request):
    # uid = request.session.get('uid')
    # user = StuUser.objects.get(pk=uid)
    user = get_user(request)
    return render(request, 'reader.html', {'user': user})


def query(request):
    if request.method == 'GET':
        bs = BookInfo.objects.all()
        return render(request, 'reader_query.html', {'books': bs})
    else:
        bs = None
        q = request.POST['query']
        item = request.POST['item']
        if item == 'name':
            bs = BookInfo.objects.filter(title__icontains=q)
        elif item == 'author':
            bs = BookInfo.objects.filter(author__icontains=q)
        else:
            print('没选择++++++++++++++++++++++++++++++')
        print(bs)
        return render(request, 'reader_query.html', {'books': bs})


def bookdetail(request, bid):
    book = BookInfo.objects.get(pk=bid)
    if request.method == 'GET':
        if book.is_borrow:
            his = book.history_set.filter(is_re=False)[0]
            r = his.user
            return render(request, 'reader_book.html', {'book': book, 'his': his, 'reader': r})
        else:
            return render(request, 'reader_book.html', {'book': book})
    else:
        if book.is_borrow:
            return render(request, 'reader_book.html', {'book': book, 'error': '该书已经借出，您无法借阅'})
        else:
            book.is_borrow = True
            user = get_user(request)
            his = History()
            his.book = book
            his.user = user
            now = datetime.now()
            time = timedelta(days=30)
            his.re_time = now + time
            his.save()
            book.save()
            return redirect(reverse('books:bookdetail', args=(bid, )))


def logout(request):
    request.session.clear()
    return redirect(reverse('books:user_login'))


def userinfo(request):
    user = get_user(request)
    return render(request, 'reader_info.html', {'user': user})


def modify(request):
    if request.method == 'GET':
        user = get_user(request)
        return render(request, 'reader_modify.html', {'user': user})
    elif request.method == 'POST':
        try:
            username = request.POST['username']
            user = get_user(request)
            user1 = StuUser.objects.filter(username=username)
            if len(user1) == 0 or user.username == username:
                sno = request.POST['sno']
                user2 = StuUser.objects.filter(sno=int(sno))
                if len(user2) == 0 or user.sno == int(sno):
                    email = request.POST['email']
                    if len(email) == 0 or user.email == email:
                        pwd = request.POST['password']
                        if len(pwd) == 0:
                            college = request.POST['college']
                            user.username = username
                            user.sno = sno
                            user.email = email
                            user.college = college
                            user.save()
                            return redirect(reverse('books:userinfo'))
                        else:
                            user = get_user(request)
                            college = request.POST['college']
                            email = request.POST['email']
                            user.username = username
                            user.password = pwd
                            user.sno = sno
                            user.email = email
                            user.college = college
                            user.save()
                            return redirect(reverse('books:userinfo'))
                    else:
                        error = '邮箱已被其他人占用'
                        return render(request, 'reader_modify.html', {'error': error})
                else:
                    error = '学号已经存在，请重新输入！'
                    return render(request, 'reader_modify.html', {'error': error})
            else:
                error = '用户名已经存在，请重新输入！'
                return render(request, 'reader_modify.html', {'error': error})
        except Exception as e:
            print(e)
            error = '修改失败，可能您的输入不合法'
            return render(request, 'reader_modify.html', {'error': error})


def history(request):
    user = get_user(request)
    historys = user.history_set.all()
    print(type(historys))
    return render(request, 'reader_history.html', {'historys': historys})


def edit(request):
    if request.method == 'GET':
        es = Article.objects.all()
        return render(request, 'edit.html', {'es': es})
    else:
        title = request.POST['title']
        message = request.POST['message']
        art = Article(title=title, content=message)
        art.save()
        return redirect(reverse('manager:index'))


def ajax(request):
    if request.method == 'GET':
        return render(request, 'ajax.html')


def ajaxload(request):
    if request.method == 'GET':
        return HttpResponse('GET请求成功')
    else:
        return HttpResponse('POST请求成功')


def option(request):
    return render(request, 'option.html')
