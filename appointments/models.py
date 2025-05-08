from django.db import models

class Scheduling(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    date = models.DateField()
    time = models.TimeField()  # <-- Novo campo
    specialty = models.CharField(max_length=100)
    observations = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
