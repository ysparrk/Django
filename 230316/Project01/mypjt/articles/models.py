from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)  # title은 문자열이다, 20까지 저장 가능/db 공간 낭비 방지
    content = models.TextField()  # 글자수의 지정x