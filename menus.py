import time
#import re
import requests
import funciones_auxiliares as faux
import validaciones as val



#----------------- OBTENER LA DIRECCION IP PUBLICA PARA LA GEOLOCALIZACION -----------------

def ubicacion_data():
    # haciendo una petición GET a la API de ipify. Esta API devuelve nuestra dirección IP pública en formato json
    ip_r = requests.get('https://api.ipify.org?format=json')
    
    #La respuesta de la API se convierte a un diccionario de Python usando el método .json().
    ip_d = ip_r.json() 
    
    # extraemos el value de 'ip' en el diccionario anterior
    ip_address = ip_d['ip']
    
    # haciendo una petición GET a la API de ipinfo.io usando la dirección IP obtenida en el paso anterior 
    # y aseguramos que esté en formato JSON.
    location_r = requests.get(f'https://ipinfo.io/{ip_address}/json') 
    #La respuesta de la API se convierte a un diccionario de Python usando el método .json().
    ubicacion_data = location_r.json()

    return ubicacion_data

def limpiar():
    faux.limpiar()

# extraemos con el metodo 'get', el nombre de la ciudad, la region y el pais
def ciudad_data(ubicacion_data) -> str:
    ubicacion = ubicacion_data.get('city', 'Desconocida')
    return ubicacion

def region_data(ubicacion_data) -> str:
    region = ubicacion_data.get('region', 'Desconocida')
    return region 

def pais_data(ubicacion_data) -> str:
    pais = ubicacion_data.get('country', 'Desconocida')
    return pais 

#---------------------------------------- MENUS ----------------------------------------
def menu_principal():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,2)
    print(faux.calculo_tamaño0(tamaño_g,'|','SISTEMA DE REGISTRO DE COSTOS','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','DESEA ABRIR EL SISTEMA [S/N]','|'))
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|','','hecho por el grupo #3  |'))
    print(espacio0)

def menu_final():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|','GRACIAS POR ABRIR EL SISTEMA','|'))
    faux.relleno_n(tamaño_g,3)
    print(espacio0)
    
def menu_inicio_0():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','SISTEMA DE REGISTRO DE COSTOS','|'))
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','OPCIONES:                  ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','1  COSTOS DIRECTOS         ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','2  COSTOS INDIRECTOS       ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','3  PEDIDO                  ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','4  VISUALIZACION DE INFORME','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)

def menu_costos_directos():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','COSTOS DIRECTOS','|'))
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','SELECCIONE UNA OPCION:      ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','1   COSTOS DE VIAJES        ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','2   INFORMACION DE VEHICULOS','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','3   SEGUROS                 ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    print(espacio0)

def menu_costos_directos_1():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','COSTOS DE VIAJES','|'))
    faux.relleno_n(tamaño_g,1)  
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)    
    print(espacio0)

def menu_costos_directos_2():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INFORMACION DE VEHICULOS','|'))
    faux.relleno_n(tamaño_g,1)  
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)    
    print(espacio0)

def menu_costos_directos_3():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','SEGUROS','|'))
    faux.relleno_n(tamaño_g,1)  
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)    
    print(espacio0)

def menu_costos_indirectos():
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño0(tamaño_g,'|','COSTOS INDIRECTOS','|'))
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','SELECCIONE UNA OPCION:    ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','1   GASTOS ADMINISTRATIVOS','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','2   PEAJES                ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','3   ENERGIA               ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    print(espacio0)

def menu_costos_indirectos_1():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','GASTOS ADMINISTRATIVOS','|'))
    faux.relleno_n(tamaño_g,1)  
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)    
    print(espacio0)

def menu_costos_indirectos_2():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','PEAJES','|'))
    faux.relleno_n(tamaño_g,1)  
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)    
    print(espacio0)

def menu_costos_indirectos_3():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','ENERGIA','|'))
    faux.relleno_n(tamaño_g,1)  
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)    
    print(espacio0)

def menu_pedido():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','OPCIONES PEDIDOS','|'))
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','SELECCIONE UNA OPCION:     ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','1   INGRESO DE PEDIDO      ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','2   MODIFICACION DE PEDIDO ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','3   ELIMINACION DE PEDIDO  ','|'))  
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))  
    faux.relleno_n(tamaño_g,1)    
    print(espacio0)

def menu_pedido_ingreso():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','PARA QUIEN ES EL PEDIDO?','|'))
    faux.relleno_n(tamaño_g,1)  
    print(faux.calculo_tamaño0(tamaño_g,'|','SELECCIONE UNA OPCION:     ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','1   PEDIDO PARA EMPRESA    ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','2   PEDIDO PARA UNA PERSONA','|'))  
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))   
    faux.relleno_n(tamaño_g,1)    
    print(espacio0)

def menu_pedido_modificacion():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','MODIFICAR PEDIDO','|'))
    faux.relleno_n(tamaño_g,1)  
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)    
    print(espacio0)

def menu_pedido_eliminar():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','ELIMINAR PEDIDO','|'))
    faux.relleno_n(tamaño_g,1)  
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)    
    print(espacio0)

def confirmacion():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','POR FAVOR VUELVA A INGRESAR','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','SU OPCION PARA CONFIRMAR','|'))    
    faux.relleno_n(tamaño_g,1)    
    print(espacio0)
    time.sleep(2)    

def ingreso_erroneo_fuera_rango():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','EL NUMERO INGRESADO ESTA FUERA DE RANGO','|'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)
    time.sleep(2)

def ingreso_erroneo_fuera_rango_letra():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','LA LETRA INGRESADO ESTA FUERA DE RANGO','|'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)
    time.sleep(2)

def ingreso_erroneo_tipo_dato():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','TIPO DE DATO INCORRECTO','|'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)
    time.sleep(2)

def ingreso_erroneo_numero_no_letras():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESE NUMEROS, NO LETRAS','|'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)
    time.sleep(2)

def ingreso_erroneo_falta_numero():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','FALTA NUMEROS','|'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)
    time.sleep(2)

def ingreso_erroneo_demasiado_numero():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','DEMACIADO NUMEROS','|'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)
    time.sleep(2)

def menu_rutas():
    print(faux.calculo_tamaño0(tamaño_g,'|','  Seleccione una ruta:               ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','        1.- Guayaquil a Cuenca       ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','        2.- Guayaquil a Quevedo      ','|'))    
    print(faux.calculo_tamaño0(tamaño_g,'|','        3.- Guayaquil a Quito        ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','        4.- Guayaquil a Ambato       ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','        5.- Guayaquil a Santo Domingo','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','        6.- Guayaquil a Loja         ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','        7.- Guayaquil a Machala      ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','        8.- Guayaquil a Salinas      ','|'))

def menu_tipo_camaron():
    print('camaron')

def menu_orden_compra_encabezado_cliente():
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    nombre_cliente, numero_cedula = val.correcion_nombre()
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_cliente, 'Cedula: ' + numero_cedula + '  |'))
    numero_tel_cliente = val.validacion_telefono(nombre_cliente,numero_cedula)
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_cliente, 'Cedula: ' + numero_cedula + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Numero de telefono: ' + numero_tel_cliente, '  |'))
    correo_cliente = val.validacion_correo(nombre_cliente,numero_cedula,numero_tel_cliente)
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_cliente, 'Cedula: ' + numero_cedula + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Numero de telefono: ' + numero_tel_cliente, '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Correo electronico: ' + correo_cliente, '  |'))
    return fecha_hf, orden_compra, pais, region, ciudad, nombre_cliente, numero_cedula, numero_tel_cliente, correo_cliente

def menu_orden_compra_encabezado_cliente_final(fecha_hf,orden_compra,pais,region,ciudad,nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente):
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_cliente, 'Cedula: ' + numero_cedula + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Numero de telefono: ' + numero_tel_cliente, '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Correo electronico: ' + correo_cliente, '  |'))
    
def menu_orden_compra_cuerpo_general():
    menu_rutas()
    menu_tipo_camaron()

#----------------------------------------------------------------------
#------------ variables Necesarias ----------------------------
ancho, altura = faux.tamaño() #definimos el ancho y la altura
tamaño_g = faux.tamaño_general(ancho)
espacio0 = faux.cantidad_apostrofe(tamaño_g) # cantidad de apostrofes

#------------ variables encabezado ventas --------------------
fecha_hf = faux.fecha_hoy()# Obtener la fecha de hoy
ubicacion = ubicacion_data()
ciudad = ciudad_data(ubicacion)
region = region_data(ubicacion)
pais = pais_data(ubicacion)
orden_compra = 0 #numero de factura