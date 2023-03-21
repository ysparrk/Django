from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

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
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():  # 입력된 form이 유효하다면
            article = form.save()
            # form model이 연결되어 save하면 자동으로 data를 field에 넣고, 생성된 article 반환
            return redirect('articles:detail', article.pk)  # detail로 보낸다, 상세페이지 pk값 필요
    
    else:
        form = ArticleForm()

    context = {'form' : form}
    return render(request, 'articles/create.html', context)

# delete
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

# update
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)  # create가 아니라 기존의 있는 것에 update
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk=article.pk)        

    else:
        form = ArticleForm(instance=article)

    context = {'form': form}
    return render(request, 'articles/update.html', context)