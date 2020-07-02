from django.urls import path
from .views import BlogPageView, BlogDetailView

urlpatterns=[
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogPageView.as_view(), name='blog')
    ]
