import time
import os
from datetime import datetime
from colorama import Fore, init
from pathlib import Path

init(autoreset=True)

# -------------------------------------- FUNCIONES EXTRAS -------------------------
def limpiar():
    os.system('cls')

def fecha_hoy() -> str:
    fecha_h = datetime.now()# Obtener la fecha de hoy
    fecha_hf = fecha_h.strftime('%Y-%m-%d')# Formatear la fecha
    return fecha_hf

def relleno_n(q,x) -> str:
    for i in range(x):
        print(calculo_tamaño(q,'|','|'))

def calculo_par(x) -> bool:
    if x % 2 == 0:
        return True
    else:
        return False
    
def esperar(x:int):
    time.sleep(x)

#--------------------------------------------------- FUNCIONES NECESARIAS ----------------------------------------------------------
def directorio_actual_data():
    directorio_actual = Path(__file__).parent # Obtener la ruta del directorio donde se encuentra este script
    return directorio_actual

def guardar_ultima_ubicacion(ciudad,region,pais):
    archivo_vacio = os.path.join(c_datos, 'ultima_ubicacion.txt')
    with open(archivo_vacio, 'a') as archivo:
            archivo.write(ciudad + ',') 
            archivo.write(region + ',')
            archivo.write(pais + '\n')

def listar_contenido_carpeta_datos(direccion,lista_arch):
    # Obtener la lista de archivos y carpetas en la dirección especificada
    contenido = os.listdir(direccion)
    if not contenido:  # Verificar si la carpeta está vacía
        lista_archivos_necesarios = lista_arch
        
        for i in lista_archivos_necesarios:
            archivo_vacio = os.path.join(direccion, f'{i}')
            with open(archivo_vacio, 'w') as archivo:
                archivo.write('')  # Crear un archivo vacío a.txt

        #inicia el conteo de numero de factura en cero
        archivo_vacio = os.path.join(direccion, 'numero_orden_compra.txt')
        with open(archivo_vacio, 'w') as archivo:
                archivo.write('0')  # Crear un archivo vacío a.txt

    return contenido
    
def listar_contenido_carpeta(direccion):
    """
    Devuelve una lista con todos los nombres de archivos y subcarpetas en la dirección especificada.
    """
    try:
        # Obtener la lista de archivos y carpetas en la dirección especificada
        contenido = os.listdir(direccion)

        return contenido
    
    except FileNotFoundError:
        print(f"La carpeta en la dirección '{direccion}' no se encontró.")
        return []
    
    except NotADirectoryError:
        print(f"La dirección '{direccion}' no es una carpeta.")
        return []
    
    except PermissionError:
        print(f"No se tienen permisos para acceder a la carpeta en '{direccion}'.")
        return []
    
#------------------ LEER NUMERO DE FACTURA ALMACENADO
def numero_orden() -> str:
    archivo = os.path.join(c_datos, 'numero_orden_compra.txt')
    with open(archivo, 'r') as a:
        x = a.readline()
        return x.strip()
    
#------------------ ACTUALIZAR NUMERO DE FACTURA
def numero_orden_actualizado(x):
    archivo = os.path.join(c_datos, 'numero_orden_compra.txt')
    with open(archivo, 'w') as a:
        a.write(x)

#------------------ GUARDAR INFORMACION DE FACTURA
def guardar_info_orden(nombre_arch:str,fecha_hf,numero_orden,numero_cedula,nombre_cliente,numero_tel_cliente,correo_cliente,ruta,precio_ruta,camaron_t,cant_compra,cant_camion,sub_precio,sub_total,iva,total_final,precio_camaron):
    archivo_ubi = os.path.join(c_pedidos, f'{nombre_arch}')
    with open(archivo_ubi, 'w') as archivo:
        archivo.write('Fecha:' + fecha_hf + '\n')
        archivo.write('Numero Factura:' + numero_orden + '\n')
        archivo.write('Nombre cliente:' + nombre_cliente + '\n')
        archivo.write('Numero cedula:' + numero_cedula + '\n')
        archivo.write('Numero telefonico:' + numero_tel_cliente + '\n')
        archivo.write('Correo:' + correo_cliente + '\n')
        archivo.write('Ruta:' + ruta + '\n')
        archivo.write('Precio ruta:' + precio_ruta + '\n')
        archivo.write('Tipo de camaron:' + camaron_t + '\n')
        archivo.write('Precio camaron:' + precio_camaron + '\n')
        archivo.write('Cantidad comprada:' + cant_compra + '\n')
        archivo.write('Cantidad camion:' + cant_camion + '\n')
        archivo.write('Sub precio:' + sub_precio + '\n')
        archivo.write('Sub total:' + sub_total + '\n')
        archivo.write('Iva:' + iva + '\n')
        archivo.write('Total final:' + total_final + '\n')
        #archivo.write('')

def guardar_info_orden_masiva(nombre_arch:str,fecha_hf,numero_orden,numero_cedula,nombre_cliente,numero_tel_cliente,correo_cliente,sub_total,iva,total_final,lista:list):

    archivo_ubi = os.path.join(c_pedidos, f'{nombre_arch}')
    with open(archivo_ubi, 'w') as archivo:
        archivo.write('Fecha:' + fecha_hf + '\n')
        archivo.write('Numero Factura:' + numero_orden + '\n')
        archivo.write('Nombre cliente:' + nombre_cliente + '\n')
        archivo.write('Numero cedula:' + numero_cedula + '\n')
        archivo.write('Numero telefonico:' + numero_tel_cliente + '\n')
        archivo.write('Correo:' + correo_cliente + '\n')

        for i in range(len(lista)):           
            archivo.write('-----------------------------------------\n')
            archivo.write('Ruta:' + lista[i][0] + '\n')
            archivo.write('Precio ruta:' + lista[i][1] + '\n')
            archivo.write('Tipo de camaron:' + lista[i][2] + '\n')
            archivo.write('Precio camaron:' + str(lista[i][3]) + '\n')
            archivo.write('Cantidad comprada:' + lista[i][4] + '\n')
            archivo.write('Cantidad camion:' + lista[i][5] + '\n')
            archivo.write('Sub precio:' + lista[i][6] + '\n')
        
        archivo.write('Sub total:' + sub_total + '\n')
        archivo.write('Iva:' + iva + '\n')
        archivo.write('Total final:' + total_final + '\n')

def guardar_info_orden_empresa(nombre_arch:str,fecha_hf,numero_orden,numero_cedula,ruc,nombre_empresa,nombre_cliente,numero_tel_cliente,correo_cliente,ruta,precio_ruta,camaron_t,cant_compra,cant_camion,sub_precio,sub_total,iva,total_final,precio_camaron):
    archivo_ubi = os.path.join(c_pedidos, f'{nombre_arch}')
    with open(archivo_ubi, 'w') as archivo:
        archivo.write('Fecha:' + fecha_hf + '\n')
        archivo.write('Numero Factura:' + numero_orden + '\n')
        archivo.write('Nombre empresa:' + nombre_empresa + '\n')
        archivo.write('Numero ruc:' + ruc + '\n')
        archivo.write('Nombre cliente:' + nombre_cliente + '\n')
        archivo.write('Numero cedula:' + numero_cedula + '\n')
        archivo.write('Numero telefonico:' + numero_tel_cliente + '\n')
        archivo.write('Correo:' + correo_cliente + '\n')
        archivo.write('Ruta:' + ruta + '\n')
        archivo.write('Precio ruta:' + precio_ruta + '\n')
        archivo.write('Tipo de camaron:' + camaron_t + '\n')
        archivo.write('Precio camaron:' + precio_camaron + '\n')
        archivo.write('Cantidad comprada:' + cant_compra + '\n')
        archivo.write('Cantidad camion:' + cant_camion + '\n')
        archivo.write('Sub precio:' + sub_precio + '\n')
        archivo.write('Sub total:' + sub_total + '\n')
        archivo.write('Iva:' + iva + '\n')
        archivo.write('Total final:' + total_final + '\n')
        #archivo.write('')

def guardar_info_orden_empresa_masiva(nombre_arch:str,fecha_hf,numero_orden,numero_cedula,ruc,nombre_empresa,nombre_cliente,numero_tel_cliente,correo_cliente,sub_total,iva,total_final,lista:list):

    archivo_ubi = os.path.join(c_pedidos, f'{nombre_arch}')
    with open(archivo_ubi, 'w') as archivo:
        archivo.write('Fecha:' + fecha_hf + '\n')
        archivo.write('Nnumero Factura:' + numero_orden + '\n')
        archivo.write('Nombre empresa:' + nombre_empresa + '\n')
        archivo.write('Numero ruc:' + ruc + '\n')
        archivo.write('Nombre cliente:' + nombre_cliente + '\n')
        archivo.write('Numero cedula:' + numero_cedula + '\n')
        archivo.write('Numero telefonico:' + numero_tel_cliente + '\n')
        archivo.write('Correo:' + correo_cliente + '\n')

        for i in range(len(lista)):           
            archivo.write('-----------------------------------------\n')
            archivo.write('Ruta:' + lista[i][0] + '\n')
            archivo.write('Precio ruta:' + lista[i][1] + '\n')
            archivo.write('Tipo de camaron:' + lista[i][2] + '\n')
            archivo.write('Precio camaron:' + str(lista[i][3]) + '\n')
            archivo.write('Cantidad comprada:' + lista[i][4] + '\n')
            archivo.write('Cantidad camion:' + lista[i][5] + '\n')
            archivo.write('Sub precio:' + lista[i][6] + '\n')
        
        archivo.write('Sub total:' + sub_total + '\n')
        archivo.write('Iva:' + iva + '\n')
        archivo.write('Total final:' + total_final + '\n')

#----------------------------------- BUSQUEDA
def busqueda1(busqueda):#orden fecha
    lista = []
    for i in range(len(pedidos_lista)):
        p = pedidos_lista[i].split(',')
        if p[0] == busqueda:
            archivo = os.path.join(c_pedidos, pedidos_lista[i] + '.txt')
            lista.append(archivo)
    return lista

def busqueda2(busqueda):#orden factura
    for i in range(len(pedidos_lista)):
        p = pedidos_lista[i].split(',')
        if p[-1] == busqueda:
            archivo = os.path.join(c_pedidos, pedidos_lista[i] + '.txt')
            return archivo

def busqueda3(busqueda):#orden cedula
    lista = []
    for i in range(len(pedidos_lista)):
        p = pedidos_lista[i].split(',')
        if p[2] == busqueda:
            archivo = os.path.join(c_pedidos, pedidos_lista[i] + '.txt')
            lista.append(archivo)
    return lista

def busqueda4(busqueda):#orden ruc
    lista = []
    for i in range(len(pedidos_lista)):
        p = pedidos_lista[i].split(',')
        if p[1] == busqueda:
            archivo = os.path.join(c_pedidos, pedidos_lista[i] + '.txt')
            lista.append(archivo)
    return lista

def busqueda5(busqueda):#orden nombre cliente
    lista = []
    for i in range(len(pedidos_lista)):
        p = pedidos_lista[i].split(',')
        if p[-3] == busqueda:
            archivo = os.path.join(c_pedidos, pedidos_lista[i] + '.txt')
            lista.append(archivo)
    return lista

def busqueda6(busqueda):#orden nombre empresa
    lista = []
    for i in range(len(pedidos_lista)):
        p = pedidos_lista[i].split(',')
        if p[1] != 'xxxxxxxxxxxxx':
            if p[3] == busqueda:
                archivo = os.path.join(c_pedidos, pedidos_lista[i] + '.txt')
                lista.append(archivo)
    return lista

def busqueda7(busqueda):#orden telefono
    lista = []
    for i in range(len(pedidos_lista)):
        p = pedidos_lista[i].split(',')
        if p[-2] == busqueda:
            archivo = os.path.join(c_pedidos, pedidos_lista[i] + '.txt')
            lista.append(archivo)
    return lista

#----------------------------------------------------------------------------
def leer_info_orden0(nombre_arch:str):
    archivo_ubi = os.path.join(c_pedidos, nombre_arch)
    with open(archivo_ubi, 'r') as archivo:
        for i in archivo:
            print(i.strip())

def leer_info_orden(nombre_arch:str) -> str:
    lista = []
    archivo_ubi = os.path.join(c_pedidos, nombre_arch)
    with open(archivo_ubi, 'r') as archivo:
        for i in archivo:
            lista.append(i.strip())
    a = lista[0]
    b = lista[1]
    c = lista[2]
    return a,b,c

#------------------------------------------------------------- CALCULOS -----------------------------------------------------
#--------- CALCULO TAMAÑOS / GUIONES MEDIO -----------------
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
        return Fore.CYAN + a

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

def calculo_espacio_tamaño00(z,v,w) -> int:
    x = calculo_par(z)
    if x == True:
        n = z // 4
        n1 = n
        n2 = n
        n3 = n        
        if(n + n1 + n2 + n3) + v == w:
            return n, n1, n2, n3
    else:
        n = z // 4
        n1 = n
        n2 = n
        y = z - (n + n1 + n2)
        if (n + n1 + n2 + y) + v == w:
            return n, n1, n2, y

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

def calculo_tamaño_venta0(q,a): # venta casi final
    if q == False:
        if len(a) < 22:
            k = len(a)
            z = 22 - k
            p, o = calculo_espacio_tamaño(z,k,22)
            f = cantidad_espacios_venta(p)
            g = cantidad_espacios_venta(o - 1)
        w = Fore.WHITE + '|' + f + Fore.LIGHTCYAN_EX + a + g 
        return w
    else:
        if len(a) < 27:
            k = len(a)
            z = 27 - k
            p, o = calculo_espacio_tamaño(z,k,27)
            f = cantidad_espacios_venta(p)
            g = cantidad_espacios_venta(o - 1)
        w = Fore.WHITE + '|' + f + Fore.LIGHTCYAN_EX + a + g 
        return w
    
# -------- ESPACIOS --------------
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

def cantidad_espacios_venta(z) -> str:
    a = ''
    for i in range(z):
        a += ' '
    return a


# -------------- CALCULOS VALORES ---------------
def calculo_valor_ruta(x):
    if x == 1:
        valor = 100 # cuenca
        lugar = 'Guayaquil a Cuenca'
    elif x == 2:
        valor = 200 # quevedo
        lugar = 'Guayaquil a Quevedo'
    elif x == 3:
        valor = 250 # quito
        lugar = 'Guayaquil a Quito'
    elif x == 4:
        valor = 200 # ambato
        lugar = 'Guayaquil a Ambato'
    elif x == 5:
        valor = 230 # santo domingo
        lugar = 'Guayaquil a Santo Domingo'
    elif x == 6:
        valor = 250 # loja
        lugar = 'Guayaquil a Loja'
    elif x == 7:
        valor = 200 # machala
        lugar = 'Guayaquil a Machala'
    else:
        valor = 150 # salinas
        lugar = 'Guayaquil a Salinas'
    return str(valor), lugar

def calculo_valor_camaron(x):
    if x == 1:
        valor = 20 # tigre blanco valor de $/kilogramo
        tipo = 'tigre blanco'
    elif x == 2:
        valor = 30 # tigle negro valor de $/kilogramo
        tipo = 'tigle negro'
    return valor, tipo 

def calcular_valor_venta(cant_compra,valor_camaron,valor_ruta) -> str:
    camion = 500 # un camion puede llevar 500kilogramos de camaron 
    camion_valor = 300 # precio por camion usado
    cant_compra = int(cant_compra)
    valor_camaron = int(valor_camaron)
    valor_ruta = int(valor_ruta)
    cant_camion = 0
    aux = 0
    sub_precio = 0
    if aux < cant_compra:
        cant_camion = cant_compra // camion #cantidad de camion a enviar
        aux += cant_camion * camion
        
        if aux < cant_compra:
            x = cant_compra - aux
            cant_camion += 1
        
        sub_precio = ((camion_valor * cant_camion) * valor_camaron ) + valor_ruta
        #pf = canti_camion * valor_camion * valor_camaron + valor ruta

    return str(cant_camion), str(sub_precio)

def calculo_sub_total(lista:list) -> str:
    suma = 0
    for i in range(len(lista)):
        suma += int(lista[i][6])
    suma = str(suma)
    return suma

def calculo_iva(sub_total:str) -> str:
    iva = int(sub_total) * 0.15
    iva = str(iva)
    return iva

def calculo_precio_final(sub_total,iva) -> str:
    precio_final = int(sub_total) + float(iva)
    return str(precio_final)

#--------------------------------------------------------- CREAR CARPETAS NECESARIAS ------------------------------------------------
# Definir nombres de las carpetas a buscar/crear
carpetas = ["informes", "pedidos", "datos"]

directorio_actual = directorio_actual_data() # Obtener la ruta del directorio donde se encuentra este script

# Inicializar variables para almacenar las ubicaciones de las carpetas
c_informes = c_pedidos = c_datos = None

variable_guardar_carpeta = {"informes": "c_informes", "pedidos": "c_pedidos", "datos": "c_datos"}

for i in carpetas: # Iterar sobre cada carpeta para verificar su existencia o crearla
    folder_path = directorio_actual / i
    if not folder_path.exists():
        folder_path.mkdir(parents=True, exist_ok=True)
    globals()[variable_guardar_carpeta[i]] = str(folder_path)

# Imprimir las ubicaciones de las carpetas
#print(f"c_informe: {c_informes}")
#print(f"c_pedidos: {c_pedidos}")
#print(f"c_datos: {c_datos}")

# lista con los nombres de los archivos en la carpeta datos
lista_archivos_necesarios_datos = ['numero_orden_compra.txt','ultima_ubicacion.txt'] #en caso que no exista, crea estos archivos
datos_lista = listar_contenido_carpeta_datos(c_datos,lista_archivos_necesarios_datos) #devuelve la lista de archivos en una lista

pedidos_lista = listar_contenido_carpeta(c_pedidos)
#print(nombres)