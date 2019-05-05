from django.shortcuts import render, redirect, reverse
from .models import User, Comment, Classify, Article, Label
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


# def index(request, n):
#     n = int(n)
#     articles = Article.objects.all()[(n*5-5):((n+1)*5)]
#     cls = Classify.objects.all()
#     ls = Label.objects.all()
#     last_articles = Article.objects.order_by('-pub_time')[:3]
#     return render(request, 'blogapp/index.html', {'articles': articles, 'cls': cls, 'ls': ls, 'la': last_articles})


def index(request):
    if request.method == 'GET':
        articles = Article.objects.order_by('-pub_time')
        cls = Classify.objects.all()
        ls = Label.objects.all()
        last_articles = Article.objects.order_by('-pub_time')[:3]
        paginnator = Paginator(articles, 3)
        page = request.GET.get('page')
        try:
            books = paginnator.page(page)
        except PageNotAnInteger:
            books = paginnator.page(1)
        except EmptyPage:
            books = paginnator.page(paginnator.num_pages)
        return render(request, 'blogapp/index.html', {'articles': books, 'cls': cls, 'ls': ls, 'la': last_articles})


def about(request):
    return render(request, 'blogapp/about.html')


def contact(request):
    return render(request, 'blogapp/contact.html')


def detailadd(request, aid):
    ar = Article.objects.get(pk=aid)
    ar.num += 1
    ar.save()
    return redirect(reverse('blogapp:detail', args=(aid, )))


def detail(request, aid):
    if request.method == 'GET':
        ar = Article.objects.get(pk=aid)
        cls = Classify.objects.all()
        ls = Label.objects.all()
        last_articles = Article.objects.order_by('-pub_time')[:3]
        return render(request, 'blogapp/single.html',
                      {'cls': cls, 'ls': ls, 'la': last_articles, 'ar': ar, })
    elif request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        arid = request.POST['arid']
        url = request.POST['url']
        com = request.POST['comment']
        article = Article.objects.get(pk=arid)
        Comment.objects.create(cname=name, content=com, www=url, email=email, article=article).save()
        return redirect(reverse('blogapp:detail', args=(aid, )))


def blog(request):
    articles = Article.objects.order_by('-pub_time')
    return render(request, 'blogapp/full-width.html', {'articles': articles})


def blogs(request, cid):
    cla = Classify.objects.get(pk=cid)
    articles = cla.article_set.order_by('-pub_time')
    return render(request, 'blogapp/full-width.html', {'articles': articles})


def bloges(request, lid):
    la = Label.objects.get(pk=lid)
    articles = la.article_set.order_by('-pub_time')
    return render(request, 'blogapp/full-width.html', {'articles': articles})


def file(request, yid, mid):
    articles = Article.objects.filter(pub_time__year=yid).filter(pub_time__month=mid).order_by('-pub_time')
    return render(request, 'blogapp/full-width.html', {'articles': articles})
