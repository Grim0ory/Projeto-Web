from django.http import HttpResponse
from django.shortcuts import render

def principal(request):
    return render(request,'principal.html')

def opcoes(request):
    return render(request, 'opcoes.html')