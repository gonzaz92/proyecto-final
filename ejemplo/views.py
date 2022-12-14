from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar, Juegos, Mascotas
from ejemplo.forms import Buscar, FamiliarForm, JuegosForm, MascotasForm
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request, nombre):
    return render(request,
    'ejemplo/saludar_a.html',
    {'nombre': nombre}
    )

def sumar(request, a, b):
    return render(request,
    'ejemplo/sumar.html',
    {'a': a,
    'b': b,
    'resultado': a + b}
    )

def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, 'ejemplo/familiares.html', {'lista_familiares' : lista_familiares})
    
class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con ??xito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  # prestar atenci??n ahora el method get recibe un parametro pk == primaryKey == identificador ??nico
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  # prestar atenci??n ahora el method post recibe un parametro pk == primaryKey == identificador ??nico
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualiz?? con ??xito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarFamiliar(View):
  template_name = 'ejemplo/familiares.html'
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiar = Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiar})

def mostrar_juegos(request):
    lista_juegos = Juegos.objects.all()
    return render(request, 'Juegos/juegos.html', {'lista_juegos': lista_juegos})

class Altajuego(View):
    form_class = JuegosForm
    template_name = 'Juegos/alta_juego.html'
    initial = {'nombre':'', 'tipo':''}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post (self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"El juego se cargo con ??xito {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'fomr':form,
                                                        'msg_exito': msg_exito})
        
        return render (request, self.template_name, {'form': form})

class ActualizarJuego(View):
  form_class = JuegosForm
  template_name = 'juegos/actualizar_juego.html'
  initial = {'nombre':'', 'tipo':''}
  
  def get(self, request, pk): 
      juego = get_object_or_404(Juegos, pk=pk)
      form = self.form_class(instance=juego)
      return render(request, self.template_name, {'form':form,'juego': juego})

  def post(self, request, pk): 
      juego = get_object_or_404(Juegos, pk=pk)
      form = self.form_class(request.POST ,instance=juego)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualiz?? el juego con ??xito {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': juego,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarJuego(View):
    template_name = 'Juegos/juegos.html'

    def get(self, request, pk):
        juego = get_object_or_404(Juegos, pk=pk)
        juego.delete()
        juego = Juegos.objects.all()
        return render(request, self.template_name, {'lista_juegos': juego})

def mostrar_mascotas(request):
    lista_mascotas = Mascotas.objects.all()
    return render(request, 'Mascotas/mascotas.html', {'lista_mascotas': lista_mascotas})

class AltaMascota(View):
    form_class = MascotasForm
    template_name = 'Mascotas/alta_mascotas.html'
    initial = {'nombre':'', 'especie':'', 'raza':''}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"La Mascota se cargo con ??xito {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'fomr':form,
                                                        'msg_exito': msg_exito})
        
        return render (request, self.template_name, {'form': form})

class ActualizarMascota(View):
  form_class = MascotasForm
  template_name = 'Mascotas/actualizar_mascotas.html'
  initial = {'nombre':'', 'especie':'', 'raza':''}
  
  def get(self, request, pk): 
      juego = get_object_or_404(Mascotas, pk=pk)
      form = self.form_class(instance=juego)
      return render(request, self.template_name, {'form':form,'juego': juego})

  def post(self, request, pk): 
      juego = get_object_or_404(Mascotas, pk=pk)
      form = self.form_class(request.POST ,instance=juego)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualiz?? el juego con ??xito {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': juego,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarMascota(View):
    template_name = 'Mascotas/mascotas.html'

    def get(self, request, pk):
        mascota = get_object_or_404(Mascotas, pk=pk)
        mascota.delete()
        mascota = Mascotas.objects.all()
        return render(request, self.template_name, {'lista_mascotas': mascota})

class FamiliarDetalle(DetailView):
    model = Familiar

class FamiliarList(ListView):
    model = Familiar

class FamiliarCrear(CreateView):
    model = Familiar
    success_url = '/panel-familia'
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class FamiliarBorrar(DeleteView):
    model = Familiar
    success_url = '/panel-familia'

class FamiliarActualizar(UpdateView):
    model = Familiar
    success_url = '/panel-familia'
    fields = ['nombre', 'direccion', 'numero_pasaporte']