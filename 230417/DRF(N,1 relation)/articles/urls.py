from django.urls import path
from articles import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    # N : 1
    # path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    # path('articles/<int:article_pk>/comments/', views.comment_create), # 댓글 작성
    path('articles/<int:article_pk>/comments/', views.comment_list), # 특정 게시물의 모든 댓글 조회
]   
