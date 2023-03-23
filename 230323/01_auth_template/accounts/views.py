from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# today
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # request.POST에 있는 데이터를 채워서
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # 회원가입 후 로그인 처리 해주세요
            return redirect('articles:index')
        
    else:
        form = CustomUserCreationForm()
    context = {'form' : form}
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['POST'])  # POST만 허용할 것이다.
def delete(request):
    # post로 요청이 들어오면 실행을 하고 싶다. 부수적인 로직이 붙지 않게 -> 데코레이터
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)  # user가 입력한 데이터 가져옴 -> 어디에 채워 넣어야 하나 -> instance
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user) # 비어있는 form을 user에게 준다 -> 기존 데이터를 넣어서 줘야 함(instance)
    context = {'form' : form}
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form' : form}
    return render(request, 'accounts/change_password.html', context)