from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps
import sqlite3 
   
# Create your views here.
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def usuarios(request):

    if (request.method=='GET'):
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM usuarios")
        resultados = res.fetchall()
        print(resultados)
        return render(request, 'usuarios.html', {'data':resultados})
    
    elif (request.method=='POST'):
        body = request.body.decode('UTF-8')
        eljson = loads(body)
        password = eljson['password']
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = cur.execute("INSERT INTO usuarios (password) VALUES (?)", (password,))
        con.commit()
        return HttpResponse("Creado nuevo usuario con contraseña: "+password)
    
    elif (request.method=='DELETE'):
        body = request.body.decode('UTF-8')
        eljson = loads(body)
        id = eljson['id']
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        flag = cur.execute("SELECT * FROM usuarios WHERE id=?", (str(id),))
        flag = flag.fetchall()
        if (bool(flag)):
            res = cur.execute("DELETE FROM usuarios WHERE id=?", (str(id),))
            res = cur.execute("DELETE FROM partidas WHERE id_usuario=?", (str(id),))
            con.commit()
            return HttpResponse("Usuario "+str(id)+" eliminado")
        else:
            return HttpResponse("ID NO EXISTENTE")

    elif (request.method=='PUT'):
        body = request.body.decode('UTF-8')
        eljson = loads(body)
        password = eljson['password']
        id = eljson['id']
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        flag = cur.execute("SELECT * FROM usuarios WHERE id=?", (str(id),))
        flag = flag.fetchall()
        if (bool(flag)):
            res = cur.execute("UPDATE usuarios SET password=? WHERE id=?", (password, str(id),))
            con.commit()
            return HttpResponse("Nuevos datos de usuraio "+str(id)+": "+password)
        else:
            return HttpResponse("EL ID INGRESADO NO ES VALIDO")        


@csrf_exempt
def partidas(request):

    if (request.method=='GET'):
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM partidas")
        resultados = res.fetchall()
        print(resultados)
        return render(request, 'partidas.html', {'data':resultados})
    
    elif (request.method=='POST'):
        body = request.body.decode('UTF-8')
        eljson = loads(body)
        fecha = eljson['fecha']
        id_usuario = eljson['id_usuario']
        minutos_jugados = eljson['minutos_jugados']
        puntaje = eljson['puntaje']
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        flag = cur.execute("SELECT * FROM usuarios WHERE id=?", (str(id_usuario),))
        flag = flag.fetchall()
        if (bool(flag)):
            res = cur.execute("INSERT INTO partidas (fecha, id_usuario, minutos_jugados, puntaje) VALUES (?, ?, ?, ?)", (fecha, id_usuario, minutos_jugados, puntaje,))
            con.commit()
            return HttpResponse("Nueva partida: "+fecha+" "+str(id_usuario)+" "+str(minutos_jugados)+" "+str(puntaje))
        else:
            return HttpResponse("El id de usuario no existe")
    
    elif (request.method=='DELETE'):
        body = request.body.decode('UTF-8')
        eljson = loads(body)
        id = eljson['id']
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        flag = cur.execute("SELECT * FROM partidas WHERE id=?", (str(id),))
        flag = flag.fetchall()
        if (bool(flag)):
            res = cur.execute("DELETE FROM partidas WHERE id=?", (str(id),))
            con.commit()
            return HttpResponse("Parida "+str(id)+" borrada")
        else:
            return HttpResponse("ID invalido")
    
    elif (request.method=='PUT'):
        body = request.body.decode('UTF-8')
        eljson = loads(body)
        id = eljson['id']
        fecha = eljson['fecha']
        id_usuario = eljson['id_usuario']
        minutos_jugados = eljson['minutos_jugados']
        puntaje = eljson['puntaje']
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        flag = cur.execute("SELECT * FROM partidas WHERE id=?", (str(id),))
        flag = flag.fetchall()
        flag2 = cur.execute("SELECT * FROM usuarios WHERE id=?", (str(id_usuario),))
        flag2 = flag2.fetchall()
        print(flag)
        print(flag2)
        if (bool(flag) and bool(flag2)):
            res = cur.execute("UPDATE partidas SET fecha=?, id_usuario=?, minutos_jugados=?, puntaje=? WHERE id=?", (fecha, str(id_usuario), str(minutos_jugados), str(puntaje), str(id),))
            con.commit()
            return HttpResponse("Partida "+str(id)+" actualizada con: "+fecha+" "+str(id_usuario)+" "+str(minutos_jugados)+" "+str(puntaje))
        else:
            return HttpResponse("INPUTS NO VALIDOS")