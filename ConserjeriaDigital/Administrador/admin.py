from django.contrib import admin
from .models import User
from .models import Residente
from .models import Conserje
from .models import Administrador
from .models import Correspondencia
# Register your models here.
admin.site.register(User)
admin.site.register(Residente)
admin.site.register(Conserje)
admin.site.register(Administrador)
admin.site.register(Correspondencia)