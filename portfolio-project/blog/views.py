from django.shortcuts import render
from .models import Blog

def bloghome(request):
    blogs = Blog.objects
    return render(request,'blog/allblogs.html',{'blogs':blogs})
def viewdetails1(request):
    blogs = Blog.objects
    return render(request,'blog/viewdetails1.html',{'blogs':blogs})
