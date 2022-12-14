"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage.views import home_view , register_view , login_view , logout_view
from about.views import about_view
from blogs.views import blog_detail_view
from django.conf import settings
from django.conf.urls.static import static 



admin.site.site_header = "Admin Panel"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home_view ,name = 'home'),
    path('about/' ,about_view ,name = 'about'),
    path('blogs/<int:id>' , blog_detail_view , name = 'blogs'),
    path('register/' , register_view , name = 'register'),
    path('login/' , login_view , name =  'login'),
    path('logout/' , logout_view , name = 'logout'),

] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
