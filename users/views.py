from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth 
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not password == confirm_password:
            messages.add_message(
                request, constants.ERROR, 'As senhas não coincídem'
            )
            return redirect('/users/register')
        
        user = User.objects.filter(username = username)

        if user.exists():
            messages.add_message(
                request, constants.ERROR, 'Já existe um usuário com o mesmo username',
            )
            return redirect('/users/register')
        
        try:
            user = User.objects.create_user(username = username, password = password)
            
            messages.add_message(
                request, constants.SUCCESS, 'Usuário cadastrado com sucesso.'
            )

            return redirect('/users/login')
        except:
            messages.add_message(
                request, constants.ERROR, 'Erro interno do sistema'
            )
            
            return redirect('/users/register')
        

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username = username, password = password)

        if user is not None:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logado!')
            
            return redirect('/flashcard/new_flashcard/')
        else:
            messages.add_message(
                request, constants.ERROR, 'Usuário ou senha inválidos'
            )
            return redirect('/users/login')
        

def logout(request):
    auth.logout(request)
    messages.add_message(request, constants.SUCCESS, 'Deslogado!')
    return redirect('/users/login')