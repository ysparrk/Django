# 데일리 과제 3-2에서 작성한 모델 Article 모델을 참고하여 작성하시오.

# 1. 마이그레이션 작업
'''
$ python manage.py makemigrations
$ python manage.py migrate
'''

# 2. 레코드 생성
'''
$ python manage.py shell_plus 

>>> article = Article()
>>> article
<Article: Article object (None)>

>>> article.title = 'first'
>>> article.content = 'django!'

>>> article.save()  # 저장

'''
