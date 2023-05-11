from django.urls import path, include
from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', views.ArticleList.as_view(), name="Article-List"),
    path('<int:pk>/', views.ArticleDetail.as_view(), name="Article-Detail"),
    path('user/', views.UserList.as_view(), name="User-List"),
    path('user/<int:pk>/', views.UserDetail.as_view(), name="User-Detail"),
]