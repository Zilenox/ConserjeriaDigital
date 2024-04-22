from django.urls import path
from . import views

urlpatterns = [
    path('', views.Paquetes_list),
    path('salir',views.Salir,name = "salir"),
    
    path('AgregarPaquete/', views.AgregarPaquetes),
    path('AgregarUsuario/',views.AgregarUsuarios),
    path('AgregarConserje/',views.AgregarConserje),

    path('GestionPaquetes/', views.Paquetes_list),
    path('GestionUsuarios/', views.User_list),
    path('GestionConserjes/', views.Conserjes_list),

    path('eliminarUsuario/<RutPersona>',views.EliminarUsuario),
    path('editarUsuario/<RutPersona>',views.EditarUsuario),
    path('EditUser/',views.EditUser),

    path('eliminarConserje/<RutPersona>',views.EliminarUsuario),
    path('editarConserje/<RutPersona>',views.EditarConserje),
    path('EditConserje/',views.EditConserje),

    path('eliminarPaquete/<identificador>',views.EliminarPaquete),
    path('editarPaquete/<identificador>',views.EditarPaquete),
    path('EditPaquete/',views.EditPaquete)
]



