from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=100, choices=[
        ("HIPERTENSÃO","Hipertensão"),
        ("HIPOTENSÃO","Hipotensão"),
        ("ARRITMIA","Arritmia"),
        ("TAQUICARDIA","Taquicardia"),
    ])

    def __str__(self):
        return self.user.username