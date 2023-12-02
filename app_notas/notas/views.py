from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from .models import Nota
from .models import Usuario
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .forms import NewUserForm
from .forms import notaForm

def notas(request):
    notas_usuario = Nota.objects.filter(usuario=request.user.id)
    return notas_usuario

def index(request):
    notas_usuario = notas(request)
    context = {"notas": notas_usuario}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def registro(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request,user)
            messages.success(request, "Registro Exitoso")
            return redirect('index')
        messages.error(request,"No fue posible el Registro. Información Invalida")
    form = NewUserForm()
    context = {"register_form":form}
    template = loader.get_template("register.html")
    return HttpResponse(template.render(context,request))


def eliminarnota(request, id):
    template = loader.get_template('eliminarnota.html')
    obj = get_object_or_404(Nota, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('index')
    context = {}
    return HttpResponse(template.render(context, request))

def nuevanota(request):
    #Obtener el template
    template = loader.get_template("nuevanota.html")
    #Generar Formulario
    nuevo_usuario = Usuario(
        nombre_completo='Nombre Completo',
        correo='correo@example.com',
        contrasena='contraseña123',
        nombre_usuario='nombre_de_usuario')
    nuevo_usuario.save()

    if request.method == "POST":
        form = notaForm(request.POST or None, request.FILES)
        if form.is_valid():
            nota_nuevo = form.save(commit=False)
            nota_nuevo.fecha_creacion = datetime.now()
            nota_nuevo.usuario = request.user
            nota_nuevo.save()
            return redirect('index')
    else:
        form = notaForm()
    #Crear contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))
    
def editarnota(request, id):
    template = loader.get_template('editarnota.html')
    obj = get_object_or_404(Nota, id=id)
    form = notaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {}
    context['form'] = form
    return HttpResponse(template.render(context, request))

def vernota(request, id):
    nota = Nota.objects.get(id=id)
    context = {'nota':nota}
    template = loader.get_template('vernota.html')
    return HttpResponse(template.render(context, request))