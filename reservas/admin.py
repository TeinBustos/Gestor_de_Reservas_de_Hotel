from django.contrib import admin
from .models import Encabezado, HotelesUnaEstrella, HotelesDosEstrellas, HotelesTresEstrellas, HotelesCuatroEstrellas, HotelesCincoEstrellas, Bienvenida

# Register your models here.
admin.site.register(Encabezado)
admin.site.register(HotelesUnaEstrella)
admin.site.register(HotelesDosEstrellas)
admin.site.register(HotelesTresEstrellas)
admin.site.register(HotelesCuatroEstrellas)
admin.site.register(HotelesCincoEstrellas)
admin.site.register(Bienvenida)