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
        limpiar()
        mn.menu_principal()
        x = input(': ').lower()
    return x

def validacion_otra_compra():
    x = input('| : ').lower()
    while x != 's' and x != 'n':
        mn.ingreso_erroneo_fuera_rango_letra()
        limpiar()
        mn.asegurar_orde_compra()
        x = input('|: ').lower()
    return x

def validacion_siguiente():
    mn.menu_siguiente()
    x = int(input(': '))
    while x < 1 or x > 2:
        mn.ingreso_erroneo_fuera_rango()
        limpiar()
        mn.menu_siguiente()
        x = int(input(': '))

def Validacion_orden_final(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente,ruta,camaron_t,cant_compra,cant_camion,precio_ruta,sub_total,iva,total_final):
    x = input(': ').lower()
    while x != 's' and x != 'x' and x != 'n':
        mn.ingreso_erroneo_fuera_rango_letra()
        limpiar()
        mn.menu_orden_compra_parte1(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente)
        mn.menu_orden_compra_parte2(ruta,camaron_t,cant_compra)
        mn.menu_orden_compra_parte3()
        mn.menu_orden_compra_parte4(cant_camion, precio_ruta, sub_total)
        mn.menu_orden_compra_parte5(sub_total,iva,total_final)
        x = input(': ').lower()
    return x

def Validacion_orden_final_masiva(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente,sub_total,iva,total_final,pedidos):
    x = input(': ').lower()
    while x != 's' and x != 'x' and x != 'n':
        mn.ingreso_erroneo_fuera_rango_letra()
        limpiar()
        mn.menu_orden_compra_parte1(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente)
        mn.mostar_menu_orden_compra_masiva(pedidos,sub_total,iva,total_final)
        x = input(': ').lower()
    return x

def Validacion_decicion_0():#seleccion del menu principal
    while True:
        try:
            x = input(':').lower()
            if x.isdigit():
                x = int(x)
                while x < 1 or x > 4:
                    mn.ingreso_erroneo_fuera_rango()
                    mn.menu_inicio_0()
                    x = input(':')
                    if x.isalpha():
                        if x == 'x':
                            break
                    if x.isdigit:
                        x = int(x)
            else:
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    mn.menu_inicio_0()
                    x = input(':').lower()
                    if x.isdigit():
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
            if x.isdigit():
                x = int(x)
                while x < 1 or x > 3:
                    mn.ingreso_erroneo_fuera_rango()
                    mn.menu_costos_directos()
                    x = input(':')
                    if x.isalpha():
                        if x == 'x':
                            break
                    if x.isdigit:
                        x = int(x)
            else:
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    mn.menu_costos_directos()
                    x = input(':').lower()
                    if x.isdigit():
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
                    if x.isalpha():
                        if x == 'x':
                            break
                    if x.isdigit:
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
                    if x.isalpha():
                        if x == 'x':
                            break
                    if x.isdigit:
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
                    if x.isalpha():
                        if x == 'x':
                            break
                    if x.isdigit:
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
                    if x.isalpha():
                        if x == 'x':
                            break
                    if x.isdigit:
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
                    if x.isalpha():
                        if x == 'x':
                            break
                    if x.isdigit:
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
                    if x.isalpha():
                        if x == 'x':
                            break
                    if x.isdigit:
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
                    if x.isalpha():
                        if x == 'x':
                            break
                    if x.isdigit:
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
                    if x.isalpha():
                        if x == 'x':
                            break
                    if x.isdigit:
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
                    if x.isalpha():
                        if x == 'x':
                            break
                    if x.isdigit:
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

def validacion_menu_modificacion():
    while True:
        try:
            x = input(': ').lower()
            if x == 'x':
                return x
                break
            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 5:
                    mn.ingreso_erroneo_fuera_rango()
                    limpiar()
                    mn.menu_modificacion()
                    x = input(': ').lower()
                    if x.isalpha():
                        if x == 'x':
                            break
                    if x.isdigit:
                        x = int(x)
                return x
        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x

def validacion_menu_consulta():
    while True:
        try:
            x = input(': ').lower()
            if x == 'x':
                return x
                break
            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 5:
                    mn.ingreso_erroneo_fuera_rango()
                    limpiar()
                    mn.menu_consulta()
                    x = input(': ').lower()
                    if x.isalpha():
                        if x == 'x':
                            break
                    if x.isdigit:
                        x = int(x)
                return x
        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x

def validacion_busqueda_consulta_numero_factura():
    while True:
        mn.menu_modificacion()
        mn.menu_busqueda_numero_factura()
        x = input(':').lower()
        if x.isalpha():
            if x == 'x':
                return x
            else:
                mn.ingreso_erroneo_numero_no_letras()
                
        if x.isdigit():
            return x

def validacion_busqueda_consulta_cedula():
    while True:
        mn.menu_modificacion()
        mn.menu_busqueda_cedula()
        x = input(':').lower()
        if x.isalpha():
            if x == 'x':
                return x
            else:
                mn.ingreso_erroneo_numero_no_letras()
                
        if x.isdigit():
            s = validacion_cedula(x)
            if s == True:
                return x
            else:
                mn.ingreso_erroneo_cedula()

#------------------------------------
def validacion_nombre():
    print('|  Nombre del cliente',end='')
    nombre_cliente = input(': ')
    patron = r'[A-Za-zÁÉÍÓÚÜáéíóúüÑñ\s]+$'

    if nombre_cliente == 'x':
        return False

    if re.match(patron,nombre_cliente):
        nombre_cliente = nombre_cliente.lower().title()
    else:
        a = False
        while a == False:
            mn.ingreso_erroneo_numero_no_letras()
            mn.menu_orden_compra_nombre()
            print('|  Nombre del cliente',end='')
            nombre_cliente = input(': ')
            if nombre_cliente == 'x':
                return False
            
            if re.match(patron,nombre_cliente):
                nombre_cliente = nombre_cliente.lower().title()
                a = True

    return nombre_cliente

def validacion_cedula(cedula):
    digitos = [int(d) for d in cedula]# Extraer los dígitos de la cédula
    digito_verificador = digitos[-1]# Obtener el dígito verificador

    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]# Coeficientes para la validación

    # Sumar los productos de los coeficientes y los dígitos, ajustando según las reglas
    suma = 0
    for i in range(9):
        producto = coeficientes[i] * digitos[i]
        if producto >= 10:
            producto -= 9
        suma += producto

    # Calcular el dígito validador esperado
    digito_calculado = 10 - (suma % 10)
    if digito_calculado == 10:
        digito_calculado = 0

    # Verificar si el dígito verificador es igual al calculado
    if digito_verificador == digito_calculado:
        return True
    else:
        return False

def validacion_cedula_f(nombre_cliente):
    while True:
        mn.menu_orden_compra_cedula(nombre_cliente)
        print('|  Cedula',end='')
        x = input(':')
        if x == 'x':
            return False
        while len(x) < 10 or x.isdecimal() == False or len(x) > 10:
            if x.isalpha():
                if x == 'x':
                    return False
                else:
                    mn.ingreso_erroneo_numero_no_letras()
            elif len(x) < 10:
                mn.ingreso_erroneo_falta_numero()
            elif len(x) > 10:
                mn.ingreso_erroneo_demasiado_numero()
            mn.menu_orden_compra_cedula(nombre_cliente)
            print('|  Cedula',end='')
            x = input(':')
            s = validacion_cedula(x)
            if s == True:
                return x
                break
            else:
                mn.ingreso_erroneo_cedula()
        s = validacion_cedula(x)
        if s == True:
            return x
        else:
            mn.ingreso_erroneo_cedula()

def validacion_telefono(nombre_cliente,numero_cedula):
    while True:
        print('|  Numero telefonico',end='')
        numero = input(':')
        while numero.isdecimal() == False or len(numero) < 10 or len(numero) > 10:

            if numero == 'x':
                return False

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
            mn.menu_orden_compra_numero_telefonico(nombre_cliente, numero_cedula)
            print('|  Numero de telefonico',end='')
            numero = input(':')

        return numero

def validacion_correo(nombre_cliente,numero_cedula,numero_tel_cliente) :
    print('|  Correo electronico',end='')
    x = input(':')

    if x == 'x':
        return False
    
    #define la expresión regular para un correo electrónico válido
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 

    if re.match(patron, x):# Usa re.match() para comprobar si el correo coincide con el patrón
        return x
    else:
        while True:
            mn.ingreso_erroneo_correo()
            mn.menu_orden_compra_correo(nombre_cliente, numero_cedula, numero_tel_cliente)
            print('|  Correo electronico',end='')
            x = input(':')
            
            if x == 'x':
                return False
            if re.match(patron, x):# Usa re.match() para comprobar si el correo coincide con el patrón
                break
        return x

def validacion_rutas():
    while True:
        try:
            x = input(':').lower()
            if x.isdigit():
                x = int(x)
                while x < 1 or x > 8:
                    mn.ingreso_erroneo_fuera_rango()
                    limpiar()
                    print(espacio0)
                    mn.menu_rutas()
                    x = input(':').lower()
                    if x.isalpha():
                        if x == 'x':
                            break
                    if x.isdigit:
                        x = int(x)
                
            else:
                if x == 'x':
                    return x
                    break
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    limpiar()
                    mn.menu_rutas()
                    x = input(':').lower()
                    if x.isdigit() :
                        mn.confirmacion()
                        break
                
        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x
        break
        
def validacion_tipos_camaron():
    while True:
        try:
            x = input(':').lower()

            if x.isdigit() == True:
                x = int(x)
                while x < 1 or x > 2:
                    mn.ingreso_erroneo_fuera_rango()
                    limpiar()
                    mn.menu_tipo_camaron()
                    x = input(':')
                    if x.isalpha():
                        if x == 'x':
                            break
                    if x.isdigit:
                        x = int(x)
            else:
                if x == 'x':
                    return x
                    break
                while x != 'x':
                    mn.ingreso_erroneo_fuera_rango_letra()
                    limpiar()
                    mn.menu_tipo_camaron()
                    x = input(':').lower()
                    if x.isdigit() == True:
                        if x == 'x':
                            return x
                            break

        except ValueError:
            mn.ingreso_erroneo_tipo_dato()
            continue
        return x
        break

def validacion_cantidad_carga():
    while True:
        try:
            x = input(': ').lower()
            if x == 'x':
                return x
                break
            if x.isdigit() == True:
                x = int(x)
                while x < 1:
                    mn.ingreso_erroneo_fuera_rango()
                    limpiar()
                    mn.menu_cantidad_compra()
                    x = input(':')
                    if x.isalpha():
                        if x == 'x':
                            break
                        else:
                            mn.ingreso_erroneo_numero_no_letras()
                    if x.isdigit:
                        x = int(x)
                x = str(x)
                return x
                break
                
        except ValueError:
            mn.ingreso_erroneo_numero_no_letras()
            continue
        return x

def validacion_telefono(nombre_cliente,numero_cedula):
    while True:
        print('|  Numero telefonico',end='')
        numero = input(':')
        while numero.isdecimal() == False or len(numero) < 10 or len(numero) > 10:

            if numero == 'x':
                return False

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
            mn.menu_orden_compra_numero_telefonico(nombre_cliente, numero_cedula)
            print('|  Numero de telefonico',end='')
            numero = input(':')

        return numero

def validacion_correo(nombre_cliente,numero_cedula,numero_tel_cliente) :
    print('|  Correo electronico',end='')
    x = input(':')

    if x == 'x':
        return False
    
    #define la expresión regular para un correo electrónico válido
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 

    if re.match(patron, x):# Usa re.match() para comprobar si el correo coincide con el patrón
        return x
    else:
        while True:
            mn.ingreso_erroneo_correo()
            mn.menu_orden_compra_correo(nombre_cliente, numero_cedula, numero_tel_cliente)
            print('|  Correo electronico',end='')
            x = input(':')
            
            if x == 'x':
                return False
            if re.match(patron, x):# Usa re.match() para comprobar si el correo coincide con el patrón
                break
        return x
    
#------------------------------------------------------------------ EMPRESA -------------------------------------------------------------------
#------------------------ RUC
def validacion_empresa_nombre():
    print('|  Nombre de la empresa',end='')
    nombre_empresa = input(': ')
    patron = r'[A-Za-zÁÉÍÓÚÜáéíóúüÑñ\s]+$'

    if nombre_empresa == 'x':
        return False

    if re.match(patron,nombre_empresa):
        nombre_empresa = nombre_empresa.lower().title()
    else:
        a = False
        while a == False:
            mn.ingreso_erroneo_numero_no_letras()
            mn.menu_orden_compra_empresa_nombre()
            print('|  Nombre de la empresa',end='')
            nombre_empresa = input(': ')
            if nombre_empresa == 'x':
                return False
            
            if re.match(patron,nombre_empresa):
                nombre_empresa = nombre_empresa.lower().title()
                a = True

    return nombre_empresa

def validacion_empresa_encargado(nombre_empresa,ruc):
    print('|  Nombre del cliente',end='')
    nombre_cliente = input(': ')
    patron = r'[A-Za-zÁÉÍÓÚÜáéíóúüÑñ\s]+$'

    if nombre_cliente == 'x':
        return False

    if re.match(patron,nombre_cliente):
        nombre_cliente = nombre_cliente.lower().title()
    else:
        a = False
        while a == False:
            mn.ingreso_erroneo_numero_no_letras()
            mn.menu_orden_compra_empresa_encargado(nombre_empresa,ruc)
            print('|  Nombre del cliente',end='')
            nombre_cliente = input(': ')
            if nombre_cliente == 'x':
                return False
            
            if re.match(patron,nombre_cliente):
                nombre_cliente = nombre_cliente.lower().title()
                a = True

    return nombre_cliente

def validacion_ruc(nombre_empresa):
    while True:
        try:
            print('|  RUC',end='')
            x = input(': ').lower()
            if x == 'x':
                return x
                break
            if x.isdigit():
                seguro = False
                while len(x) != 13  and seguro == False:
                    mn.ingreso_erroneo_ruc()
                    limpiar()
                    mn.menu_orden_compra_empresa_ruc(nombre_empresa)
                    print('|  RUC:',end='')
                    x = input(':')
                    if x.isalpha():
                        if x == 'x':
                            break
                        else:
                            mn.ingreso_erroneo_letras_ruc(nombre_empresa)
                    seguro = validacion_ruc_f(x)
                    
            else:
                mn.ingreso_erroneo_letras_ruc()
                break
                
        except ValueError:
            mn.ingreso_erroneo_numero_no_letras()
            continue
        return x

def validacion_ruc_f(ruc):

    provincia = int(ruc[0:2])
    if provincia < 1 or provincia > 24:
        mn.ingreso_erroneo_provincia_ruc()
        return False
    
    tercer_digito = int(ruc[2])
    if tercer_digito < 0 or tercer_digito > 6 and tercer_digito != 9:
        return False

    if ruc[10:13] != "001":
        mn.ingreso_erroneo_establecimiento_ruc()
        return False

    def validar_cedula(cedula):
        if len(cedula) != 10 or not cedula.isdigit():
            return False
        coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
        suma = 0
        for i in range(9):
            producto = int(cedula[i]) * coeficientes[i]
            suma += producto if producto < 10 else producto - 9
        digito_verificador = (10 - (suma % 10)) % 10
        return digito_verificador == int(cedula[9])

    if not validar_cedula(ruc[:10]):
        mn.ingreso_erroneo_cedula_ruc()
        return False

    return True

def validacion_empresa_cedula_f(nombre_empresa,ruc,nombre_encargado):
    while True:
        mn.menu_orden_compra_empresa_cedula(nombre_empresa,ruc,nombre_encargado)
        print('|  Cedula',end='')
        x = input(':')
        if x == 'x':
            return False
        while len(x) < 10 or x.isdecimal() == False or len(x) > 10:
            if x.isalpha():
                if x == 'x':
                    return False
                else:
                    mn.ingreso_erroneo_numero_no_letras()
            elif len(x) < 10:
                mn.ingreso_erroneo_falta_numero()
            elif len(x) > 10:
                mn.ingreso_erroneo_demasiado_numero()
            mn.menu_orden_compra_empresa_cedula(nombre_empresa,ruc,nombre_encargado)
            print('|  Cedula',end='')
            x = input(':')
            s = validacion_cedula(x)
            if s == True:
                return x
                break
            else:
                mn.ingreso_erroneo_cedula()
        s = validacion_cedula(x)
        if s == True:
            return x
        else:
            mn.ingreso_erroneo_cedula()

def validacion_empresa_telefono(nombre_empresa,ruc,nombre_encargado, numero_cedula):
    while True:
        print('|  Numero telefonico',end='')
        numero = input(':')
        while numero.isdecimal() == False or len(numero) < 10 or len(numero) > 10:

            if numero == 'x':
                return False

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
            mn.menu_orden_compra_empresa_numero_telefonico(nombre_empresa,ruc,nombre_encargado, numero_cedula)
            print('|  Numero de telefonico',end='')
            numero = input(':')

        return numero
    
def validacion_empresa_correo(nombre_empresa,ruc,nombre_encargado, numero_cedula, numero_tel_cliente) :
    print('|  Correo electronico',end='')
    x = input(':')

    if x == 'x':
        return False
    
    #define la expresión regular para un correo electrónico válido
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 

    if re.match(patron, x):# Usa re.match() para comprobar si el correo coincide con el patrón
        return x
    else:
        while True:
            mn.ingreso_erroneo_correo()
            mn.menu_orden_compra_empresa_correo(nombre_empresa,ruc,nombre_encargado, numero_cedula, numero_tel_cliente)
            print('|  Correo electronico',end='')
            x = input(':')
            
            if x == 'x':
                return False
            if re.match(patron, x):# Usa re.match() para comprobar si el correo coincide con el patrón
                break
        return x

def Validacion_orden_empresa_final(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente,ruta,camaron_t,cant_compra,cant_camion,precio_ruta,sub_total,iva,total_final):
    x = input(': ').lower()
    while x != 's' and x != 'x' and x != 'n':
        mn.ingreso_erroneo_fuera_rango_letra()
        limpiar()
        mn.menu_orden_compra_empresa_parte1(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente)
        mn.menu_orden_compra_parte2(ruta,camaron_t,cant_compra)
        mn.menu_orden_compra_parte3()
        mn.menu_orden_compra_parte4(cant_camion, precio_ruta, sub_total)
        mn.menu_orden_compra_parte5(sub_total,iva,total_final)
        x = input(': ').lower()
    return x

def Validacion_orden_empresa_final_masiva(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente,sub_total,iva,total_final,pedidos):
    x = input(': ').lower()
    while x != 's' and x != 'x' and x != 'n':
        mn.ingreso_erroneo_fuera_rango_letra()
        limpiar()
        mn.menu_orden_compra_empresa_parte1(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente)
        mn.mostar_menu_orden_compra_masiva(pedidos,sub_total,iva,total_final)
        x = input(': ').lower()
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
orden_compra = faux.numero_orden() #numero de factura