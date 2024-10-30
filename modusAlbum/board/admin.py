from django.contrib import admin
from .models import Board, Post, ImagePost

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'board', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('board',)
    ordering = ('-created_at',)

class ImagePostAdmin(admin.ModelAdmin):
    list_display = ('author', 'board', 'created_at')
    search_fields = ('author__username', )
    list_filter = ('board', 'author')
    ordering = ('-created_at',)

admin.site.register(Board)
admin.site.register(Post, PostAdmin)  # Post 모델 등록
admin.site.register(ImagePost, ImagePostAdmin)  # ImagePost 모델 등록