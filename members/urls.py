from django.urls import path
from .views import UserRegosterView
urlpatterns = [
    #path('',views.home,name="home"),
    path('register/',UserRegosterView.as_view(),name="register"),

]
