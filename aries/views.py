import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import *

# Create your views here.

def homeView(request):
    destacados = Vehiculo.objects.all()[:3]
    return render(request,"index.html",{"host":request.get_host(),"section":"inicio", "destacados":destacados})

def carsView(request):
    vehiculos = Vehiculo.objects.all()
    return render(request,"cars.html",{"host":request.get_host(), "section":"vehiculos",
                                       "vehiculos":vehiculos})

def carDetailView(request, modelo):
    try:
        vehiculo = Vehiculo.objects.get(modelo=modelo)
    except:
        return redirect("/")
    return render(request, "car-details.html",{"host":request.get_host(), "section": "vehiculos",
                                               "vehiculo": vehiculo})

def contactView(request):
    return render(request,"contact.html",{"host":request.get_host(),"section":"contacto"})

def aboutUsView(request):
    return render(request,"about-us.html",{"host":request.get_host(),"section":"empresa"})

def sendMailView(request):
    send_mail(
        request.POST.get("subject"),
        "Mensaje de {}: \n".format(request.POST.get("email")) + request.POST.get("message"),
        request.POST.get("email"),
        ['cettipao@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse(json.dumps({"success": True}), content_type="application/json")


def cotizarView(request):
    send_mail(
        "Pedido de cotizacion de: {}".format(request.POST.get("nombre")),
        "Vehiculo a Cotizar\nModelo: {}, Version: {}\nInfo Contacto\nDNI: {}\nEmail: {}\nTelefono: {}".format(
            request.POST.get("modelo"), request.POST.get("email"), request.POST.get("dni"),
            request.POST.get("correo"), request.POST.get("telefono")
        ),
        request.POST.get("email"),
        ['cettipao@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse(json.dumps({"success": True}), content_type="application/json")