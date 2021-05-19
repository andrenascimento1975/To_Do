from django.contrib import admin
from .models import Tarefa, Grupos, Tags, SubGrupo

admin.site.register(Grupos)
admin.site.register(Tags)
admin.site.register(Tarefa)
admin.site.register(SubGrupo)



# Register your models here.
