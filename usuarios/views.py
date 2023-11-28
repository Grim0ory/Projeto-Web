from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as login_django

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('senha')
        user = authenticate(username=username, password=password)
    if user:
        login_django(request, user)
        return HttpResponseRedirect('../opcoes')
    else:
        return HttpResponseRedirect('login')
    
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponseRedirect('cadastro')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponseRedirect('login')
            
        
