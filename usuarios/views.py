from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
    if user:
        return HttpResponseRedirect('../admin')
    else:
        return HttpResponseRedirect('login')
    
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponseRedirect('cadastro')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        
        return HttpResponseRedirect('login')
            
        
