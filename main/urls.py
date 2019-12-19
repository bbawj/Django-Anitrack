from django.urls import path
from . import views



app_name= 'main'
urlpatterns = [
    path('', views.home, name='main-home'),
    path('airing/', views.airing, name='main-airing'),
    path('following_ld/', views.following_ld, name='main-following_ld'),
    path('following_sd/', views.following_sd, name='main-following_sd'),
    path('following_hd/', views.following_hd, name='main-following_hd'),
    path('following_fhd/', views.following_fhd, name='main-following_fhd')
]
