from django.shortcuts import HttpResponse  # pyright: ignore[reportMissingImports]
from django.http import HttpResponseRedirect  # pyright: ignore[reportMissingImports]

# Create your views here.

# ------------------------------------ Atividade 1 ------------------------------------

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

# Exemplo de URL: http://127.0.0.1:8000/perfil/joao
# def perfil(request, username=None):
#     if username:
#         return HttpResponse(f"Perfil do usuário: {username}".encode('utf-8'))
#     else:
#         return HttpResponse("Perfil de visitante".encode('utf-8'))

# Integração entre múltiplos aplicativos (6. Questão)

# View para slug (7. Questão)
def artigo(request, slug):
    return HttpResponse(f"Slug: {slug}".encode('utf-8')) # Exemplo de URL: http://127.0.0.1:8000/artigo/minha-postagem-de-artigo

# Questão 8: Rota hierárquica com parâmetros múltiplos
# Exemplo: /categoria/eletronicos/produto/televisor/
# def produto(request, categoria, produto):
#     return HttpResponse(f"Categoria: {categoria} - Produto: {produto}".encode('utf-8'))
# Exemplo de URL: http://127.0.0.1:8000/categoria/eletronicos/produto/televisor/

# 9. Rota para download de arquivos
# Crie uma URL que receba o nome de um arquivo e sua extensão, e exiba uma mensagem indicando
# o tipo de arquivo.
# Exemplo: /download/relatorio.pdf/ Baixando: relatorio.pdf
def download(request, nome, ext):
    return HttpResponse(f"Baixando: {nome}.{ext}".encode('utf-8'))

# Url de exemplo: http://127.0.0.1:8000/download/relatorio.pdf/

# 9. Rota para download de arquivos
# path('download/<str:nome>.<str:ext>/', views.download, name='download')

# 10. Desafio: View para miniaplicativo de blog
# Crie um app blog com as seguintes rotas:
# - /blog/ lista de posts
# - /blog/post/<int:ano>/<slug:slug>/ exibe um post específico.
# - /blog/autor/<str:nome>/ lista posts de um autor.

# def index(request):
#     return HttpResponse("Blog".encode('utf-8'))

# def post(request, ano, slug):
#     return HttpResponse(f"Post: {ano}/{slug}".encode('utf-8'))

# def autor(request, nome):
#     return HttpResponse(f"Autor: {nome.encode('utf-8')}")

# Exemplo de URL: http://127.0.0.1:8000/blog/post/2023/minha-postagem-de-artigo/

# ------------------------------------ Atividade 2 ------------------------------------

# 1. Capturando um número inteiro simples
# Crie uma rota que capture um número inteiro e o exiba em uma view.
# Exemplo: /numero/123/ → “Você digitou o número 123.”

# def mostra_numero(request, num):
#     return HttpResponse(f"Você digitou o número {num}.".encode('utf-8'))

# Exemplo de URL: http://127.0.0.1:8000/numero/123/

# 2. Capturando strings com letras e hífens
# Crie uma rota que aceite nomes de produtos compostos por letras minúsculas e hífens
# Exemplo: /produto/caixa-de-som
# Exemplo: /produto/caixa-de-som/ → “Você solicitou a caixa de som.”

def produto(request, produto):
    return HttpResponse(f"Você solicitou o produto {produto}.".encode('utf-8'))

# Exemplo de URL: http://127.0.0.1:8000/produto/caixa-de-som/

# 3. Capturando múltiplos parâmetros
# Crie uma rota que capture um nome e uma idade
# Exemplo: /usuario/joao/21/→ “O usuário joao tem 21 anos.”

def usuario(request, nome, idade):
    return HttpResponse(f"O usuário {nome} tem {idade} anos.".encode('utf-8'))

# Exemplo de URL: http://127.0.0.1:8000/usuario/joao/21/

# 4. Validando formato de datas
# Crie uma rota que aceite datas no formato YYYY-MM-DD.
# re_path(r'^agenda/(?P<data>\d{4}-\d{2}-\d{2})/$', views.agenda)
# Na view, valide o formato utilizando datetime.strptime

def agenda(request, data):
    from datetime import datetime
    try:
        data_formatada = datetime.strptime(data, '%Y-%m-%d')
        return HttpResponse(f"A data {data} é válida.".encode('utf-8'))
    except ValueError:
        return HttpResponse(f"A data {data} é inválida.".encode('utf-8'))

# Exemplo de URL: http://127.0.0.1:8000/agenda/2023-01-01/

# 5. URLs opcionais
# Crie uma rota que aceite um nome opcional na URL
# Exemplo: /perfil/ → “Visitante” /perfil/ana/ → “Usuário: ana”

# def perfil(request, nome=None):
#     if nome:
#         return HttpResponse(f"Usuário: {nome}".encode('utf-8')) # usuário Logado
#     else:
#         return HttpResponse("Visitante".encode('utf-8')) # Visitante

# Exemplo de URL: http://127.0.0.1:8000/perfil/ana/

# 6. Validando e-mails simples
# Crie uma rota que valide um e-mail recebido via URL.

def email(request, email):
    from re import match
    if match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return HttpResponse(f"E-mail {email} é válido.".encode('utf-8'))
    else:
        return HttpResponse("E-mail inválido.".encode('utf-8')) # Exemplo de e-mail inválido: joao@gmail

# URL válida: http://127.0.0.1:8000/email/joao@gmail.com/ → Mostra: "E-mail joao@gmail.com é válido."
# URL inválida: http://127.0.0.1:8000/email/joaogmail/ → Mostra: "E-mail inválido."

# 7. Rota com slugs
# Crie uma rota que aceite slugs compostos por letras, números e hífens.

def slug(request, slug):
    return HttpResponse(f"Slug: {slug}".encode('utf-8'))

# Exemplo de URL: http://127.0.0.1:8000/artigo/minha-postagem-de-artigo/

# 8. Múltiplos formatos de arquivo
# Crie uma rota que aceite apenas arquivos com extensões .pdf, .txt ou .docx

def arquivo(request, nome, ext):
    from re import match
    if match(r'^(.+)\.(pdf|txt|docx)$', f'{nome}.{ext}'):
        return HttpResponse(f"Arquivo {nome}.{ext} é válido.".encode('utf-8'))
    else:
        return HttpResponse("Arquivo inválido.".encode('utf-8'))

# Exemplo de URL: http://127.0.0.1:8000/arquivo/relatorio.pdf/
# Exemplo de URL: http://127.0.0.1:8000/arquivo/relatorio.txt/
# Exemplo de URL: http://127.0.0.1:8000/arquivo/relatorio.docx/
# Exemplo de URL: http://127

# 9. Redirecionamento condicional
# Crie uma rota que redirecione para um domínio se ele terminar com .com ou .org.

def site(request, dominio):
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect(f"https://{dominio}")

# Exemplo de URL: http://127.0.0.1:8000/site/google.com/ → Redireciona para https://google.com/
# Exemplo de URL: http://127.0.0.1:8000/site/google.org/ → Redireciona para https://google.org/
# Exemplo de URL: http://127.0.0.1:8000/site/google.

# 10. Desafio: Sistema de blog com re_path()
# Crie um app blog com as seguintes rotas:

# - /blog/ → lista de posts
# - /blog/post/<ano>/<mes>/<slug>/ → exibe um post específico

# Exemplo: /blog/post/2025/10/django-urlconf-avancado/

def post(request, ano, mes, slug):
    # Validando o ano (2000-2030)
    if not (2000 <= int(ano) <= 2030):
        return HttpResponse("Ano inválido. Deve estar entre 2000 e 2030.".encode('utf-8'))
    
    # Validando o mês (01-12)
    if not (1 <= int(mes) <= 12):
        return HttpResponse("Mês inválido. Deve estar entre 01 e 12.".encode('utf-8'))
    
    return HttpResponse(f"Post: {ano}/{mes}/{slug}".encode('utf-8'))

def blog(request):
    return HttpResponse("Lista de posts".encode('utf-8'))

# Exemplo de URL: http://127.0.0.1:8000/blog/post/2025/10/django-urlconf-avancado/
