from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map_view, name='map'),
    path('grid/', views.grid_view, name='grid'),
    path('settings/', views.settings_view, name='settings'),
]

