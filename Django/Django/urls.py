"""
URL configuration for Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib import admin
from DjangoApp import views
from DjangoApp.forms import LoginForm

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('account/register/', views.register),
    path('account/login/', LoginView.as_view(authentication_form=LoginForm)),
    path('account/', include('django.contrib.auth.urls')),
    path('users/<str:username>', views.user),
    path('categories/add', views.addCategory),
    path('categories/<int:id>', views.category),
    path('categories/<int:category_id>/posts/add', views.addPost),
    path('categories/<int:category_id>/posts/<int:post_id>', views.post),
    path('categories/<int:category_id>/posts/<int:post_id>/like/', views.likePost),
    path('categories/<int:category_id>/posts/<int:post_id>/comments/add', views.addComment),
    path('categories/<int:category_id>/posts/<int:post_id>/comments/<int:comment_id>/reply', views.addReply),
    path('categories/<int:category_id>/posts/<int:post_id>/comments/<int:comment_id>/like/', views.likeComment),
]
