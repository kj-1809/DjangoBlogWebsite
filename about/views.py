from django.shortcuts import render

# Create your views here.
def about_view(request):

    print(request)

    context = {

    }

    return render(request , 'about.html' , context = context)
    
