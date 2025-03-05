from django.contrib import admin
from .models import Article, ArticleCategory

class ArticleInline(admin.TabularInline):
    model = Article

class ArticleAdmin(admin.ModelAdmin):
    model = Article

    search_fields = ['title',]
    list_display = ['category', 'title', 'updatedOn']
    list_filter = ['category', 'createdOn']

admin.site.register(Article, ArticleAdmin)