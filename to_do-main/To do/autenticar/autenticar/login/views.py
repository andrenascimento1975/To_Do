from .models import Tarefa, Grupos, Tags, SubGrupo
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect

class Logar(LoginView):
    template_name = 'login/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('grupos')

class Registrar(FormView):
    template_name = 'login/registrar.html'
    fields = '__all__'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tarefas')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Registrar, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tarefas')
        return super(Registrar, self).get(*args, **kwargs)

class Sair(LogoutView):

    def get_success_url(self):
        return reverse_lazy('login')

class ListaTarefa(LoginRequiredMixin, ListView):
    model = Tarefa
    fields = '__all__'
    context_object_name = 'tarefas'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tarefas'] = data['tarefas'].filter(user=self.request.user)
        data['count'] = data['tarefas'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            data['tarefas'] = data['tarefas'].filter(
                title__startswith=search_input)
        data['search_input'] = search_input
        return data

class TodasTarefas(LoginRequiredMixin, ListView):
    model = Tarefa
    context_object_name = 'completo'

class Detalhe(LoginRequiredMixin, DetailView):
    model = Tarefa
    context_object_name = 'tarefa'
    template_name = 'login/detalhe.html'

class Criar(LoginRequiredMixin, CreateView):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')
    template_name = 'login/formulario.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Criar, self).form_valid(form)

class Atualizar(LoginRequiredMixin, UpdateView):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')
    template_name = 'login/formulario.html'

class AtualizarGrupo(LoginRequiredMixin, UpdateView):
    model = Grupos
    fields = '__all__'
    success_url = reverse_lazy('grupos')
    template_name = 'login/formulario_grupos.html'

class Apagar(DeleteView, LoginRequiredMixin):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')
    template_name = 'login/confirmar.html'

class ApagarGrupo(DeleteView, LoginRequiredMixin):
    model = Grupos
    fields = '__all__'
    success_url = reverse_lazy('grupos')
    template_name = 'login/apagar_grupo.html'

class CriarTag(LoginRequiredMixin, CreateView):
    model = Tags
    context_object_name = 'tags'
    success_url = reverse_lazy('tags')
    fields = '__all__'
    template_name = 'login/formulario_tags.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CriarTag, self).form_valid(form)

class VisualizaGrupo(LoginRequiredMixin, ListView):
    model = Grupos
    fields = '__all__'
    context_object_name = 'criar_grupo'
    success_url = reverse_lazy('grupos')
    template_name = 'login/grupos.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VisualizaGrupo, self)

class Mostra_tarefa_grupo(LoginRequiredMixin, View):
    model = Grupos
    fields = '__all__'
    context_object_name = 'criar_grupo'
    success_url = reverse_lazy('mostra_tarefa_grupo')
    template_name = 'login/mostra_tarefa_grupo.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(mostra_tarefa_grupo, self)

class Mostra_subgrupo(LoginRequiredMixin, View):
    model = SubGrupo
    fields = '__all__'
    context_object_name = 'criar_subgrupo'
    success_url = reverse_lazy('mostra_subgrupo')
    template_name = 'login/mostra_subgrupo.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(mostra_subgrupo, self)

class CriarGrupo(LoginRequiredMixin, CreateView):
    model = Grupos
    context_object_name = 'criar_grupo'
    success_url = reverse_lazy('grupos')
    fields = '__all__'
    template_name = 'login/formulario_grupos.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CriarGrupo, self).form_valid(form)

class CriarSubGrupo(LoginRequiredMixin, CreateView):
    model = SubGrupo
    context_object_name = 'criar_subgrupo'
    success_url = reverse_lazy('subgrupos')
    fields = '__all__'
    template_name = 'login/formulario_subgrupos.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CriarSubGrupo, self).form_valid(form)