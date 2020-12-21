from django.shortcuts import render
from django.utils import timezone
from .models import consulta, Prodcto
from .models import Prodcto
from .forms import PostForm
from django.shortcuts import redirect


# Create your views here.
def principal(request):
    return render(request, 'ventas/principal.html', {})


def formulario(request):
    form = PostForm()
    return render(request, 'ventas/formulario.html', {'form': form})
        

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'ventas/formulario.html', {'form': form})    

def productos_list(request):
    productos = Prodcto.objects.order_by('Titulo')
    return render(request, 'ventas/productos_list.html', {'productos': productos})