from django.urls import path, include  # pyright: ignore[reportMissingImports]
from . import views

app_name = 'myapp'

urlpatterns = [
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


]