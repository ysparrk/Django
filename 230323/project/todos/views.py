from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TodoForms
from .models import Todo

# Create your views here.
def index(request):
    print('index 함수 도착')
    form = TodoForms()
    todo_lst = Todo.objects.all()  # 모든 Todo 데이터 조회
    # 단일객체 todo = 
    context = {
        'form' : form,
        'todo_lst' : todo_lst

    }

    return render(request, 'todos/index.html', context)


def create(request):
    print('#' * 30)
    print('create 함수 도착')
    print(f'request : {request}')
    print(request.method)  # POST
    print(type(request.method)) # str
    print(request.POST)
    print('#' * 30)
    if request.method == 'POST':  # TODO 작성 요청
        # task = request.POST.get('task')
        form = TodoForms(request.POST)
        if form.is_valid():  # 유효성 검사 -> cleaned_data(dict형태로 나온다) -> clean_field
            form.save()
            
        return redirect('todos:index')

# 함수를 실행시키기 전에 user가 로그인 되어 있는지 아닌지 확인, 안되어 있으면 로그인페이지로 간다 
@login_required   
def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    print('update')
    if request.method == 'POST':
        form = TodoForms(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('todos:index')
    else:
        form = TodoForms(instance=todo)
        
    context = {
        'form' : form,
        'todo' : todo,
    }
    return render(request, 'todos/update.html', context)

def delete(request, pk):
    if request.method == 'POST':
        todo = Todo.objects.get(pk=pk)
        todo.delete()



    else:
        pass

    return redirect('todos:index')


def done(request, pk):
    # auth가 있다면?
    todo = Todo.objects.get(pk=pk)
    todo.isCompleted = True
    todo.save()

    return redirect('todos:index')

    