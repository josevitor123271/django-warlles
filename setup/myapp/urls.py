from django.urls import path
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
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/<str:username>/', views.perfil, name='perfil_nomeado')
    # Exemplo: http://localhost:8000/perfil/leo/ (leo é o nome do usuário)
]
