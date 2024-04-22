from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from .models import User, Administrador, Conserje ,Residente ,Correspondencia
from .form import LoginForm
from django.contrib import messages
 # Create your views here.

##############################
#Vistas de LOG in-out
##############################

def log_in(request):
    return render(request, "registration/login.html")

@login_required
def Salir(request):
    logout(request)
    return redirect('/')

##############################
#Vistas de paginas de gestion
##############################

#gestion de paquetes
@login_required
def Paquetes_list(request):
    paquetes = Correspondencia.objects.all()
    personas = Residente.objects.all()
    return render(request, 'gestionPaquetes.html', {'paquetes': paquetes, 'personas': personas})

#gestion de usuarios
@login_required
def User_list(request):
    personas = Residente.objects.all()
    return render(request, 'gestionUsuarios.html', {'personas': personas})

#gestion de conserjes
@login_required
def Conserjes_list(request):
    personas = Conserje.objects.all()
    return render(request, 'gestionConserjes.html', {'personas': personas})


##############################
# Funciones para agregar objetos
##############################


@login_required
def AgregarPaquetes(request):
    numerodepto = request.POST['DEPTO[]']
    tipoEncomienda = request.POST['tipo[]']
    print(numerodepto)
    print(tipoEncomienda)
    temp_resident = Residente.objects.get(NumeroDepartamento = numerodepto)
    temp_resident.casilla += 1
    temp_resident.save()
    Correspondencia.objects.create(type = tipoEncomienda, destinatario = temp_resident)
    return redirect('../GestionPaquetes/')

@login_required
def AgregarUsuarios(request):
    name = request.POST['Nombre']
    ident = request.POST['RUT']
    apartment = request.POST['Departamento']
    N_user = User.objects.create(rut = ident , nombre = name)
    R_User = Residente.objects.create(usuario = N_user, NumeroDepartamento = apartment, casilla = 0)

    return redirect('../GestionUsuarios/')

@login_required
def AgregarConserje(request):
    name = request.POST['Nombre']
    ident = request.POST['RUT']
    R_User = Conserje.objects.create(usuario = User.objects.create(rut = ident , nombre = name))

    return redirect('../GestionConserjes/')


##############################
# Funciones de control de usuarios
##############################

@login_required
def EliminarUsuario(request,RutPersona):
    userToDelete = User.objects.get(rut = RutPersona)
    userToDelete.delete()
    messages.success(request, 'eliminado!')
    return redirect('../GestionUsuarios/')


@login_required
def EditarUsuario(request,RutPersona):
    Usuario_temp = User.objects.get(rut = RutPersona )
    userToModify = Residente.objects.get(usuario = Usuario_temp)
    return render(request, 'edicionUsuarios.html', {'userToModify': userToModify})

@login_required
def EditUser(request):
    name = request.POST['Nombre']
    ident = request.POST['RUT']
    apartment = request.POST['Departamento']

    Usuario_temp = User.objects.get(rut = ident)
    Usuario_temp.nombre = name
    ResidentToModify = Residente.objects.get(usuario = Usuario_temp)
    ResidentToModify.NumeroDepartamento= apartment
    Usuario_temp.save()
    ResidentToModify.save()

    messages.success(request, 'Usuario actualizado!')
    return redirect('../GestionUsuarios/')


##############################
# Funciones de control de conserjes
##############################

@login_required
def EliminarConserje(request,RutPersona):
    userToDelete = User.objects.get(rut = RutPersona)
    userToDelete.delete()
    messages.success(request, 'eliminado!')
    return redirect('../GestionConserjes/')

@login_required
def EditarConserje(request,RutPersona):
    ConserjeToModify = User.objects.get(rut = RutPersona )
    return render(request, 'edicionConserjes.html', {'ConserjeToModify': ConserjeToModify})

@login_required
def EditConserje(request):
    name = request.POST['Nombre']
    ident = request.POST['RUT']

    Usuario_temp = User.objects.get(rut = ident)
    Usuario_temp.nombre = name
    Usuario_temp.save()

    messages.success(request, 'Conserje actualizado!')
    return redirect('../GestionConserjes/')

##############################
# Funciones de control de Paquetes
############################## 

@login_required
def EliminarPaquete(request,identificador):
    toDelete = Correspondencia.objects.get(id = identificador)
    toDelete.destinatario.casilla -= 1
    toDelete.delete()
    messages.success(request, 'eliminado!')
    return redirect('../GestionPaquetes/')

@login_required
def EditarPaquete(request,identificador):
    ToModify = Correspondencia.objects.get(id = identificador)
    deptos = Residente.objects.all()
    return render(request, 'edicionPaquetes.html', {'ToModify': ToModify, "deptos": deptos})

@login_required
def EditPaquete(request):

    identificador = request.POST['ID']
    PRE_apartment = request.POST['PRE_apartment']
    POST_apartment = request.POST['DEPTO[]']    
    tipoPaquete = request.POST['tipo[]']

    print("PRE_apartment ",PRE_apartment)
    print("post apartment ",POST_apartment)
    paquete = Correspondencia.objects.get(id= identificador)

    if(POST_apartment != PRE_apartment):
        Residente_temp = Residente.objects.get(NumeroDepartamento = PRE_apartment)
        Residente_temp.casilla -= 1
        Residente_temp.save()
        NEW_Residente_temp = Residente.objects.get(NumeroDepartamento = POST_apartment)
        NEW_Residente_temp.casilla += 1
        NEW_Residente_temp.save()
        paquete.destinatario = NEW_Residente_temp
        print("cambio de depto")

    paquete.type = tipoPaquete
    paquete.save()
    messages.success(request, 'Paquete actualizado!')
    return redirect('../GestionPaquetes/')