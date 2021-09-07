from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Playlist, Post


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'


class PlaylistView(ListView):
    model = Playlist
    template_name = 'darslar.html'


class PostlistView(ListView):
    model = Post
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'bizhaqimizda.html'



