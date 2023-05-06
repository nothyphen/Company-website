from django.contrib import admin
from .models import Article, Category
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status', 'category_to_string')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'describtion')
    prepopulated_fields = {'slug' : ('title',)}
    ordering = ['-status', '-publish']

    def category_to_string(self, obj):
        return ", ".join([category.title for category in obj.category.all()])

admin.site.register(Article, ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Category, CategoryAdmin)