from django.contrib import admin
from django.urls import path, include
from monitoramento.views import UsuariosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuarios', UsuariosViewSet, basename='Usuarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]