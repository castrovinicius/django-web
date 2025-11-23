from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from galeria.models import Fotografia


@login_required(login_url='login')
def index(request):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    
    if "categoria" in request.GET:
        categoria = request.GET['categoria']
        if categoria:
            fotografias = fotografias.filter(categoria=categoria)
    
    return render(request, 'galeria/index.html', {'cards': fotografias})

@login_required(login_url='login')
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

@login_required(login_url='login')
def buscar(request):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(
                Q(nome__icontains=nome_a_buscar) | Q(categoria__icontains=nome_a_buscar)
            )

    return render(request, 'galeria/buscar.html', {'cards': fotografias})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    
    return render(request, 'galeria/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')