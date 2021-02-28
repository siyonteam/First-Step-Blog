from django.contrib import admin
from .models import Post , Comment


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'publish'
    list_display = ('title','publish','status','author')
    readonly_fields = ('author',)
    list_filter = ('publish','status','author')
    search_fields = ('title' , 'body')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
