from django.shortcuts import render
from blogs.models import Blog , Comment
from django.shortcuts import redirect
# Create your views here.


def blog_detail_view(request , id):
    blog = Blog.objects.get(id = id)
    comments = Comment.objects.filter(blog=blog)
    context = {
        "blog" : blog,
        "comments" : comments
    }

    if(request.method == "POST"):
        current_user = request.user
        comment_data = request.POST['comment']

        if(current_user.is_authenticated):
            comment = Comment(user=current_user , blog=blog , data = comment_data)
            comment.save()
        else:
            return redirect('login')

    return render(request , "blog_detail.html" , context = context)