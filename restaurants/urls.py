from django.urls import path, include

from . import views
urlpatterns = [
    path('feed/eating',views.index, name='feed_index'),
]