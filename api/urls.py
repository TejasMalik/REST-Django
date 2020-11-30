from django.urls import path
from api import views


urlpatterns = [
    path('user/', views.usersApi),
    path('articles/', views.articleApi),
    path('createArticle/', views.createArticleApi),
    path('classArticle/', views.ArticleList.as_view()),
    path('classArticle/<int:pk>', views.ArticleDetail.as_view())
]