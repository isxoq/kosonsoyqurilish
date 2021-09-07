from django.urls import path
from .views import   AboutPageView,  PlaylistView, PostlistView




urlpatterns = [
    path('', PostlistView.as_view(), name='index'),
    path('dorsal/', PlaylistView.as_view(), name='dorsal'),
    path('about/', AboutPageView.as_view(), name='about'),



]