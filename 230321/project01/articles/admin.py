from django.contrib import admin
from .models import Article

# Register your models here.
# admin.site.register(Article)

# 내가 관리하고 싶은 것만 보기
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content')