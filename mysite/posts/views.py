from django.shortcuts import render
from .models import Post

# Create your views here.
class HomePage(ListView):
    model = Post
    template_name = 'home.html'
