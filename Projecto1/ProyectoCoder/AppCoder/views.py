# from django.shortcuts import render
from django.shortcuts import render
import datetime

# Create your views here.
from django.http import HttpResponse
from django.template import Context, Template
from AppCoder.models import Familiares



def familiares(self):

    miHtml = open('/Users/lucaslera/Documents/python-coder/djangoProjecto1/Projecto1/ProyectoCoder/AppCoder/plantillas/template1.html')

    plantilla = Template(miHtml.read())

    miHtml.close()


    mama = Familiares(nombre= "Mama" , fechaNacimiento= datetime.datetime(1978,11,11,), edad = 52 )
    mama.save()

    papa = Familiares(nombre= "Papa" , fechaNacimiento= datetime.datetime(1974,12,2), edad = 48 )
    papa.save()

    tio = Familiares(nombre= "Tio" , fechaNacimiento= datetime.datetime(1977,9,3), edad = 45 )
    tio.save()

    dateAux ={
        "mamaNacimiento": mama.fechaNacimiento.strftime("%x"),
        "papaNacimiento": papa.fechaNacimiento.strftime("%x"),
        "tioNacimiento": tio.fechaNacimiento.strftime("%x"),
    }
    familiaDic = {
        "mama": f"{mama.nombre} - Nacio: {dateAux.get('mamaNacimiento')} tiene {mama.edad} años!",
        "papa": f"{papa.nombre} - Nacio: {dateAux.get('papaNacimiento')} tiene {papa.edad} años!",
        "tio": f"{tio.nombre} - Nacio: {dateAux.get('tioNacimiento')} tiene {tio.edad} años!",
    }
    
    documentoDeTexto = f"<h2>-->{mama.nombre} - Nacio: {mama.edad} tiene {mama.edad} años<h2><br><h2>-->{papa.nombre} - Nacio: {papa.edad} tiene {mama.edad} años<h2><br><h2>-->{mama.nombre} - Nacio: {tio.edad} tiene {tio.edad} años<h2>"
    miContexto = Context(familiaDic)
    documento = plantilla.render(miContexto)
  
    return HttpResponse(documento)
    # return HttpResponse(documentoDeTexto)