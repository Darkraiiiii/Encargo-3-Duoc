from django.shortcuts import render, redirect
from .models import *
from .forms import AnimalForm, RegistroUserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def dos(request):
    animales = Animal.objects.raw('Select * from vehiculos_animal')
    datos ={'animalitos':animales}
    return render(request, 'dos.html', datos)
    
    
    '''
    vehiculos=Vehiculo.objects.all()    #obtenemos todos los obj de la clase Vehiculo
    datos={'autitos' : vehiculos}     #creamos diccionario que recibe la colección de objetos
    return render(request, 'dos.html', datos)   #enviamos parámetro al template
    '''

@login_required
def crear(request):
    if request.method=='POST':
        animalform = AnimalForm(request.POST, request.FILES)
        if animalform.is_valid():
            animalform.save()     #similar al insert en función
            return redirect('dos')
    else:
        animalform=AnimalForm()
    return render(request, 'crear.html',{'animalform': AnimalForm})

@login_required
def eliminar(request, id):
    AnimalEliminado=Animal.objects.get(numero=id)  #obtenemos un objeto por su pk
    AnimalEliminado.delete()
    return redirect('dos')

@login_required
def modificar(request,id):
    animal = Animal.objects.get(numero=id)         #obtenemos un objeto por su pk
    datos ={
        'form':AnimalForm(instance=animal)
    }
    if request.method=='POST':
        formulario = AnimalForm(data=request.POST, instance=animal, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            return redirect ('dos')
    return render(request, 'modificar.html', datos)

#método que permite registrar un usuario
def registrar(request):
    data = {
        'form' : RegistroUserForm()         #creamos un objeto de tipo forms para user
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data = request.POST)  
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"],
                password=formulario.cleaned_data["password1"])
            login(request,user)   
            return redirect('index')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)


def mostrar(request):
    animalitos = Animal.objects.all()
    datos={
        'animalitos': animalitos
    }
    return render(request,'mostrar.html',datos)

def vision(request):
    return render(request, 'vision.html')