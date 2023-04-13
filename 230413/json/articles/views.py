from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
# html 응답
def article_html(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/article.html', context)

# 1) JSON Response
def article_json_1(request):
    articles = Article.objects.all()  # 데이터 가져오기
    articles_json = []  # 빈 리스트 정의

    for article in articles:
        articles_json.append(
            {
                'id' : article.pk,
                'title' : article.title,
                'content' : article.content,
                'created_at' : article.created_at,
                'updated_at' : article.updated_at,
            }
        )
    # articles_json은 리스트일 뿐이다. json이 담긴 http response로 바꿔줘야 한다
    return JsonResponse(articles_json, safe=False)


# 2) Serializer (data -> json 포맷으로 만든다)
def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json') 

# 3) DRF
@api_view(['GET']) # api로 사용하는 view 이다
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
