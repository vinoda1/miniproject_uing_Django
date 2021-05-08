"""FarmProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from testapp import views
from django.conf.urls.static import static
from FarmProject.settings import *

urlpatterns = [
    path('',views.index,name='home'),
    path('index/',views.index,name='index'),
    path('upload/',views.upload,name='upload-product'),
    path('update/<int:product_id>',views.update,name='update_product'),
    path('delete/<int:product_id>',views.delete,name='delete_product'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', views.contact),
    path('About_us/',views.About_us),
    path('logout/', views.logout),
    path('success/', views.success),
    path('display/', views.detail_view),
     path('subscribe/',views.subscribe),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)
