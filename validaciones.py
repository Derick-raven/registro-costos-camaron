import time
import re
import funciones_auxiliares as faux
import menus as mn

def limpiar():
    faux.limpiar()

#------------- VALIDACIONES --------------------
#inicio del sistemas
def Validacion_texto_0():
    x = input(': ').lower()
    while x != 's' and x != 'n':
        mn.ingreso_erroneo_fuera_rango_letra()
        x = input(': ').lower()
    return x

def Validacion_decicion_0():#seleccion del menu principal
    while True:
        try:
            x = input(':').lower()
            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 4:
                    mn.ingreso_erroneo_fuera_rango()
                    mn.menu_inicio_0()
                    x = input(':')
                    if x.isalpha() == True:
                        mn.confirmacion()
                        break
                    else:
                        x = int(x)
            else:
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    mn.menu_inicio_0()
                    x = input(':').lower()
                    if x.isdigit() == True:
                        mn.confirmacion()
                        break
            
        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x
        break

def Validacion_decicion_directo():# menu costo directo 
    while True:
        try:
            x = input(':').lower()
            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 3:
                    mn.ingreso_erroneo_fuera_rango()
                    mn.menu_costos_directos()
                    x = input(':')
                    if x.isalpha() == True:
                        mn.confirmacion()
                        break
                    else:
                        x = int(x)
            else:
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    mn.menu_costos_directos()
                    x = input(':').lower()
                    if x.isdigit() == True:
                        mn.confirmacion()
                        break

        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x
        break

def Validacion_decicion_directo1():# menu costo directo 
    while True:
        try:
            x = input(':').lower()
            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 3:
                    mn.ingreso_erroneo_fuera_rango()
                    mn.menu_costos_directos_1()
                    x = input(':')
                    if x.isalpha() == True:
                        mn.confirmacion()
                        break
                    else:
                        x = int(x)
            else:
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    mn.menu_costos_directos_1()
                    x = input(':').lower()
                    if x.isdigit() == True:
                        mn.confirmacion()
                        break

        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x
        break

def Validacion_decicion_directo2():# menu costo directo 
    while True:
        try:
            x = input(':').lower()
            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 3:
                    mn.ingreso_erroneo_fuera_rango()
                    mn.menu_costos_directos_2()
                    x = input(':')
                    if x.isalpha() == True:
                        mn.confirmacion()
                        break
                    else:
                        x = int(x)
            else:
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    mn.menu_costos_directos_2()
                    x = input(':').lower()
                    if x.isdigit() == True:
                        mn.confirmacion()
                        break

        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x
        break

def Validacion_decicion_directo3():# menu costo directo 
    while True:
        try:
            x = input(':').lower()
            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 3:
                    mn.ingreso_erroneo_fuera_rango()
                    mn.menu_costos_directos_3()
                    x = input(':')
                    if x.isalpha() == True:
                        mn.confirmacion()
                        break
                    else:
                        x = int(x)
            else:
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    mn.menu_costos_directos_3()
                    x = input(':').lower()
                    if x.isdigit() == True:
                        mn.confirmacion()
                        break

        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x
        break


def Validacion_decicion_indirecto():# menu opciones indirecto 
    while True:
        try:
            x = input(':').lower()
            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 3:
                    mn.ingreso_erroneo_fuera_rango()
                    mn.menu_costos_indirectos()
                    x = input(':')
                    if x.isalpha() == True:
                        mn.confirmacion()
                        break
                    else:
                        x = int(x)
            else:
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    mn.menu_costos_indirectos()
                    x = input(':').lower()
                    if x.isdigit() == True:
                        mn.confirmacion()
                        break

        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x
        break

def Validacion_decicion_indirecto1():# menu opciones indirecto 
    while True:
        try:
            x = input(':').lower()
            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 3:
                    mn.ingreso_erroneo_fuera_rango()
                    mn.menu_costos_indirectos_1()
                    x = input(':')
                    if x.isalpha() == True:
                        mn.confirmacion()
                        break
                    else:
                        x = int(x)
            else:
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    mn.menu_costos_indirectos_1()
                    x = input(':').lower()
                    if x.isdigit() == True:
                        mn.confirmacion()
                        break

        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x
        break

def Validacion_decicion_indirecto2():# menu opciones indirecto 
    while True:
        try:
            x = input(':').lower()
            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 3:
                    mn.ingreso_erroneo_fuera_rango()
                    mn.menu_costos_indirectos_2()
                    x = input(':')
                    if x.isalpha() == True:
                        mn.confirmacion()
                        break
                    else:
                        x = int(x)
            else:
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    mn.menu_costos_indirectos_2()
                    x = input(':').lower()
                    if x.isdigit() == True:
                        mn.confirmacion()
                        break

        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x
        break

def Validacion_decicion_indirecto3():# menu opciones indirecto 
    while True:
        try:
            x = input(':').lower()
            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 3:
                    mn.ingreso_erroneo_fuera_rango()
                    mn.menu_costos_indirectos_3()
                    x = input(':')
                    if x.isalpha() == True:
                        mn.confirmacion()
                        break
                    else:
                        x = int(x)
            else:
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    mn.menu_costos_indirectos_3()
                    x = input(':').lower()
                    if x.isdigit() == True:
                        mn.confirmacion()
                        break

        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x
        break

def Validacion_decicion_pedidos():# menu opciones pedido 
    while True:
        try:
            x = input(':').lower()
            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 3:
                    mn.ingreso_erroneo_fuera_rango()
                    mn.menu_pedido()
                    x = input(':')
                    if x.isalpha() == True:
                        mn.confirmacion()
                        break
                    else:
                        x = int(x)
            else:
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    mn.menu_pedido()
                    x = input(':').lower()
                    if x.isdigit() == True:
                        mn.confirmacion()
                        break

        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x
        break

def Validacion_decicion_pedidos_ingreso():# menu opciones pedido 
    while True:
        try:
            x = input(':').lower()
            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 2:
                    mn.ingreso_erroneo_fuera_rango()
                    mn.menu_pedido_ingreso()
                    x = input(':')
                    if x.isalpha() == True:
                        mn.confirmacion()
                        break
                    else:
                        x = int(x)
            else:
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    mn.menu_pedido_ingreso()
                    x = input(':').lower()
                    if x.isdigit() == True:
                        mn.confirmacion()
                        break

        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x
        break

def Validacion_decicion_pedidos_modificacion():# menu opciones pedido 
    while True:
        try:
            x = input(':').lower()
            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 3:
                    mn.ingreso_erroneo_fuera_rango()
                    mn.menu_pedido_modificacion()
                    x = input(':')
                    if x.isalpha() == True:
                        mn.confirmacion()
                        break
                    else:
                        x = int(x)
            else:
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    mn.menu_pedido_modificacion()
                    x = input(':').lower()
                    if x.isdigit() == True:
                        mn.confirmacion()
                        break

        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x
        break

def Validacion_decicion_pedidos_eliminar():# menu opciones pedido 
    while True:
        try:
            x = input(':').lower()
            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 3:
                    mn.ingreso_erroneo_fuera_rango()
                    mn.menu_pedido_eliminar()
                    x = input(':')
                    if x.isalpha() == True:
                        mn.confirmacion()
                        break
                    else:
                        x = int(x)
            else:
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    mn.menu_pedido_eliminar()
                    x = input(':').lower()
                    if x.isdigit() == True:
                        mn.confirmacion()
                        break

        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x
        break


def validacion_cedula(nombre_cliente):
    print('|  Cedula',end='')
    x = input(':')
    while len(x) < 10 or x.isdecimal() == False or len(x) > 10:
        if x.isdecimal() == False:
            mn.ingreso_erroneo_numero_no_letras()
        
        elif len(x) < 10:
            mn.ingreso_erroneo_falta_numero()

        elif len(x) > 10:
            mn.ingreso_erroneo_demasiado_numero()

        limpiar()
        print(espacio0)
        print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
        print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
        print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_cliente,'  |'))
        print('|  Cedula',end='')
        x = input(':')
    
    return x


def correcion_nombre():
    print('|  Nombre del cliente',end='')
    nombre_cliente = input(': ')
    patron = r'[A-Za-zÁÉÍÓÚÜáéíóúüÑñ\s]+$'

    if re.match(patron,nombre_cliente):
        nombre_cliente = nombre_cliente.lower().title()
    else:
        a = False
        while a == False:
            limpiar()
            print(espacio0)
            faux.relleno_n(tamaño_g,2)
            print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','  |'))
            print(faux.calculo_tamaño0(tamaño_g,'|','NO INGRESE NUMEROS NI SIMBOLOS','|'))
            faux.relleno_n(tamaño_g,2)
            print(espacio0)
            time.sleep(2)

            limpiar()
            print(espacio0)
            print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
            print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
            print('|  Nombre del cliente',end='')
            nombre_cliente = input(': ')
            if re.match(patron,nombre_cliente):
                nombre_cliente = nombre_cliente.lower().title()
                a = True

    numero_cedula = validacion_cedula(nombre_cliente)
    return nombre_cliente, numero_cedula

def validacion_telefono(nombre_cliente,numero_cedula):
    print('|  Numero telefonico',end='')
    numero = input(':')
    while numero.isdecimal() == False or len(numero) < 10 or len(numero) > 10:
        if len(numero) <= 14:
            if numero.find('+') == 0: #comprueba que comience con +
                patron = r'\+\d{11,13}' # regla para comprobar que despues del +, tenga 3 digitos para el pais y 10 para el numero telefonico
                if re.match(patron,numero):
                    return numero
        else:
            mn.ingreso_erroneo_demasiado_numero()

        if numero.find('+') == 0:
            if numero[1::].isdecimal() == False:
                mn.ingreso_erroneo_numero_no_letras()
            elif len(numero) < 10:
                mn.ingreso_erroneo_falta_numero()
        elif len(numero) < 10:
            mn.ingreso_erroneo_falta_numero()

        limpiar()
        print(espacio0)
        print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
        print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
        print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_cliente, 'Cedula: ' + numero_cedula + '  |'))
        print('|  Numero de telefonico',end='')
        numero = input(':')
    
    return numero

def validacion_correo(nombre_cliente,numero_cedula,numero_tel_cliente):
    print('|  Correo electronico',end='')
    x = input(':')

    #define la expresión regular para un correo electrónico válido
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 

    if re.match(patron, x):# Usa re.match() para comprobar si el correo coincide con el patrón
        return x
    else:
        while True:
            limpiar()
            print(espacio0)
            faux.relleno_n(tamaño_g,2)
            print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','|'))
            print(faux.calculo_tamaño0(tamaño_g,'|','EN EL CORREO ELECTRONICO','|'))
            faux.relleno_n(tamaño_g,2)
            print(espacio0)
            time.sleep(2)

            limpiar()
            print(espacio0)
            print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
            print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
            print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_cliente, 'Cedula: ' + numero_cedula + '  |'))
            print(faux.calculo_tamaño(tamaño_g,'|  Numero de telefono: ' + numero_tel_cliente, '  |'))
            print('|  Correo electronico',end='')
            x = input(':')
            if re.match(patron, x):# Usa re.match() para comprobar si el correo coincide con el patrón
                break
        return x

ancho, altura = faux.tamaño() #definimos el ancho y la altura
tamaño_g = faux.tamaño_general(ancho)
fecha_hf = faux.fecha_hoy()# Obtener la fecha de hoy
espacio0 = faux.cantidad_apostrofe(tamaño_g)

#--------------------- variables encabezado venta -------------------
ubicacion = mn.ubicacion_data()
pais = mn.pais_data(ubicacion)
region = mn.region_data(ubicacion)
ciudad = mn.ciudad_data(ubicacion)
orden_compra = 0 #numero de factura