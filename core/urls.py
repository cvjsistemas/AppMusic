from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='inicio'),
    path('registroDisco/',registroDisco,name='registroDisco'),
    path('eliminarDisco/<product_id>',eliminarDisco,name='eliminarDisco'),
    path('edicionDisco/<product_id>',edicionDisco,name='edicionDisco'),
    path('editarDisco/',editarDisco,name='editarDisco'),
    path('signup/',signup,name='signup'),
    path('logout/',signout,name='signout'),
    path('signin/',signin,name='signin'),
]