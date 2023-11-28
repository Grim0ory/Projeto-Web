from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from django.template import loader
from barbearia.models import Barbeiro
from barbearia.models import Servico
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Agenda

@login_required(login_url="/auth/login")
def agendamento(request):
    if request.method == "GET":
        barbeiros = Barbeiro.objects.all().values()
        servicos = Servico.objects.all().values()
        template = loader.get_template('agendamento.html')
        context = {
            'barbeiros': barbeiros,
            'servicos': servicos
        }
        return HttpResponse(template.render(context, request))
    else:
        user = request.user
        username_barbeiro = request.POST.get('barbeiro')
        barbeiro = Barbeiro.objects.filter(username=username_barbeiro).first()
        
        titulo_servico = request.POST.get('servico')
        servico = Servico.objects.filter(titulo=titulo_servico).first()
        
        data = request.POST.get('date')
        horario = request.POST.get('time')
        
        agenda = Agenda.objects.filter(data=data, horario=horario).first()
        if agenda:
            return HttpResponse('Data ou Horario Invalido')
        
        agenda = Agenda(usuario=user, barbeiro=barbeiro, servico=servico, data=data, horario=horario)
        agenda.save()
        
        return HttpResponseRedirect('/opcoes')
        

    
