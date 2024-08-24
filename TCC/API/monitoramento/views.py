from rest_framework import viewsets
from monitoramento.models import Usuario
from monitoramento.serializer import UsuarioSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os usuários"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer