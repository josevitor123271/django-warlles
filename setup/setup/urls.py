"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # pyright: ignore[reportMissingImports]
from django.urls import path, include  # pyright: ignore[reportMissingImports]
from django.conf import settings  # pyright: ignore[reportMissingImports]
from django.conf.urls.static import static  # pyright: ignore[reportMissingImports]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('clientes/', include('clientes.urls')),
    path('pedidos/', include('pedidos.urls')),
]

# Configuração para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
