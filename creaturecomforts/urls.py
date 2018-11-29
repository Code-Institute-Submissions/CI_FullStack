"""creaturecomforts URL Configuration

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
from django.urls import path, include
from home import urls as home_urls
from home.views import index
from products import urls as products_urls
from .settings import MEDIA_ROOT
from django.views import static
from payment import urls as payment_urls
from search import urls as search_urls
from cart import urls as cart_urls
from blog import urls as blog_urls
from accounts import urls as accounts_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include(home_urls)),
    path('products/', include(products_urls)),
    path('payment/', include(payment_urls)),
    path('cart/', include(cart_urls)),
    path('search/', include(search_urls)),
    path('blog/', include(blog_urls)),
    path('accounts/', include(accounts_urls)),
    path('', index, name='index'),
]
