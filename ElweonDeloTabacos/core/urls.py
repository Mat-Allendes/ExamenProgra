from django.urls import path
from .views import *

urlpatterns = [
   path('',root),
   path('index', index,name='index'),
   path('tabacos/',tabacos,name='tabacos'),
   path('cigarros/',cigarros,name='cigarros'),
   path('accesorios/',accesorios,name='accesorios'),
   path('nosotros/',nosotros,name='nosotros'),
   path('suscripcion/',suscripcion,name='suscripcion'),
   path('registro/',registro,name='registro')
]
