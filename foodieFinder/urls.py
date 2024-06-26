"""
URL configuration for foodieFinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from . import settings

handler404 = 'core.views.handler404'
handler500 = 'core.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('menu/',include('menu.urls')),
    path('',include('orders.urls')),
    path('restaurants/',include('restaurants.urls')),
    path('',include('reviews.urls')),
    path('users/',include('users.urls')),
    path('',include('payments.urls')),
    path('restaurants/administration/',include('admin_panel.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


