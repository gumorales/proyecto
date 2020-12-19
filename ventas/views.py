from django.shortcuts import render
from .models import Post
# Create your views here.
def inicio(request):
    
    posts = Post.objects.filter()
    return render(request, 'ventas/inicio.html', {'posts':posts})