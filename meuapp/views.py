from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def cadastro(request):
    nome_cadastrado = None
    msg = None
    logado = False

    if request.method == "POST":
        # Se for para apagar todos os usuários
        if "apagar_usuarios" in request.POST:
            User.objects.all().delete()
            msg = "Todos os usuários foram apagados."
        else:
            # Cadastro de novo usuário
            user = request.POST.get("user")
            senha = request.POST.get("senha")

            if User.objects.filter(username=user).exists():
                msg = "Usuário já existe"
            else:
                novo_usuario = User.objects.create_user(
                    username=user,
                    password=senha
                )
                novo_usuario.save()
                nome_cadastrado = user
                logado = True

    # Buscar a lista de usuários **depois de qualquer ação**
    usuarios = User.objects.all()

    return render(request, "meuapp/index.html", {
        "nome_cadastrado": nome_cadastrado,
        "msg": msg,
        "usuarios": usuarios,
        "logado": logado,
    })