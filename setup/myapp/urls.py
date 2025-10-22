from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    # path('', views.home, name='home'),
    # Url personalizada com nome de usuário
    path('saudacao/<str:nome>/', views.saudacao, name='saudacao'),
]
