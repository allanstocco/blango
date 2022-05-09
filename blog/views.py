from django.shortcuts import render
from blog.models import *
from django.utils import timezone

# Create your views here.

def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    print(posts)
    return render(request, "blog/index.html", {
      "posts": posts
      })