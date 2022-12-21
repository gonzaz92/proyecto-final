from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from ejemplo_dos.models import Post
from ejemplo_dos.forms import UsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def index(request):
    return render(request, 'ejemplo_dos/index.html', {})

class PostDetalle(DetailView):
    model = Post

class PostList(ListView):
    model = Post

class PostCrear(LoginRequiredMixin,CreateView):
    model = Post
    success_url = reverse_lazy('ejemplo-dos-listar')
    fields = '__all__'

class PostBorrar(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('ejemplo-dos-listar')

class PostActualizar(LoginRequiredMixin,UpdateView):
    model = Post
    success_url = reverse_lazy('ejemplo-dos-listar')
    fields = '__all__'

class UserSingUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('ejemplo-dos-listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('ejemplo-dos-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('ejemplo-dos-index')
