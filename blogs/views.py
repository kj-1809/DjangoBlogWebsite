from django.shortcuts import render
from blogs.models import Blog

# Create your views here.


def blog_detail_view(request , id):
    data = Blog.objects.get(id = id)
    context = {
        "blog" : data
    }

    return render(request , "blog_detail.html" , context = context)