from django.shortcuts import render

# Create your views here.
def hello(request, name):
    print('index 함수 호출됨')
    apple = ['iphone', 'mac', 'airpot']
    context = {
        'name' : name,
        
    }
    print('index 함수 종료')
    return render(request, 'articles/hello.html', context)