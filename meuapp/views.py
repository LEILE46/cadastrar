from django.shortcuts import render
from .models import Usuario
def Login(request):
    msg=""
    logado=False
    if request.method =="POST":
        user=request.POST.get("user")
        senha=request.POST.get("senha")
        if not user or not senha:
            msg="preencha todos os campos!"
        elif Usuario.objects.filter(nome=user,senha=senha).exists():
            msg=f"Login bem-sucedido! Bem-vindo ,{user}."
            logado=True
        else:
            msg="usuario ou senha inválidos."

    context={
        "usuarios":Usuario.objects.all(),
        "msg": msg,
        "logado":logado
    }
    return render(request,"meuapp/index.html",context)

