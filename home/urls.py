from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name="home"),
    path('blog/<str:id_test>/', views.blog, name="blog"),
    path('newpost/', views.newPost, name='newpost'),
    path('logout/', views.logout_user, name='logout'),



]