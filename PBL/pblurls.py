from django.urls import path
from . import views

urlpatterns = [
    path('', views.cover, name=""),
    path('Login/', views.Login, name="Login"),
    path('Register/', views.Register, name="Register"),
    path('user-home/', views.userHome, name="user-home"),
    path('logout/', views.logout, name="logout"),
    path('addpost/', views.addpost, name="addpost"),
    path('posts/', views.posts, name="posts"),
    path('About/', views.About, name="About"),


]