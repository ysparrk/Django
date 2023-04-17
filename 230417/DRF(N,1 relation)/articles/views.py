from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Comment
from .serializers import ArticleListSerializer, CommentSerializer


# Create your views here.
# =================== Single model =============================
# # GET
# @api_view(['GET'])
# def article_list(request):
#     articles = Article.objects.all()
#     serializer = ArticleListSerializer(articles, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def article_detail(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     serializer = ArticleListSerializer(article)
#     return Response(serializer.data)

# POST
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)  # 404넣기
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data) # 역직렬화
        # if serializer.is_valid():  # 데이터가 유효하다면
        if serializer.is_valid(raise_exception=True):  # 실패하면 DRF 안에서 알아서 처리해준다
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # serializer 들어있는 데이터를 직렬화해서 json으로 준다, 새로 생성했다는 status
        
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # response안에는 클라이언트와 협의를 하는 부분. 지금은 errors에 담아준다.

# DELETE
# @api_view(['GET', 'DELETE'])
# def article_detail(request, article_pk):
#     article = Article.objects.get(pk=article_pk)

#     if request.method == 'GET':
#         serializer = ArticleListSerializer(article)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# PUT
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    # 수정
    # 1) 기존 인스턴스 2) 새로운 데이터 필요, 3) 2번을 1번에 넣고 save
    elif request.method == 'PUT':
        serializer = ArticleListSerializer(article, data=request.data)  # 기존 데이터에 넣기
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
# ============================== N : 1 ===============================
# GET-LIST
# @api_view(['GET'])
# def comment_list(request):
#     if request.method == 'GET':
#         comments = Comment.objects.all()
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)
    
# GET-DETAIL
@api_view(['GET'])
def comment_detail(request, comment_pk):
    if request.method == 'GET':
        comment = Comment.objects.get(pk=comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
# POST
# @api_view(['POST'])
# def comment_create(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     serializer = CommentSerializer(data=request.data) # request 데이터에는 article 정보가 없다.(content만 있다.) article의 정보를 넣어 주어야 한다.
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(article=article) # article 정보를 추가해서 저장
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# GET-LIST와 POST를 합친다
@api_view(['GET', 'POST'])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'GET':
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    

