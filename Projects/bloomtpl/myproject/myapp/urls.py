"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'), 
    path('shop/', views.shop, name='shop'), 
    path('blog_single/', views.blog_single, name='blog_single'), 
    path('blog/', views.blog, name='blog'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('category/', views.category, name='category'),
    path('product_single/<int:id>/', views.product_single, name='product_single'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('category_single_product/<int:category_id>/product/<int:product_id>/', views.category_single_product, name='category_single_product'),
    path('seller_signup/', views.seller_signup, name='seller_signup'),
    path('signup/', views.buyer_signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('change-password/', views.c_pass, name='change_password'),
    path('forgot-password/', views.f_pass, name='forgot_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('create-password/', views.n_pass, name='n_pass'),
    path('seller_dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('buyer_profile/', views.buyer_profile, name='buyer_profile'),
    path('bank_account/', views.bank_account, name='bank_account'),

    
]