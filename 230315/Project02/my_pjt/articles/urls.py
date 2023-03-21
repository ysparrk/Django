from django.urls import path
from . import views


urlpatterns = [
    path('hello/<str:name>/', articles_views.hello),
]




