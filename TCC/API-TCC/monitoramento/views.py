from rest_framework import viewsets, generics
from monitoramento.models import Usuario
from monitoramento.serializer import UsuarioSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer