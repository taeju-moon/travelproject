from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'blog'
urlpatterns = [
    path('home/',home,name="home"),
    path('home2/',home2,name="home2"),
    path('home3/',home3,name="home3"),
    path('hub/',hub,name="hub"),
    path('search/',search,name="search"),
    path('<str:id>', detail, name="detail"), #id(기본키에 따라 화면 다르게 표시), detail은 함수이름
    path('new/', new, name='new'),
    path('create/', create, name="create"),
    path('edit/<str:id>',edit,name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
    path('comment_delete/<str:id>', comment_delete, name="comment_delete"),
    path('comment_delete_handle/<str:id>',comment_delete_handle,name="comment_delete_handle"),
    path('my_comment/',my_comment,name="my_comment"),
]

