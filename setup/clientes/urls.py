from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    # Página inicial de clientes
    path('', views.index, name='index'),
    # Página de detalhes de um cliente específico
    path('<int:cliente_id>/', views.detail, name='detail'),
]