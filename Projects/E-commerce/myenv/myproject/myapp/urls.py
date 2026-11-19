"""
URL configuration for myproject project.

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
from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
        path('', views.index, name='index'),
        path('index/', views.index, name='index'),
        path('sindex/', views.sindex, name='sindex'),
        path('about/', views.about, name='about'),
        path('CPass/', views.CPass, name='CPass'),
        path('scpass/', views.scpass, name='scpass'),
        path('Signup/', views.Signup, name='Signup'),
        path('Login/', views.Login, name='Login'),
        path('Logout/', views.Logout, name= 'Logout'),
        path('FPass/', views.FPass, name= 'FPass'),
        path('OTP/', views.OTP, name= 'OTP'),
        path('New_Pass/', views.New_Pass, name= 'New_Pass'),
        path('CProfile/', views.CProfile, name= 'CProfile'),
        path('add/', views.add, name= 'add'),
        path('view/', views.view, name='view'),
        path('update/<int:pk>', views.update, name='update'),
        path('delete/<int:pk>', views.delete, name='delete'),
        path('mdetails/<int:pk>', views.mdetails, name= 'mdetails'),
        path('addwish/<int:pk>/', views.addwish, name= 'addwish'),
        path('wishlist/', views.wishlist, name= 'wishlist'),
        path('dwishlist/<int:pk>', views.dwishlist, name= 'dwishlist'),
        path('cart/', views.cart, name='cart'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)