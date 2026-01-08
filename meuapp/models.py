from django.db import models
from django.shortcuts import render
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return f"usuario = {self.nome}"


def cadastro(request):
    nome_cadastrado = None

    if request.method == 'POST':
        nome = request.POST.get('user')
        senha = request.POST.get('senha')
        Usuario.objects.create(nome=nome, senha=senha)

        nome_cadastrado = nome

    return render(request, 'cadastro.html', {
        'nome_cadastrado': nome_cadastrado
    })
