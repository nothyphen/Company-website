from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import Http404
# Create your views here.

def HomeBlog(request):
    articles = Article.objects.filter(status="p").order_by('-publish')

    context = {
        'articles' : articles,
    }

    return render(request, 'blog.html', context=context)

def ArticleDetail(request, slug):
    detail = get_object_or_404(Article, slug=slug, status="p")

    context = {
        'details' : detail,
    }

    return render(request, 'post.html', context=context)

def CategoryFilter(request, slug):
    category = get_object_or_404(Category, slug=slug, status=True)

    context = {
        'category' : category,
    }

    return render(request, 'category.html', context=context)