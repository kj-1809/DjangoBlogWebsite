from django.shortcuts import render , redirect , HttpResponse
from blogs.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , logout , login
from django.contrib import messages
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


def register_view(request):
    print(request.method)
    print(request)
    
    if(request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if(password != confirm_password):
            messages.error(request, "Passwords Don't match !")
            return redirect('home')

        current_users = User.objects.filter(username = username)
        if len(current_users) == 0:
            user = User.objects.create_user(username , email , password)
            user.save()
            messages.success(request, "Successfully created user")
        else:
            messages.error(request, "User with the same username already exists. Please try again !")

        return redirect('home')
        

    return render(request , 'register.html' , context = {})

def login_view(request):
    print(request.method)


    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request , user)
            messages.success(request, "Logged in successfully")
            return redirect('home')
        else:
            messages.error(request, "Invalid Password or username! Please try again")
            return redirect('home')

    return render(request , 'login.html' , context = {})

def logout_view(request):
    logout(request)
    return redirect('home')
