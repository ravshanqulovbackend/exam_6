from django.contrib import admin
from .models import Category, Post, Comment, PostImage

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 3

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]  
    list_display = ('title', 'category', 'created_at')

admin.site.register(Category)
admin.site.register(Comment)
