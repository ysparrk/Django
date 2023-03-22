# django에 내장된 로그인/로그아웃 기능을 사용하기 위한 import문을 작성하시오(이때, as 구문은 생략합니다)
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login 
from django.contrib.auth import logout