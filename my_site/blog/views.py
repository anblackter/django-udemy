from datetime import date
from django.shortcuts import render
from .models import Post

def get_date(post):
    return post['date']

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-date')[:3]
    return render(request, "blog/index.html", {"posts": posts})

def posts(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, "blog/all-posts.html",  {"all_posts": posts})

def post_detail(request, slug):
    identified_post = Post.objects.get(slug=slug)
    return render(request, "blog/post-detail.html", {'post': identified_post})
