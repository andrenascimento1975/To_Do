from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SubGrupo(models.Model):
    nome_subgrupo = models.CharField(max_length=100, null=False, blank=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True, blank=True, related_name=subgrupo)

    def __str__(self):
        return self.nome_subgrupo

class Grupos(models.Model):
    nome_grupo = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return self.nome_grupo

class Tags(models.Model):
    tag = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.tag

class Tarefa(models.Model):
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE, null=True, blank=True)
    subgrupo = models.ForeignKey(SubGrupo, on_delete=models.CASCADE, null=True, blank=True, related_name=tarefa_subgrupo)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']