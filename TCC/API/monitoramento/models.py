from django.db import models

class Usuario(models.Model):
    NIVEL = (
        ('1', 'Incial'),
        ('2', 'Controlado'),
        ('3', 'Grave')
    )
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    doenca = models.CharField(max_length=15)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False,default='1')

    def __str__(self):
        return self.nome