from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('admin/', admin.site.urls),
    # Users
    path('users/', include(('users.urls', 'users'), namespace='users')),  
]
