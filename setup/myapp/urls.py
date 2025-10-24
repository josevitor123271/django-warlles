from django.urls import path, re_path, include
from . import views

app_name = 'myapp'

urlpatterns = [

    # ------------------------------------ Atividade 1 ------------------------------------

    # Objetivo: Explorar o uso do objeto path() no arquivo urls.py para definir rotas dinâmicas e parametrizadas
    # em projetos Django. Os exercícios envolvem desde a criação de URLs básicas até a passagem de
    # # múltiplos parâmetros e integração com views

    # 1. Questão
    # path('', views.home, name='home'),
    
    # 2. Questão
    # Url personalizada com nome de usuário
    # path('saudacao/<str:nome>/', views.saudacao, name='saudacao'),

    # 3. Questão
    # path('soma/<int:num1>/<int:num2>/', views.soma, name='soma'),

    # 4. Questão: Validação de data (Ano e mês)
    # path('data/<int:ano>/<int:mes>/', views.validar_data, name='validar_data')

    # 5. Questão: Rotas com parâmetros opcionais
    # path('perfil/', views.perfil, name='perfil'),
    # path('perfil/<str:username>/', views.perfil, name='perfil_nomeado'),
    # Exemplo: http://localhost:8000/perfil/leo/ (leo é o nome do usuário)

    # 6. Questão: Integração entre múltiplos aplicativos
    # path('clientes/', include('clientes.urls')),
    # path('pedidos/', include('pedidos.urls'))

    # 7. Capturando slugs de artigos
    # Crie uma rota /artigo/<slug:slug>/ para exibir o título de um artigo. Exemplo: /artigo/djangopara-iniciantes/
    # path('artigo/<slug:slug>/', views.artigo, name='artigo')

    # 8. Rota hierárquica com parâmetros múltiplos
    # path('categoria/<str:categoria>/produto/<str:produto>/', views.produto, name='produto')

    # 9. Rota para download de arquivos
    # path('download/<str:nome>.<str:ext>/', views.download, name='download')

    # 10. Desafio: miniaplicativo de blog
    # Crie um app blog com as seguintes rotas:
    # - /blog/ lista de posts
    # - /blog/post/<int:ano>/<slug:slug>/ exibe um post específico.
    # - /blog/autor/<str:nome>/ lista posts de um autor.
    
    # path('blog/', views.index, name='blog_index'),
    # path('blog/post/<int:ano>/<slug:slug>/', views.post, name='post'),
    # path('blog/autor/<str:nome>/', views.autor, name='autor'),

    # Conceitos explorados
    # • Utilização de path() e parâmetros dinâmicos.
    # • Integração de múltiplos apps com include().
    # • Uso de tipos de conversores: int, str, slug.
    # • Organização de rotas complexas.
    # • Boas práticas de legibilidade e modularização em Django

    # ------------------------------------- Atividade 2 ------------------------------------
    # Objetivo: Explorar a criação de rotas dinâmicas e expressões regulares em Django, utilizando o
    # objeto re_path() no arquivo urls.py.

    # 1. Capturando um número inteiro simples
    # Crie uma rota que capture um número inteiro e o exiba em uma view.
    # Exemplo: /numero/123/ → “Você digitou o número 123.”

    # re_path(r'^numero/(?P<num>\d{1,5})/$', views.mostra_numero)

    # 2. Capturando strings com letras e hífens
    # Crie uma rota que aceite nomes de produtos compostos por letras minúsculas e hífens
    # Exemplo: /produto/caixa-de-som
    # Exemplo: /produto/caixa-de-som/ → “Você solicitou a caixa de som.”

    # re_path(r'^produto/(?P<produto>[a-z-]+)/$', views.produto),

    # 3. Capturando múltiplos parâmetros
    # Crie uma rota que capture um nome e uma idade
    # Exemplo: /usuario/joao/21/→ “O usuário joao tem 21 anos.”

    # re_path(r'^usuario/(?P<nome>[a-z]+)/(?P<idade>\d{1,2})/$', views.usuario),

    # 4. Validando formato de datas
    # Crie uma rota que aceite datas no formato YYYY-MM-DD.
    # re_path(r'^agenda/(?P<data>\d{4}-\d{2}-\d{2})/$', views.agenda)
    # Na view, valide o formato utilizando datetime.strptime

    # re_path(r'^agenda/(?P<data>\d{4}-\d{2}-\d{2})/$', views.agenda);

    # 5. URLs opcionais
    # Crie uma rota que aceite um nome opcional na URL
    # Exemplo: /perfil/ → “Visitante” /perfil/ana/ → “Usuário: ana”

    # re_path(r'^perfil/(?P<nome>[a-z]+)?/?$', views.perfil)

    # 6. Validando e-mails simples
    # Crie uma rota que valide um e-mail recebido via URL.

    # re_path(r'^email/(?P<email>[\w\.-]+@[\w\.-]+\.\w{2,4})/$', views.email)

    # 7. Rota com slugs
    # Crie uma rota que aceite slugs compostos por letras, números e hífens.

    # re_path(r'^artigo/(?P<slug>[-\w]+)/$', views.slug)

    # 8. Múltiplos formatos de arquivo
    # Crie uma rota que aceite apenas arquivos com extensões .pdf, .txt ou .docx

    # re_path(r'^arquivo/(?P<nome>[\w-]+)\.(?P<ext>pdf|txt|docx)/$', views.arquivo)

    # 9. Redirecionamento condicional
    # Crie uma rota que redirecione para um domínio se ele terminar com .com ou .org.

    # re_path(r'^site/(?P<dominio>[\w-]+\.(com|org))/$', views.site)

    # 10. Desafio: Sistema de blog com re_path()
    # Crie um app blog com as seguintes rotas:

    # - /blog/ → lista de posts
    # - /blog/post/<ano>/<mes>/<slug>/ → exibe um post específico

    # Exemplo: /blog/post/2025/10/django-urlconf-avancado/
    
    re_path(r'^blog/post/(?P<ano>\d{4})/(?P<mes>\d{2})/(?P<slug>[-\w]+)/$', views.post)

    # Conceitos explorados
    # • Expressões regulares no Django
    # • Uso de re_path() com parâmetros nomeados
    # • Rotas opcionais e múltiplos padrões
    # • Redirecionamentos e validações
    # • Boas práticas de legibilidade em padrões RegEx

]