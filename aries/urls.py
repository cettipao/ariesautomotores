from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView),
    path("vehiculos/<str:modelo>", carDetailView),
    path("vehiculos/", carsView),
    path("contacto/", contactView),
    path("nuestra_empresa/", aboutUsView),

    path("sendmail/", sendMailView),
    path("cotizar/", cotizarView),
]


