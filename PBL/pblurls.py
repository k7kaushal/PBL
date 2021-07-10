from django.urls import path
from . import views

urlpatterns = [
    path('', views.cover, name=""),
    path('Login/', views.Login, name=""),
    path('Register/', views.Register, name=""),

]