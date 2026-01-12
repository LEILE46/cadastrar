from django.shortcuts import render
from django.contrib.auth.models import User

def cadastro(request):
    logado = False

    if request.method == "POST":

        if "apagar_usuarios" in request.POST:
            User.objects.all().delete()
            return render(request, "meuapp/index.html", {
                "msg": "Todos os usuários foram apagados.",
                "usuarios": User.objects.all(),
                "logado": logado,
            })

        user = request.POST.get("user")
        senha = request.POST.get("senha")

        # 🔴 VALIDAÇÃO CRÍTICA
        if not user or not senha:
            return render(request, "meuapp/index.html", {
                "msg": "Usuário e senha são obrigatórios",
                "usuarios": User.objects.all(),
                "logado": logado,
            })

        if User.objects.filter(username=user).exists():
            return render(request, "meuapp/index.html", {
                "msg": "Usuário já existe",
                "usuarios": User.objects.all(),
                "logado": logado,
            })

        User.objects.create_user(
            username=user,
            password=senha
        )

        logado = True
        return render(request, "meuapp/index.html", {
            "nome_cadastrado": user,
            "usuarios": User.objects.all(),
            "logado": logado,
        })

    return render(request, "meuapp/index.html", {
        "usuarios": User.objects.all(),
        "logado": logado,
    })
