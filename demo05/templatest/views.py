from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.


def goods(request):
    return render(request, 'templatest/goods_base.html')


def user(request):
    return render(request, 'templatest/user_base.html')


def login(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'templatest/login.html', {'form': form})
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if request.POST['username'] == 'liuhu':
                form.save()
                return HttpResponse('登录成功！')
            else:
                form.save(commit=False)
                return HttpResponse('登录失败！')
