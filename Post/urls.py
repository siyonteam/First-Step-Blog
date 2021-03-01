from django.contrib import admin
from django.urls import path , include
from .views import home, detail_article ,add_comment , add_reply


app_name = "Post"

urlpatterns = [
    path('',home,name="home"),
    path('article/<int:year>/<int:month>/<int:day>/<int:id>/<slug:slug>/',detail_article,name="detail_article"),
    path('article/<int:pk>/comment/',add_comment , name="add_comment"),
    path('article/comment/reply/<int:post_pk>/<int:comment_pk>/',add_reply , name="add_reply"),
]
