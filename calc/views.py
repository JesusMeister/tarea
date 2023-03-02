from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps

def mcd(a,b):
    if (b == 0): 
        return a
    else:
        return mcd(b, a%b)

def mcm(a,b):
    return (a*b/mcd(a,b))

class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)
    def simplificar(self):
        x = mcd(self.num, self.den)
        f = Fraccion(int(self.num/x), int(self.den/x))
        return f
    
# Create your views here.
def index(request):
    #return HttpResponse('<h1> Bienvenidos a la sesión del jueves!</h1>')
    return render(request, 'index.html')


def proceso(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    return HttpResponse('Hola '+ nombre)

@csrf_exempt
def suma(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']
    dr = mcm(denominador1, denominador2)
    nr1 = numerador1*(dr/denominador1)
    nr2 = numerador2*(dr/denominador2)
    nr = nr1 + nr2
    resultado = Fraccion(int(nr),int(dr))
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")

@csrf_exempt
def multiplicacion(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']
    dr = denominador1*denominador2
    nr = numerador1*numerador2
    resultado = Fraccion(int(nr),int(dr))
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")

@csrf_exempt
def division(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']
    dr = denominador1*numerador2
    nr = numerador1*denominador2
    resultado = Fraccion(int(nr),int(dr))
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")

@csrf_exempt
def resta(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']
    dr = mcm(denominador1, denominador2)
    nr1 = numerador1*(dr/denominador1)
    nr2 = numerador2*(dr/denominador2)
    nr = nr1 - nr2
    resultado = Fraccion(int(nr),int(dr))
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")