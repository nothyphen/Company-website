from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeBlog, name='HomeBlog'),
    path('<slug:slug>/', views.ArticleDetail, name='BlogDetail'),
    path('category/<slug:slug>/', views.CategoryFilter, name='CategoryDetail'),
]