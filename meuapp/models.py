from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.hashers import make_password  # para senha segura

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('user')
        senha = request.POST.get('senha')

        if nome and senha:  
            senha_hash = make_password(senha)
            Usuario.objects.create(nome=nome, senha=senha_hash)
            return render(request, 'meuapp/index.html', {
                'nome_cadastrado': nome
            })


    return render(request, 'meuapp/index.html')
