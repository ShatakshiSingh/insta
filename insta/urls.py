"""insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from main import views
from insta import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.post,name='post'),
    url(r'^signup',views.signup,name='signup'),
    url(r'^login/$',auth_views.login,name='login'),
    url(r'^logout$',auth_views.logout,name ='logout'),
    url(r'^custom_logout/$',views.custom_logout,name='custom_logout'),
    url(r'^like_post/$',views.update_post_likes,name='like_post'),
    url(r'postform',views.postform,name='postform'),
    url(r'^search',views.ajax_search,name='search'),
    url(r'gallery',views.gallery,name='gallery'),


]

if settings.DEBUG:
    urlpatterns+=[url(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})]
