from django.shortcuts import render, redirect
from .models import Animal, Boleta, detalle_boleta
from .forms import AnimalForm, RegistroUserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from vehiculos.compras import Carrito

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

def tienda(request):
    animalitos = Animal.objects.all()
    datos={
        'animalitos':animalitos
    }
    return render(request, 'mostrar.html', datos)


def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    animal = Animal.objects.get(numero=id)
    carrito_compra.agregar(animal=animal)
    return redirect('mostrar')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    animal = Animal.objects.get(numero=id)
    carrito_compra.eliminar(animal=animal)
    return redirect('mostrar')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    animal = Animal.objects.get(numero=id)
    carrito_compra.restar(animal=animal)
    return redirect('mostrar')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('mostrar')    


def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Animal.objects.get(numero = value['animal_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)