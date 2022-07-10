import os

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse

from .turingmachine import turing_machine
from .automatos import verificar_automato
from .models import TM
from .forms import TMForm
from .forms import SequenciaTMForms
from .models import AFD
from .forms import AFDForm
from .forms import SequenciaForm
from .imagesgeneration import desenha_automato, desenha_turing

from django.core.files.storage import FileSystemStorage
import json

def introducao(request):
    return render(request, 'website/introducao.html')

def afd(request):
    context = {'afds': AFD.objects.all()}
    return render(request, 'website/afd.html', context)

def turing(request):
    context = {'tms': TM.objects.all()}
    return render(request, 'website/turing.html', context)

def option_afd_view(request):
    return render(request, 'website/optionafd.html')

def novo_afd_view(request):
    form = AFDForm(request.POST or None)
    if form.is_valid():
        form.save()
        descricao = form.data.get('descricao'); estados = form.data.get('estados')
        estadoInicial = form.data.get('estadoinicial'); estadosdeaceitacao = form.data.get('estadosdeaceitacao'); tabeladetransicoes = form.data.get('tabeladetransicoes')
        desenha_automato(descricao, estados, estadoInicial, estadosdeaceitacao, tabeladetransicoes)
        return HttpResponseRedirect(reverse('website:afd'))

    context = {'form': form}

    return render(request, 'website/novoafd.html', context)

def json_afd_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        with open(name, 'r') as json_file:
            data = json.load(json_file)
        os.remove(name)
        if AFD.objects.all().count() == 0:
            ID = 1
        else:
            ID = AFD.objects.all()[AFD.objects.all().count() - 1].id + 1
        descricao = data['descricao']
        alfabeto = data['alfabeto']
        estados = data['estados']
        estadoinicial = data['estadoinicial']
        estadosdeaceitacao = data['estadosdeaceitacao']
        tabeladetransicoes = data['tabeladetransicoes']

        form = AFD(ID,descricao,alfabeto,estados,estadoinicial,estadosdeaceitacao,tabeladetransicoes)
        form.save()
        desenha_automato(descricao, estados, estadoinicial, estadosdeaceitacao, tabeladetransicoes)
        return HttpResponseRedirect(reverse('website:afd'))
    return render(request, 'website/jsonafd.html')

def edita_afd_view(request, afd_id):
    afd = AFD.objects.get(id=afd_id)
    form = AFDForm(request.POST or None, instance=afd)
    name = afd.descricao

    if form.is_valid():
        form.save()
        os.remove('website/static/website/images/' + name + '.svg')
        descricao = form.data.get('descricao')
        estados = form.data.get('estados')
        estadoInicial = form.data.get('estadoinicial')
        estadosdeaceitacao = form.data.get('estadosdeaceitacao')
        tabeladetransicoes = form.data.get('tabeladetransicoes')
        desenha_automato(descricao, estados, estadoInicial, estadosdeaceitacao, tabeladetransicoes)
        return HttpResponseRedirect(reverse('website:afd'))

    context = {'form': form, 'afd_id': afd_id}
    return render(request, 'website/edita.html', context)


def apaga_afd_view(request, afd_id):
    name = AFD.objects.get(id=afd_id).descricao
    AFD.objects.get(id=afd_id).delete()
    os.remove(name + '.svg')
    return HttpResponseRedirect(reverse('website:afd'))

def detalhes_afd_view(request, afd_id):
    automato = {'detalhes': AFD.objects.get(id=afd_id)}
    return render(request, 'website/detalhes.html', automato)

def sequencia_afd_view(request, afd_id):
    resultado = sequencia = None

    if request.POST:
        form = SequenciaForm(request.POST)
        if form.is_valid():
            sequencia = form.cleaned_data['sequencia']
            try:
                resultado = verificar_automato(sequencia, afd_id)
            except:
                resultado = "sequencia inválida"

    form = SequenciaForm(None)

    context= {
        'form': form,
        'resultado': resultado,
        'sequencia': sequencia
    }
    return render(request, 'website/sequencia.html', context)

def option_tm_view(request):
    return render(request, 'website/optiontm.html')

def novo_tm_view(request):
    form = TMForm(request.POST or None)
    if form.is_valid():
        form.save()
        descricao = form.data.get('descricao')
        estados = form.data.get('estados')
        estadoInicial = form.data.get('estadoinicial')
        estadodeaceitacao = form.data.get('estadodeaceitacao')
        tabeladetransicoes = form.data.get('tabeladetransicoes')
        desenha_turing(descricao, estados, estadoInicial, estadodeaceitacao, tabeladetransicoes)
        return HttpResponseRedirect(reverse('website:turing'))

    context = {'form': form}

    return render(request, 'website/novotm.html', context)

def json_tm_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        with open(name, 'r') as json_file:
            data = json.load(json_file)
        os.remove(name)
        if TM.objects.all().count() == 0:
            ID = 1
        else:
            ID = TM.objects.all()[TM.objects.all().count() - 1].id + 1
        descricao = data['descricao']
        estados = data['estadostm']
        estadoinicial = data['estadoinicial']
        estadodeaceitacao = data['estadodeaceitacao']
        tabeladetransicoes = data['tabeladetransicoes']

        form = TM(ID,descricao,estados,estadoinicial,estadodeaceitacao,tabeladetransicoes)
        form.save()
        desenha_turing(descricao,estados,estadoinicial,estadodeaceitacao,tabeladetransicoes)
        return HttpResponseRedirect(reverse('website:turing'))
    return render(request, 'website/jsontm.html')

def edita_tm_view(request, tm_id):
    tm = TM.objects.get(id=tm_id)
    form = TMForm(request.POST or None, instance=tm)
    name = tm.descricao

    if form.is_valid():
        form.save()
        os.remove('website/static/website/images/' + name + '.svg')
        descricao = form.data.get('descricao')
        estados = form.data.get('estados')
        estadoInicial = form.data.get('estadoinicial')
        estadodeaceitacao = form.data.get('estadodeaceitacao')
        tabeladetransicoes = form.data.get('tabeladetransicoes')
        desenha_turing(descricao, estados, estadoInicial, estadodeaceitacao, tabeladetransicoes)
        return HttpResponseRedirect(reverse('website:turing'))

    context = {'form': form, 'tm_id': tm_id}
    return render(request, 'website/editatm.html', context)

def apaga_tm_view(request, tm_id):
    name = TM.objects.get(id=tm_id).descricao
    TM.objects.get(id=tm_id).delete()
    os.remove(name + '.svg')
    return HttpResponseRedirect(reverse('website:turing'))

def detalhes_tm_view(request, tm_id):
    machine = {'detalhes': TM.objects.get(id=tm_id)}
    return render(request, 'website/detalhestm.html', machine)

def sequencia_tm_view(request, tm_id):
    resultado = sequencia = None

    if request.POST:
        form = SequenciaTMForms(request.POST)
        if form.is_valid():
            sequencia = form.cleaned_data['sequenciaTM']
            resultado = turing_machine(sequencia, tm_id)

    form = SequenciaTMForms(None)

    context = {
        'form': form,
        'resultado': resultado,
        'sequencia': sequencia
    }
    return render(request, 'website/sequenciatm.html', context)

#def exportjson_afd_view(request, afd_id):
#    Objeto = AFD.objects.get(id=afd_id)
#   Dic = {'descricao':Objeto.descricao,'alfabeto':Objeto.alfabeto,'estados':Objeto.estados,'estadoinicial':Objeto.estadoinicial, 'estadosdeaceitacao': Objeto.estadosdeaceitacao, 'tabeladetransicoes':Objeto.tabeladetransicoes}
#    return JsonResponse(Dic, safe=True,)
