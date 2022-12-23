from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from ejemplo_dos.models import Post, Avatar, Mensaje
from ejemplo_dos.forms import UsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User

def index(request):
    posts = Post.objects.order_by('-publicado_el').all()
    return render(request, 'ejemplo_dos/index.html', {'posts': posts})

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

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('ejemplo-dos-listar')

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('ejemplo-dos-listar')

class MensajeDetail(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje

class MensajeCrear(LoginRequiredMixin, CreateView):
    model = Mensaje
    success_url = reverse_lazy('ejemplo-dos-mensajes-crear')
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin,DeleteView):
    model = Mensaje
    success_url = reverse_lazy('ejemplo-dos-mensajes-listar')
