from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)  # CHAR는 max_length가 필요
    content = models.TextField()  # 길이 제한 없음
    image = models.ImageField(blank=True, null=True)
    # 글을 쓸때, 우리는 생성일, 수정일이 자동적으로 넣어준다.
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일, 더해질때 한번 더해준다 -> now, add
    updated_at = models.DateTimeField(auto_now=True)  # 수정일, 변경될때 그때의 시간, 날짜 -> now

    # 오버라이딩 / Article을 문자열로 표현하면 항상 f'{}로 돌려주세요
    def __str__(self):
        return f'{self.id}번째글 - {self.title}' 

    
