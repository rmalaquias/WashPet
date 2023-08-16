from django.shortcuts import render
from reserva.forms import ReservaForm
from base.forms import contatoForm


def criar_reserva(request):
    form = ReservaForm (request.POST or None)
    sucesso = False
    if form.is_valid():
        form.save()
        sucesso=True
    contexto = {
        'form':form,
        'sucesso':sucesso,
    }
    return render (request, 'criar_reserva.html', contexto)

def contato(request):
    sucesso = False 
    form = contatoForm (request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
                              
    contexto = {
        'telefone': '(14)9.9824.6259',
        'responsavel': 'Rafael Malaquias', 
        'form':form,
        'sucesso':sucesso
    }

    return render(request, 'contato.html',contexto)

