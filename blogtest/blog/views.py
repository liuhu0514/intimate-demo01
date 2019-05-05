from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import User, Classify, Label, Article
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from comment.forms import CommentForm
import markdown

# Create your views here.


def paging(request, articles):
    paginnator = Paginator(articles, 2)
    page = request.GET.get('page')
    try:
        articles = paginnator.page(page)
    except PageNotAnInteger:
        articles = paginnator.page(1)
    except EmptyPage:
        articles = paginnator.page(paginnator.num_pages)
    return articles


def index(request):
    articles = Article.objects.order_by('-add_time')
    # paginnator = Paginator(articles, 3)
    # page = request.GET.get('page')
    # try:
    #     articles = paginnator.page(page)
    # except PageNotAnInteger:
    #     articles = paginnator.page(1)
    # except EmptyPage:
    #     articles = paginnator.page(paginnator.num_pages)
    articles = paging(request, articles)
    return render(request, 'blog/index.html', {'articles': articles})


def detailadd(request, aid):
    a = Article.objects.get(pk=aid)
    a.num += 1
    a.save()
    return redirect(reverse('blog:detail', args=[aid]))


def detail(request, aid):
    if request.method == 'GET':
        a = get_object_or_404(Article, pk=aid)
        # 第一种markdown方法
        # a.increseview()
        # a.content = markdown.markdown(a.content, extensions=[
        #     'markdown.extensions.extra',
        #     'markdown.extensions.codehilite',
        #     'markdown.extensions.toc',
        # ])

        # 第二种markdown方法
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        a.content = md.convert(a.content)
        a.toc = md.toc
        form = CommentForm()
        return render(request, 'blog/single.html', {'a': a, 'form': form})


def cls(request, cid):
    if request.method == 'GET':
        c = Classify.objects.get(pk=cid)
        articles = c.article_set.order_by('-add_time')
        articles = paging(request, articles)
        return render(request, 'blog/index.html', {'articles': articles})


def label(request, lid):
    l = Label.objects.get(pk=lid)
    articles = l.article_set.order_by('-add_time')
    articles = paging(request, articles)
    return render(request, 'blog/index.html', {'articles': articles})


def file(request, y, m):
    articles = Article.objects.filter(add_time__year=y).filter(add_time__month=m).order_by('-add_time')
    articles = paging(request, articles)
    return render(request, 'blog/index.html', {'articles': articles})


def author(request, author_id):
    u = User.objects.get(pk=author_id)
    articles = u.article_set.order_by('-add_time')
    articles = paging(request, articles)
    return render(request, 'blog/index.html', {'articles': articles})
