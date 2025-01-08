from django.contrib import admin
from .models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "thumb", "author", "created_at", "status"]
    prepopulated_fields = {"slug": ["title"]}
