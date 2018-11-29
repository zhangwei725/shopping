from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# 注册
# 登录
# 注销
# 修改密码  通过邮件方式修改密码
def login_view(request):
    if request.method == 'GET':
        next = request.GET.get('next')
        return render(request, 'login.html', {'next': next})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next = next if next else '/'
            return redirect(next)
        else:
            return render(request, 'login.html', {'next': next})
    else:
        return render(request, 'login.html', {'next': next})


def register_view(request):
    pass


def logout_view(request):
    logout(request)
    return redirect('/')
