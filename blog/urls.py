from django.urls import path
from . import views 


urlpatterns = [
    path('', views.allblogs, name='allblogs'), #they don't have to be the same name
    path('<int:blog_id>/', views.detail, name='detail'), #saves the integer given as the blog_id value in views.py when makign a request
] 