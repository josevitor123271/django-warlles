from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    View para a página inicial de clientes
    """
    return HttpResponse("Página inicial de clientes".encode('utf-8'))

def detail(request, cliente_id):
    """
    View para exibir detalhes de um cliente específico
    """
    return HttpResponse(f"Detalhes do cliente #{cliente_id}".encode('utf-8'))