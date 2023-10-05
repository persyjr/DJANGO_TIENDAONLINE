from django.shortcuts import render
from .models import Post
# Create your views here.
def blogVR(request):
    posts=Post.objects.all()
    print(posts)
    return render(request,'blog\\blog.html',{"posts":posts })