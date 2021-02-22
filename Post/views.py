from django.shortcuts import render
from django.http import HttpResponse
from .models import Post



def home(request):
    contents = Post.objects.all()
    context = {
        "contents":contents,
    }
    return render(request,'Content.html',context)
