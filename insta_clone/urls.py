"""instagram_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
#from post.views import PostDetails,tags
from authy.views import UserProfile,follow,UserSearch
urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/',include('post.urls')),
    path('user/',include('authy.urls')),
    path('<username>/',UserProfile,name='profile'),
    path('<username>/follow/<option>',follow,name = 'follow'),


 #   path('', index, name='index'),
  # 	path('newpost/', NewPost, name='newpost'),
   #	path('<uuid:post_id>', PostDetails, name='postdetails'),
   	#path('<uuid:post_id>/like', like, name='postlike'),
   	#path('<uuid:post_id>/favorite', favorite, name='postfavorite'),
   	#path('tag/<slug:tag_slug>', tags, name='tags'),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
