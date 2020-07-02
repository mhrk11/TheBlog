from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView


class BookPageView(ListView):
    model=Book
    template_name='book.html'
    context_object_name='books_list'

class BookDetailView(DetailView):
    model=Book
    template_name="book_detail.html"


# Create your views here.
