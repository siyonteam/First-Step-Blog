from django.contrib import admin
from django.urls import path , include
from .views import home, detail_article


app_name = "Post"

urlpatterns = [
    path('',home,name="home"),
    path('article/<int:year>/<int:month>/<int:day>/<int:id>/<slug:slug>/',detail_article,name="detail_article"),
]
