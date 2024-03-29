"""blog URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from core.views import index, show_category, read_post, register
from blog import settings
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('category/<int:category_id>/', show_category, name='category'),
    path('read/<int:post_id>/', read_post, name='read_post'),
    re_path(r'^register/$', register, name='register'),
    re_path(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    re_path(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)