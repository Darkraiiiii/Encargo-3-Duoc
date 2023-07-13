from django.urls import path
from .views import index,dos,crear,eliminar,modificar, registrar,mostrar,vision, generarBoleta,agregar_producto,eliminar_producto,restar_producto,limpiar_carrito

urlpatterns=[ 
    path('', index, name="index"),
    path('dos/',dos, name="dos"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/', registrar, name="registrar"),
    path('mostrar/', mostrar, name="mostrar"),
    path('vision/', vision, name="vision"),

    path('mostrar/',mostrar, name="mostrar"),
    path('mostrar/',mostrar, name="mostrar"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
    
]