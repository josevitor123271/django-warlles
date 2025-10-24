from django.shortcuts import HttpResponse  # pyright: ignore[reportMissingImports]

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

# Exemplo de URL: http://127.0.0.1:8000/perfil/joao
def perfil(request, username=None):
    if username:
        return HttpResponse(f"Perfil do usuário: {username}".encode('utf-8'))
    else:
        return HttpResponse("Perfil de visitante".encode('utf-8'))

# Integração entre múltiplos aplicativos (6. Questão)

# View para slug (7. Questão)
def artigo(request, slug):
    return HttpResponse(f"Slug: {slug}".encode('utf-8')) # Exemplo de URL: http://127.0.0.1:8000/artigo/minha-postagem-de-artigo

# Questão 8: Rota hierárquica com parâmetros múltiplos
# Exemplo: /categoria/eletronicos/produto/televisor/
def produto(request, categoria, produto):
    return HttpResponse(f"Categoria: {categoria} - Produto: {produto}".encode('utf-8'))
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

def index(request):
    return HttpResponse("Blog".encode('utf-8'))

def post(request, ano, slug):
    return HttpResponse(f"Post: {ano}/{slug}".encode('utf-8'))

def autor(request, nome):
    return HttpResponse(f"Autor: {nome.encode('utf-8')}")

# Exemplo de URL: http://127.0.0.1:8000/blog/post/2023/minha-postagem-de-artigo/