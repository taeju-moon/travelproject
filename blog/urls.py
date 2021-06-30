from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'blog'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('<str:id>', detail, name="detail"), #id(기본키에 따라 화면 다르게 표시), detail은 함수이름
    path('new/', new, name='new'),
    path('create/', create, name="create"),
    path('edit/<str:id>',edit,name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
]