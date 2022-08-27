from django.shortcuts import render
from blogs.models import Blog
# Create your views here.

def home_view(request):
    
    blogs = Blog.objects.all()
    # featured_blogs = Blog.objects.get(featured = True)
    # for blog in blogs:
    #     if(blog.featured):
    #         featured_blogs.append(blog)

    # print(featured_blogs)

    context = {
        "blogs" : blogs ,
        # "featured_blogs" : featured_blogs
    }
    

    
    return render(request , 'index.html' , context = context)
