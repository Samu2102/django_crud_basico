from django.urls import path #acceder a las urls
from . import views #acceder a las vistas

from django.conf import settings
from django.conf.urls.static import static # se utilizarán archivos estáticos

urlpatterns = [
    path('',views.inicio,name='inicio'),

    path('nosotros/',views.nosotros,name='nosotros'),
#en la primera parte, nosotros vamos a escribir en la url la palabra nosotros. Accediendo a views.nosotros para mostrarlo.
    path('hojas/',views.hojas, name='hojas'), #la funcion es la de views.hojas
    path('hojas/crear',views.crearh, name='crearh'), #no se repita la url de hojas, se agrega hojas/crear
    path('editar/<int:id>',views.editarh, name='editarh'),
    path('eliminar/<int:id>',views.eliminarh, name='eliminarh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
