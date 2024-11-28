"""sample01 URL Configuration

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
from myapp import views
from django.urls import re_path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('serach_list/', views.serach_list),
    path('search_name/', views.search_name),
    path('index/',views.index),
    path('post1/',views.post1),
    path('edit1/<int:id>/<str:mode>/', views.edit1),
    path('edit2/<int:id>/', views.edit2),
    path('delete/<int:id>/', views.delete),
    re_path(r'^.*$', views.index),  # 匹配所有未匹配的路徑，導向 index
    
]
