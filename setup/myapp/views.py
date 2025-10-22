from django.shortcuts import HttpResponse

# Create your views here.

# view simples de saudação
def saudacao(request, nome):
    return HttpResponse(f"Olá, {nome}! Seja bem vindo ao meu site!")