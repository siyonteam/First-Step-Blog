from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.urls import reverse


class Post(models.Model):

    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    body = RichTextUploadingField(config_name = "Post")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=STATUS, max_length=10, default='draft')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("Post:detail_article", args=[self.publish.year,self.publish.month,self.publish.day,self.id , self.slug])
    


    
class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name="comments" , null = True , blank = True )
    reply = models.ForeignKey('self' , on_delete=models.CASCADE , related_name="rcomment" , null = True , blank = True )
    author = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()                             
    created = models.DateTimeField(auto_now_add=True)

    class Meta :
        ordering = ('-created',)

    def __str__(self):
        return self.body[:30]
    