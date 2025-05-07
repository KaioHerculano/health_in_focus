from django.db import models

class Scheduling(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    data = models.DateField()
    especialidade = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome} - {self.data}"
