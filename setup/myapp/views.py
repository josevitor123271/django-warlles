from django.shortcuts import HttpResponse

# Create your views here.

# view simples de saudação (1. Questão)
# def home(request):
#     return HttpResponse("Olá, mundo! Seja bem vindo ao meu site!")

# view simples de saudação (2. Questão)
# def saudacao(request, nome):
#     return HttpResponse(f"Olá, {nome}! Seja bem vindo ao meu site!")

# View simples para soma de dois números (3. Questão)
# def soma(request, num1, num2):
#     return HttpResponse(f"A soma de {num1} e {num2} é {num1 + num2}")

# View para validar data (Ano e mês) (4. Questão)
# def validar_data(request, ano, mes):
#     if 1 <= mes <= 12:
#         return HttpResponse(f"A data {ano}-{mes} é válida.")
#     else:
#         return HttpResponse(f"A data {ano}-{mes} é inválida.")

# View para rotas com parâmetros opcionais (5. Questão)
# URL /perfil/ que, se receber um nome de uusário, mostre perfil do usuário, caso contrário, mostre o perfil de visitante.
# Dica: usa kwargs ou uma lógica condicional
def perfil(request, username=None):
    if username:
        return HttpResponse(f"Perfil do usuário: {username}")
    else:
        return HttpResponse("Perfil de visitante")