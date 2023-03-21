from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles' : articles}
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # pk에 해당하는 글을 조회해서 넘겨줘야 한다. -> pk로 하나의 article 조회
    # id는 pk라 써도 된다.
    article = Article.objects.get(pk=pk)
    context = {'article' : article}
    return render(request, 'articles/detail.html', context)

# create
def new(request):
    return render(request, 'articles/new.html')

# DB에 저장 => 1) 사용자가 입력한 DATA 가져온다. 2) DB에 저장한다.
# 사용자가 전송한 데이터는 request에 들어있다.
def create(request):
    # 1) 사용자가 입력한 data 가져온다. 사용자가 전송한 데이터는 request에 들어있다.
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # 2) DB에 새로운 Article 저장
    Article.objects.create(
        title=title,
        content=content,
    )

    # 2) -1 
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # # 2) - 2
    # article = Article(title=title, content=content)
    # # 저장 되기 전 로직 추가 가능
    # article.save()

    # 3) 어떤 url로 보낼건지
    return redirect('articles:index')

# delete
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

# update
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', pk=article.pk)