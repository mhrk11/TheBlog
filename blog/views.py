from django.shortcuts import render
from .models import post
from django.views.generic import ListView, DetailView

class BlogPageView(ListView):
    model=post
    template_name="blog.html"
    context_object_name="blogs_list"

class BlogDetailView(DetailView):
    model=post
    template_name="post_detail.html"


# Create your views here.
