from django.shortcuts import render, redirect, reverse
from .models import Manager, Article
from books.models import BookInfo, History, StuUser, HotPic
from datetime import datetime
# Create your views here.


def manager_login(request):
    if request.method == 'GET':
        return render(request, 'manager_login.html')
    else:
        name = request.POST['username']
        pwd = request.POST['password']
        ms = Manager.objects.all()
        for m in ms:
            if name == m.username and pwd == m.password:
                request.session['mid'] = m.id
                return redirect(reverse('manager:index'))
        else:
            error = '用户名或密码错误'
            return render(request, 'manager_login.html', {'error': error})


def index(request):
    mid = request.session.get('mid')
    m = Manager.objects.get(pk=mid)
    return render(request, 'manager.html', {'m': m})


def book_manage(request):
    books = BookInfo.objects.all()
    return render(request, 'manager_books.html', {'books': books})


def addbook(request):
    if request.method == 'GET':
        return render(request, 'manager_books_add.html')
    elif request.method == 'POST':
        try:

            isbn = request.POST['id']
            book = BookInfo.objects.filter(isbn=isbn)
            if len(book) == 0:
                isbn = request.POST['id']
                title = request.POST['name']
                author = request.POST['author']
                company = request.POST['company']
                datetime = request.POST['date']
                BookInfo.objects.create(isbn=int(isbn), title=title, author=author,
                                        press=company, pub_time=datetime).save()
                return redirect(reverse('manager:book_manage'))
            else:
                error = '您要注册的书号已经存在，请重新填写'
                return render(request, 'manager_books_add.html', {'error': error})
        except:
            error = '您的输入不合法，请重新输入！'
            return render(request, 'manager_books_add.html', {'error': error})


def deletebook(request):
    if request.method == 'GET':
        return render(request, 'manager_books_delete.html')
    else:
        isbn = request.POST['id']
        book = BookInfo.objects.filter(isbn=int(isbn))
        if len(book) == 0:
            error = '您要删除的书目不在'
            return render(request, 'manager_books_delete.html', {'error': error})
        else:
            try:
                book[0].delete()
                return redirect(reverse('manager:book_manage'))
            except:
                error = '删除失败！'
                return render(request, 'manager_books_delete.html', {'error': error})


def bookdetail(request, bid):
    if request.method == 'GET':
        book = BookInfo.objects.get(pk=bid)
        his = book.history_set.filter(is_re=False)
        if len(his) == 0:
            return render(request, 'manager_book.html', {'book': book})
        else:
            return render(request, 'manager_book.html', {'book': book, 'his': his[0]})
    elif request.method == 'POST':
        book = BookInfo.objects.get(pk=bid)
        his = book.history_set.filter(is_re=False)[0]
        book.is_borrow = False
        his.re_time = datetime.now()
        his.is_re = True
        his.save()
        book.save()
        return redirect(reverse('manager:bookdetail', args=(bid, )))


def book_modify(request, bid):
    book = BookInfo.objects.get(pk=bid)
    if request.method == 'GET':
        return render(request, 'manager_modify.html', {'book': book})
    else:
        try:
            title = request.POST['name']
            author = request.POST['author']
            press = request.POST['company']
            time = request.POST['date']
            book = BookInfo.objects.get(pk=bid)
            book.title = title
            book.author = author
            book.press = press
            book.pub_time = time
            book.save()
            return redirect(reverse('manager:bookdetail', args=(book.id, )))
        except:
            error = '修改失败，请输入有效数据！'
            return render(request, 'manager_modify.html', {'book': book, 'error': error})


def user_manage(request):
    users = StuUser.objects.all()
    return render(request, 'manager_users.html', {'users': users})


def userdetail(request, uid):
    user = StuUser.objects.get(pk=uid)
    return render(request, 'manager_userinfo.html', {'user': user})


def deleteuser(request, uid):
    user = StuUser.objects.get(pk=uid)
    user.delete()
    users = StuUser.objects.all()
    return render(request, 'manager_users.html', {'users': users})


def user_modify(request, uid):
    if request.method == 'GET':
        user = StuUser.objects.get(pk=uid)
        return render(request, 'manager_user_modify.html', {'user': user})
    else:
        try:
            user = StuUser.objects.get(pk=uid)
            username = request.POST['username']
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
                            college = request.POST['college']
                            email = request.POST['email']
                            user.username = username
                            user.password = pwd
                            user.sno = sno
                            user.email = email
                            user.college = college
                            user.save()
                            return redirect(reverse('manager:userdetail', args=(uid, )))
                    else:
                        error = '邮箱已被其他人占用'
                        return render(request, 'manager_user_modify.html', {'error': error})
                else:
                    error = '学号已经存在，请重新输入！'
                    return render(request, 'manager_user_modify.html', {'error': error})
            else:
                error = '用户名已经存在，请重新输入！'
                return render(request, 'manager_user_modify.html', {'error': error})
        except Exception as e:
            print(e)
            error = '修改失败，可能您的输入不合法'
            return render(request, 'manager_user_modify.html', {'error': error})


def upload(request):
    if request.method == 'GET':
        hots = HotPic.objects.all()
        return render(request, 'upload.html', {'hots': hots})
    else:
        name = request.POST['name']
        img = request.FILES['tu']
        i = request.POST['index']
        img = HotPic(name=name, pic=img, index=int(i))
        img.save()
        return redirect(reverse('manager:index'))


def hotinfo(request, hid):
    if request.method == 'GET':
        hot = HotPic.objects.get(pk=hid)
        return render(request, 'hotinfo.html', {'hot': hot})
    else:
        hot = HotPic.objects.get(pk=hid)
        num = request.POST['index']
        h = HotPic.objects.filter(index=num)
        if len(h) == 0 or int(num) == hot.index:
            name = request.POST['name']
            hot.index = num
            hot.name = name
            hot.save()
            return redirect(reverse('manager:upload'))

        else:
            error = '索引已存在'
            return render(request, 'hotinfo.html', {'hot': hot, 'error': error})


def hot_delete(request, hid):
    hot = HotPic.objects.get(pk=hid)
    hot.delete()
    return redirect(reverse('manager:upload'))


def einfo(request, aid):
    if request.method == 'GET':
        e = Article.objects.get(pk=aid)
        return render(request, 'edatil.html', {'e': e})
    else:
        title = request.POST['title']
        content = request.POST['content']
        e = Article.objects.get(pk=aid)
        e.title = title
        e.content = content
        e.save()
        return redirect(reverse('books:edit'))


def edelete(request, aid):
    a = Article.objects.get(pk=aid)
    a.delete()
    return redirect(reverse('books:edit'))
