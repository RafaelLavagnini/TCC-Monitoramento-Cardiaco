from django.db import models

class Usuario(models.Model):
    CLASSIFICACAO = (
        ('1', 'Bom'),
        ('2', 'Regular'),
        ('3', 'Grave')
    )
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    doenca = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    diagnostico = models.CharField(max_length=1, choices=CLASSIFICACAO, blank=False, null=False,default='1')

    def __str__(self):
        return self.nome