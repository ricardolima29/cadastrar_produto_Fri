from django.shortcuts import render
from .models import Usuario
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibir os cadastros

    usuarios = {
    'usuarios': Usuario.objects.all()
    }

#retornar os dados para a pagina
    return render(request,'usuarios/usuarios.html', usuarios)