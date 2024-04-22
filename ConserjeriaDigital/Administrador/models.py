from django.db import models

# Create your models here.

##clase principal User

class User(models.Model):
    rut=models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
        
##clase Residente, hereda de User en modo 1 a 1

class Residente(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    NumeroDepartamento = models.IntegerField(default=0)
    casilla = models.IntegerField()

    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.usuario.nombre,self.NumeroDepartamento)

##clase Conserje, hereda de User en modo 1 a 1

class Conserje(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE) 
    pass

##clase Administrador, hereda de User en modo 1 a 1

class Administrador(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE) 
    pass

##clase Correspondencia, tiene relacion con Residente en muchos a 1

class Correspondencia(models.Model):
    CARTA = "C"
    ENCOMIENDA = "E"
    tipo = [
        (CARTA, "carta"),
        (ENCOMIENDA,"Encomienda")
    ]
    id = models.AutoField(primary_key=True)
    type = models.CharField(
        max_length=2,
        choices=tipo,
        default=CARTA
    )
    destinatario = models.ForeignKey(Residente,on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.type,self.destinatario.NumeroDepartamento)