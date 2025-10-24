from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    # Página inicial de pedidos
    path('', views.index, name='index'),
    # Página de detalhes de um pedido específico
    path('<int:pedido_id>/', views.detail, name='detail'),
]