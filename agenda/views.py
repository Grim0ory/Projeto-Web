from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from django.template import loader
from barbearia.models import Barbeiro
from barbearia.models import Servico
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Agenda
from datetime import datetime
from datetime import date

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')

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
        
        data_string = request.POST.get('date')
        data = datetime.strptime(data_string, "%Y-%m-%d").date()
        horario_string = request.POST.get('time')
        horario = datetime.strptime(horario_string, "%H:%M").time()
        data_hoje = date.today()
        hora = datetime.now().time()

        
        agenda = Agenda.objects.filter(data=data, horario=horario).first()
        if agenda or (data < data_hoje) or (data == data_hoje and horario < hora):
            messages.error(request, "Data e Horário não disponiveis!")
            return HttpResponseRedirect('/opcoes')
        
        agenda = Agenda(usuario=user, barbeiro=barbeiro, servico=servico, data=data_string, horario=horario_string)
        
        agenda.save()

        messages.success(request, "Agendamento concluido com sucesso!")
            
        return HttpResponseRedirect('/opcoes')

@login_required(login_url="/auth/login")
def agenda(request):
    template = loader.get_template('agenda.html')
    user = request.user
    user_id = user.id
    agenda = Agenda.objects.filter(usuario_id=user_id).values()
    data_hoje = date.today()
    context = {
        'user':user.username,
        'agenda':agenda,
        'data_hoje':data_hoje
    }
    
    return HttpResponse(template.render(context, request))
