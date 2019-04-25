from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import CommentForm
from blog.models import Article
from django.http import HttpResponse

# Create your views here.


def commit_comment(request, aid):
    a = get_object_or_404(Article, pk=aid)
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.article = a
            comment.save()
            return redirect(reverse('blog:detail', args=(aid, )))
        else:
            return HttpResponse('评论失败')
    else:
        return HttpResponse('评论失败')

