from django.urls import path
from monitoramento.views import index, imagem, execute_prediction, perfil_usuario

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('execute_prediction/', execute_prediction, name='execute_prediction'),
    path('perfil/<str:username>/', perfil_usuario, name='perfil_usuario'),
]