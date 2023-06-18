from django.urls import path
from .views import index,dos,crear,eliminar,modificar, registrar,mostrar,vision

urlpatterns=[ 
    path('', index, name="index"),
    path('dos/',dos, name="dos"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/', registrar, name="registrar"),
    path('mostrar/', mostrar, name="mostrar"),
    path('vision/', vision, name="vision"),
    
]