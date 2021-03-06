"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from blog import views as blog_view
from django.conf.urls import include
from django.urls import re_path
from . import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_view.Index.as_view()),
    path('category/<int:category>', blog_view.CategoryList.as_view(), name='category'),
    path('search/', blog_view.Search.as_view(), name='search'),
    path('detail/<int:pk>', blog_view.ArticleDetail.as_view(), name='detail'),
    path('comment/', blog_view.pub_comment, name='comment'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('upload/', blog_view.image_upload),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
