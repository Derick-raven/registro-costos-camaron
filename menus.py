import time
import requests
import funciones_auxiliares as faux
from colorama import Fore



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

#------------------------------------------------------ MENUS PRINCIPALES ---------------------------------------------------
def menu_principal():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,2)
    print(faux.calculo_tamaño0(tamaño_g,'|','SISTEMA DE REGISTRO DE COSTOS','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','DESEA ABRIR EL SISTEMA [S/N]','|'))
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|  hecho por el grupo #3','','INTEGRANTES:                          |'))
    print(faux.calculo_tamaño0(tamaño_g,'|','','García Portilla Britsney Valeria     |'))
    print(faux.calculo_tamaño0(tamaño_g,'|','','Navarrete Mayor Jorge Andrés         |'))
    print(faux.calculo_tamaño0(tamaño_g,'|','','Navas Muñoz Diego Enrique            |'))
    print(faux.calculo_tamaño0(tamaño_g,'|','','Núñez Vera Andrea Paulette           |'))
    print(faux.calculo_tamaño0(tamaño_g,'|','','Rosado Marriott Leonardo Derick      |'))
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
    faux.relleno_n(tamaño_g,1)
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
    print(faux.calculo_tamaño0(tamaño_g,'|','2   CONSULTA               ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','3   MODIFICACION DE PEDIDO ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','4   ELIMINACION DE PEDIDO  ','|'))  
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))  
    faux.relleno_n(tamaño_g,1)    
    print(espacio0)

#--------- COSTOS DIRECTOS -------------
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

#------------ COSTOS INDIRECTOS

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

#--------- OPCIONES PEDIDOS ------------
def menu_pedido_ingreso():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','PARA QUIEN ES EL PEDIDO?','|'))
    faux.relleno_n(tamaño_g,1)  
    print(faux.calculo_tamaño0(tamaño_g,'|','SELECCIONE UNA OPCION:     ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','1   PEDIDO PARA EMPRESA    ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','2   PEDIDO PARA UNA PERSONA','|'))  
    faux.relleno_n(tamaño_g,1)  
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

#---------------------------- MODIFICACION
def menu_modificacion():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,2)
    print(faux.calculo_tamaño0(tamaño_g,'|','OPCIONES DE MODIFICACION','|'))
    faux.relleno_n(tamaño_g,1)
#----------------------------- CONSULTA
def menu_consulta():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,2)
    print(faux.calculo_tamaño0(tamaño_g,'|','OPCIONES DE CONSULTA','|'))
    faux.relleno_n(tamaño_g,1)

#------------------------------------------------------------- TIPOS DE BUSQUEDAS ----------------------------------------
def menu_busqueda():
    print(faux.calculo_tamaño0(tamaño_g,'|','SELECCIONE UNA OPCION DE BUSQUEDA:','|'))
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','  1  FECHA             ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','  2  NUMERO DE FACTURA ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','  3  CEDULA            ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','  4  RUC               ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','  5  NOMBRE CLIENTE    ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','  6  NOMBRE EMPRESA    ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','  7  NUMERO TELEFONICO ','|'))
    faux.relleno_n(tamaño_g,2)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)

def menu_busqueda_numero_factura():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESE EL NUMERO DE FACTURA','|'))
    faux.relleno_n(tamaño_g,2)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)

def menu_busqueda_cedula():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESE NUMERO DE CEDULA','|'))
    faux.relleno_n(tamaño_g,2)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)

def menu_busqueda_ruc():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESE EL RUC','|'))
    faux.relleno_n(tamaño_g,2)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)

def menu_busqueda_nombre():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESE EL NOMBRE DEL CLIENTE','|'))
    faux.relleno_n(tamaño_g,2)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)

def menu_busqueda_telefono():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESE EL NUMERO TELEFONICO','|'))
    faux.relleno_n(tamaño_g,2)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)

# ------------------------ MENUS EXTRAS ------------------------
def confirmacion():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','POR FAVOR VUELVA A INGRESAR','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','SU OPCION PARA CONFIRMAR','|'))    
    faux.relleno_n(tamaño_g,1)    
    print(espacio0)
    time.sleep(2)    

#----------------------------------------------------------- MENUS TIPOS DE INGRESO --------------------------------------------
def ingreso_erroneo_fuera_rango():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','EL NUMERO INGRESADO ESTA FUERA DE RANGO','|'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)
    time.sleep(2)

def ingreso_erroneo_cedula():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','EL NUMERO INGRESADO NO ES CEDULA','|'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)
    time.sleep(2)

def ingreso_erroneo_ruc():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESE EL NUMERO CORRECTO DE NUMEROS EN EL RUC','|'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)
    time.sleep(2)

def ingreso_erroneo_letras_ruc():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESE NUMERO NO LETRAS EN EL RUC','|'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)
    time.sleep(2)

def ingreso_erroneo_provincia_ruc():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESE CORRECTAMENTE EL NUMERO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','DE PROVINCIA EN EL RUC','|'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)
    time.sleep(2)

def ingreso_erroneo_establecimiento_ruc():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','EL NUMERO DEL ESTABLECIMIENTO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','PRINCIPAL EN EL RUC','|'))
    faux.relleno_n(tamaño_g,1)
    print(espacio0)
    time.sleep(2)

def ingreso_erroneo_cedula_ruc():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','EL NUMERO DE CEDULA EN EL RUC','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','ES INCORRECTO','|'))
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
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESE NUMEROS, NO LETRAS, NI SIMBOLO','|'))
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

def ingreso_erroneo_correo():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,2)
    print(faux.calculo_tamaño0(tamaño_g,'|','INGRESO ERRONEO','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','EN EL CORREO ELECTRONICO','|'))
    faux.relleno_n(tamaño_g,2)
    print(espacio0)
    time.sleep(2)

def menu_siguiente():
    limpiar()
    print(espacio0)
    faux.relleno_n(tamaño_g,2)
    print(faux.calculo_tamaño0(tamaño_g,'|','SIGUIENTE ACCION ?      ','|'))
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','1  INGRESAR OTRA FACTURA','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','2  IR AL MENU PRINCIPAL ','|'))
    faux.relleno_n(tamaño_g,2)
    print(espacio0)
#------------------------------------------------------- FACTURA -------------------------------------------------------------------
# -------------------- ENCABEZADO DE LA FACTURA EMPRESA -----------------------------------
def menu_orden_compra_empresa_nombre() -> str:
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    faux.guardar_ultima_ubicacion(ciudad,region,pais)
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)

def menu_orden_compra_empresa_ruc(nombre_empresa) -> str:
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre de la empresa: ' + nombre_empresa ,'  |'))
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)

def menu_orden_compra_empresa_encargado(nombre_empresa,ruc) -> str:
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre de la empresa: ' + nombre_empresa ,'Ruc:' + ruc + '  |'))
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)

def menu_orden_compra_empresa_cedula(nombre_empresa,ruc,nombre_encargado) -> str:
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre de la empresa: ' + nombre_empresa ,'Ruc:' + ruc + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_encargado,'  |'))
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)

def menu_orden_compra_empresa_numero_telefonico(nombre_empresa,ruc,nombre_encargado, numero_cedula):
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre de la empresa: ' + nombre_empresa ,'Ruc:' + ruc + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_encargado, 'Cedula: ' + numero_cedula + '  |'))
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)

def menu_orden_compra_empresa_correo(nombre_empresa,ruc,nombre_encargado, numero_cedula, numero_tel_cliente):    
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre de la empresa: ' + nombre_empresa ,'Ruc:' + ruc + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_encargado, 'Cedula: ' + numero_cedula + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Numero de telefono: ' + numero_tel_cliente, '  |'))
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)

def menu_orden_compra_empresa_ruta(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente):
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre de la empresa: ' + nombre_empresa ,'Ruc:' + ruc + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_encargado, 'Cedula: ' + numero_cedula + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Numero de telefono: ' + numero_tel_cliente, '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Correo electronico: ' + correo_cliente, '  |'))

def menu_orden_compra_empresa_parte1(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente):
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre de la empresa: ' + nombre_empresa ,'Ruc:' + ruc + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_encargado, 'Cedula: ' + numero_cedula + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Numero de telefono: ' + numero_tel_cliente, '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Correo electronico: ' + correo_cliente, '  |'))


# -------------------- ENCABEZADO DE LA FACTURA PERSONA -----------------------------------
def menu_orden_compra_nombre() -> str:
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    faux.guardar_ultima_ubicacion(ciudad,region,pais)
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)

def menu_orden_compra_cedula(nombre_cliente):
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_cliente,'  |'))
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)
    #print(espacio0)

def menu_orden_compra_numero_telefonico(nombre_cliente, numero_cedula):
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_cliente, 'Cedula: ' + numero_cedula + '  |'))
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)

def menu_orden_compra_correo(nombre_cliente, numero_cedula, numero_tel_cliente):    
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_cliente, 'Cedula: ' + numero_cedula + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Numero de telefono: ' + numero_tel_cliente, '  |'))
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)

def menu_orden_compra_ruta(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente):
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_cliente, 'Cedula: ' + numero_cedula + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Numero de telefono: ' + numero_tel_cliente, '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Correo electronico: ' + correo_cliente, '  |'))

def menu_orden_compra_parte1(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente):
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_cliente, 'Cedula: ' + numero_cedula + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Numero de telefono: ' + numero_tel_cliente, '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Correo electronico: ' + correo_cliente, '  |'))

# ---------- CUERPO DE LA FACTURA -----------------------
def menu_orden_compra_camaron(ruta):
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Ruta: ' + ruta,'  |'))
    faux.relleno_n(tamaño_g,2)

def menu_orden_compra_cantidad_compra(ruta,camaron_t):
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Ruta: ' + ruta,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Tipo de camaron: ' + camaron_t,'  |'))
    faux.relleno_n(tamaño_g,1)

def menu_orden_compra_encabezado_cliente_final3(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente,ruta,camaron_t):
    limpiar()
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Fecha: ' + fecha_hf, 'N° factura: ' + str(orden_compra) + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Ubicacion: ' + pais + '-' + region + '-' + ciudad,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Nombre del cliente: ' + nombre_cliente, 'Cedula: ' + numero_cedula + '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Numero de telefono: ' + numero_tel_cliente, '  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Correo electronico: ' + correo_cliente, '  |'))
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Ruta: ' + ruta,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Tipo de camaron: ' + camaron_t,'  |'))
    faux.relleno_n(tamaño_g,4)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)

def menu_rutas():
    faux.relleno_n(tamaño_g,2)
    print(faux.calculo_tamaño0(tamaño_g,'|','  Seleccione una ruta:               ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','        1.- Guayaquil a Cuenca       ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','        2.- Guayaquil a Quevedo      ','|'))    
    print(faux.calculo_tamaño0(tamaño_g,'|','        3.- Guayaquil a Quito        ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','        4.- Guayaquil a Ambato       ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','        5.- Guayaquil a Santo Domingo','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','        6.- Guayaquil a Loja         ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','        7.- Guayaquil a Machala      ','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','        8.- Guayaquil a Salinas      ','|'))
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)

def menu_tipo_camaron():
    faux.relleno_n(tamaño_g,2)
    print(faux.calculo_tamaño0(tamaño_g,'|','TIPOS DE CAMARONES ','|'))    
    print(faux.calculo_tamaño0(tamaño_g,'|','1   tigre blanco   ','|'))    
    print(faux.calculo_tamaño0(tamaño_g,'|','2   tigre negro    ','|'))
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)

def menu_cantidad_compra() -> str:
    print(faux.calculo_tamaño0(tamaño_g,'|','','x para retroceder  |'))
    faux.relleno_n(tamaño_g,1)
    print('|  cantidad a comprar en kg',end='')

# ---------------- FINAL DE LA FACTURA ----------------------
def menu_orden_compra_parte2(ruta,camaron_t,cant_compra):
    print(espacio0)
    print(faux.calculo_tamaño(tamaño_g,'|  Ruta: ' + ruta,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Tipo de camaron: ' + camaron_t,'  |'))
    print(faux.calculo_tamaño(tamaño_g,'|  Cantidad comprada: ' + cant_compra + ' kg','|'))  

def menu_orden_compra_parte3() -> str:
    #print(espacio0)
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño_venta0(tamaño_g,'Cantidad Camion'), end='')
    print(faux.calculo_tamaño_venta0(tamaño_g,'Valor camion'), end='')
    print(faux.calculo_tamaño_venta0(tamaño_g,'Precio ruta'), end='')
    print(faux.calculo_tamaño_venta0(tamaño_g,'Sub precio'), Fore.WHITE + ' |' , sep='')    
    print(espacio0)

def menu_orden_compra_parte4(cant_camion, precio_ruta, sub_precio) -> str:
    #print(espacio0)
    #faux.relleno_n(tamaño_g,1)    
    print(faux.calculo_tamaño_venta0(tamaño_g,cant_camion), end='')
    print(faux.calculo_tamaño_venta0(tamaño_g,'$300'), end='')
    print(faux.calculo_tamaño_venta0(tamaño_g,'$' + precio_ruta), end='')
    print(faux.calculo_tamaño_venta0(tamaño_g,'$' + sub_precio), Fore.WHITE + ' |' , sep='')
    #print(espacio0)

def menu_orden_compra_parte5(sub_total,iva,total_final):
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|','                       |  Sub total   |','$' +   sub_total + '|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','                       |   Iva 15%    |','$' +         iva + '|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','                       | Total Final  |','$' + total_final + '|'))
    #print(faux.calculo_tamaño0(tamaño_g,'|','','|'))
    print(espacio0)

def mostar_menu_orden_compra_masiva(x:list,sub_total,iva,total_final):
    # x es una matriz n*6s
    for i in range(len(x)):
        menu_orden_compra_parte2(x[i][0],x[i][2],x[i][4])
        menu_orden_compra_parte3()
        menu_orden_compra_parte4(x[i][5],x[i][1],x[i][6])
    print(espacio0)
    menu_orden_compra_parte5(sub_total,iva,total_final)

def asegurar_orde_compra():
    faux.relleno_n(tamaño_g,2)
    print(faux.calculo_tamaño0(tamaño_g,'|','DESEA AÑADIR OTRO PEDIDO AL','|'))
    print(faux.calculo_tamaño0(tamaño_g,'|','    MISMO CLIENTE ? [S/N]    ','|'))
    faux.relleno_n(tamaño_g,2)  

def asegurar_orde_compra_final():
    faux.relleno_n(tamaño_g,3)
    print(faux.calculo_tamaño0(tamaño_g,'|','FINALIZAR FACTURA ? [S/N/X]','|'))
    faux.relleno_n(tamaño_g,1)
    print(faux.calculo_tamaño0(tamaño_g,'|    s para confirmar','n para eliminar todo','x para retroceder    |'))
    
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
orden_compra = faux.numero_orden()#numero de factura
#directorio_actual = faux.directorio_actual_data()