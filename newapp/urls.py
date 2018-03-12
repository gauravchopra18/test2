from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from new.views import HomePageView
urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('', include('new.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('submit/',include('new.urls')),
    path('', HomePageView.as_view()),
    path('performs', include('new.urls')),
    path('profile/',include('new.urls')),


]