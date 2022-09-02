from django.template import Context, Template
from django.shortcuts import render
from django.http import HttpResponse

def saludo(self, nombre = 'Jane Dow'):
    return HttpResponse(f'hola Django - soy {nombre} coder')

def testeo(request):
    return HttpResponse('<h1>Ahora si estamos con HTML<h1>')

def probandoTemplate(self):
    miHtml = open('/Users/lucaslera/Documents/python-coder/djangoProjecto1/Projecto1/Projecto1/plantillas/template1.html')

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)