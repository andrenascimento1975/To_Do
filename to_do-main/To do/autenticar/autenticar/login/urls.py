from django.urls import path
from .models import Tarefa, Grupos
from .views import ListaTarefa, Criar, Atualizar, Apagar, Logar, Registrar, TodasTarefas, VisualizaGrupo, CriarGrupo, ApagarGrupo, AtualizarGrupo, CriarTag, Mostra_tarefa_grupo
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('mostra_tarefa_grupo/<int:pk>/', Mostra_tarefa_grupo.as_view(), name='mostra_tarefa_grupo'),
    path('tags/', CriarTag.as_view(), name='tags'),
    path('grupos/', VisualizaGrupo.as_view(), name='grupos'),
    path('criar_grupo/', CriarGrupo.as_view(), name='criar_grupo'),
    path('todas/', TodasTarefas.as_view(), name='completo'),
    path('login/', Logar.as_view(), name='login'),
    path('registrar/', Registrar.as_view(), name='registrar'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', ListaTarefa.as_view(), name='tarefas'),
    path('criar/', Criar.as_view(), name='criar'),
    path('atualizar/<int:pk>/', Atualizar.as_view(), name='atualizar'),
    path('atualizar_grupos/<int:pk>/', AtualizarGrupo.as_view(), name='atualizar_grupos'),
    path('apagar/<int:pk>/', Apagar.as_view(), name='apagar'),
    path('apagar_grupo/<int:pk>/', ApagarGrupo.as_view(), name='apagar_grupo'),
]
