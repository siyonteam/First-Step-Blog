from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import CommentForm



def home(request):
    contents = Post.objects.all()
    context = {
        "contents":contents,
    }
    return render(request,'Content.html',context)


def detail_article(request ,year , month , day , id , slug):
    article = get_object_or_404(Post,publish__year=year , publish__month=month , publish__day=day , pk=id , slug = slug)
    context = {
        "article":article,
        'myform':CommentForm,
    }

    return render(request ,'FullContent.html',context)