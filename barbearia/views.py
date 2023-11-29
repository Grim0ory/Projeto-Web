from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def principal(request):
    return render(request,'principal.html')

def opcoes(request):
    template = loader.get_template('opcoes.html')
    if request.user.is_authenticated:
        context = {
                'user': request.user
        }
        return HttpResponse(template.render(context, request))
    
    return HttpResponse(template.render())