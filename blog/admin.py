from django.contrib import admin
from .models import BlogPost


# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'image', 'slug', 'author', 'date_published','date_updated']
