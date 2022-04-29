
from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AuthorView,FollowView,SearchView
urlpatterns = [
    #path('',views.home,name="home"),
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(),name="article_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('author/<int:pk>', AuthorView, name="authorPosts"),
    path('follow/<int:pk>', FollowView, name="follow_post"),
    path('search', views.SearchView, name="searchPost"),

]
