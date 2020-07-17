
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subscribe/',include('subscribe.urls')),
    path('register/',include('form.urls')),
    path('upload/',include('profile_maker.urls')),
    path('',include('home.urls')),
    path('ajax/',include('post.urls')),
]
