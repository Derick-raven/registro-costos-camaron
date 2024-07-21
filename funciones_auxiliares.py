import time
import os
from datetime import datetime

# --------------- FUNCIONES EXTRAS -------------------------
def limpiar():
    os.system('cls')

def fecha_hoy() -> str:
    fecha_h = datetime.now()# Obtener la fecha de hoy
    fecha_hf = fecha_h.strftime('%Y-%m-%d')# Formatear la fecha
    return fecha_hf


#--------------- CALCULOS -----------------------------
#comprueba el tamaño de la ventana del cmd
def tamaño() -> int:
    ancho = ''
    altura = ''

    r = os.get_terminal_size() #devuelve una tupla con el tamaño del CMD, (columns, lines) 

    #le pedira al usuario que ajuste el tamaño y no se detendra hasta tener minimo 90 de ancho y 20 de altura
    while r[0] < 90 or r[1] < 20:
        print('ajuste el tamaño de la ventana')
        r = os.get_terminal_size()
        time.sleep(2)
    
    #valida que la altura y el ancho sea numeros pares
    if r[0] < 120 or r[1] < 30:
        for i in r:
            if i % 2 != 0 and ancho == '':
                ancho = i - 1
            elif i % 2 == 0 and ancho == '':
                ancho = i
            elif i % 2 != 0 and altura == '':
                altura = i - 1
            else:
                altura = i 

    else: #elif r[0] >= 120 or r[1] >= 30:
        for i in r:
            if i % 2 != 0 and ancho == '':
                ancho = i - 1
            elif i % 2 == 0 and ancho == '':
                ancho = i
            elif i % 2 != 0 and altura == '':
                altura = i - 1
            else:
                altura = i 
    return ancho, altura

#cantidad de apostrofe
def tamaño_general(ancho) -> bool:
    if ancho < 100:
        tamaño_g = False
    elif ancho >= 110:
        tamaño_g = True
    return tamaño_g 

def calculo_par(x):
    if x % 2 == 0:
        return True
    else:
        return False

def calculo_espacio_tamaño(z,v,w) -> int:
    x = calculo_par(z)
    if x == True:
        n = z // 2
        if(n*2) + v == w:
            return n, n
    else:
        n = z // 2
        y = z - n
        if (n + y) + v == w:
            return y,n


# ----------- rango de 90 columnas -----------------
def cantidad_espacios_venta(z) -> str:
    a = ''
    for i in range(z):
        a += ' '
    return a

def cantidad_apostrofe(z) -> str:
    if z == False:
        a = ''
        for i in range(90):
            a += '-'
        return a
    else:
        a = ''
        for i in range(110):
            a += '-'
        return a

def calculo_tamaño(q,a,b) -> str:
    if q == False:
        if len(a) + len(b) < 90:
            z = 90 - (len(a) + len(b))
            z = cantidad_espacios_venta(z)
        w = a + z + b
        return w
    else:
        if len(a) + len(b) < 110:
            z = 110 - (len(a) + len(b))
            z = cantidad_espacios_venta(z)
        w = a + z + b
        return w

def calculo_tamaño0(q,a,b,c) -> str:
    if q == False:
        if len(a) + len(b) + len(c) < 90:
            k = (len(a) + len(b) + len(c))
            z = 90 - k
            f ,g = calculo_espacio_tamaño(z,k,90)
            v = cantidad_espacios_venta(g)
            y = cantidad_espacios_venta(f)
        w = a + y + b + v + c
        return w
    else:
        if len(a) + len(b) < 110:
            k = (len(a) + len(b) + len(c))
            z = 110 - k
            f, g = calculo_espacio_tamaño(z,k,110)
            v = cantidad_espacios_venta(g)
            y = cantidad_espacios_venta(f)
        w = a + y + b + v + c
        return w
    
def relleno_n(q,x) -> str:
    for i in range(x):
        print(calculo_tamaño(q,'|','|'))