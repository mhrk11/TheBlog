from django.urls import path
from .views import BookPageView, BookDetailView

urlpatterns=[
    path('books/book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/', BookPageView.as_view(), name='books')

    ]
