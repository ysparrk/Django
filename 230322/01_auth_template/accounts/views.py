from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm  # 비어있는 폼 제공
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    if request.method == 'POST':  # 로그인폼을 입력하고 로그인을 누르는 것
        # 로그인 처리를 해줌
        # 1) 입력한 아이디와 패스워드가 일치하는지 검사
        # 2) 일치하면 session table가서 session 만들고,
        # 3) 쿠키에 session id 담아서 전송
        # => django에서 가지고 있다.
        form = AuthenticationForm(request, request.POST)  # (요청들어온 곳에 쿠키 담아서 보냄)
        if form.is_valid():
            auth_login(request, form.get_user())
            # 응답
            return redirect('articles:index')

    else:
        # 비어있는 로그인 페이지를 제공 -> 이미 가지고 있음
        form = AuthenticationForm()
    context = {'form' : form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    # 현재 request로 들어왔는데, 
    # 요청에 있는 쿠키를 열어서 session id가 있으면 꺼내서 
    # db의 session table과 비교해서 있으면 로그아웃
    auth_logout(request)
    return redirect('articles:index')
