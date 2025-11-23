from django.urls import path
from galeria.views import index, imagem, buscar, login, logout

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>/', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]