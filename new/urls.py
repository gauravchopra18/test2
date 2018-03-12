from django.urls import path

from . import views

urlpatterns = [

    path('register/', views.register.as_view(), name='register'),
    path('profile/',views.Profile,name='Profile'),
    path('/', views.performs.as_view(),name='perform'),
    path('details/',views.details,name='details'),
    path('connect/',views.connect.as_view(),name='connect'),
    path('newjoin/', views.newjoin.as_view(), name='newjoin'),




]
