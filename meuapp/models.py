from django.db import models
from django.shortcuts import render
from django.contrib.auth.hashers import make_password 
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return f"usuario = {self.nome}"


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
