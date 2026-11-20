from django.db import models


class Evento(models.Model):
    titulo = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    data = models.DateField()
    local = models.CharField(max_length=120)

    def __str__(self):
        return self.titulo