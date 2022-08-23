from django.urls import path
from . import views

urlpatterns = [
    path('blog-list/', views.blog_list, name='blog-list'),
    path('blog-detail/<int:id_data>/', views.blog_detail)
]
