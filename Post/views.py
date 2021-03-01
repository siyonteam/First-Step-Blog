from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Post , Comment
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


def add_comment(request , pk):
    post = get_object_or_404(Post , pk=pk)

    if request.method=='POST':
        name = request.POST.get("author")
        email = request.POST.get("email")
        body = request.POST.get("body")
        Comment(author=name , email=email , body = body , post=post).save()
        messages.success(request , "دیدگاه شما با موفقیت ثبت شد" )
        return redirect(post)


def add_reply(request , post_pk , comment_pk):
    comment = get_object_or_404(Comment , pk=comment_pk)
    post = get_object_or_404(Post , pk=post_pk)

    if request.method=='POST':
        name = request.POST.get("author")
        email = request.POST.get("email")
        body = request.POST.get("body")
        Comment(author=name , email=email , body = body , reply=comment).save()
        messages.success(request , "دیدگاه شما با موفقیت ثبت شد" )
        return redirect(post)
        
    