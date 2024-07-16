import time
import os
#verificacion que todo funcione bien
def limpiar():
    os.system('cls')

#--------------- CALCULOS -----------------------------
#comprueba el tamaño de la ventana del cmd
def tamaño():
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
def tamaño0(ancho):
    signo0 = ''    
    for i in range(ancho):
        signo0 += '-'
    
    return signo0

#cantidad de espacios
def tamaño00(signo0):
    signo00 = ''
    
    if len(signo0) <= 120:
        signo0 = len(signo0) // 3
    else:
        signo0 = int(len(signo0) // 2.5)

    for i in range(signo0 - 2):
        signo00 += ' '

    return signo00



#------------- VALIDACIONES --------------------
#inicio del sistemas
def Validacion_texto_0():
    x = input(': ').lower()
    while x != 's' and x != 'n':
        print('\nIngreso Erroneo')
        x = input(': ').lower()
    return x

def Validacion_decicion_0():
    while True:
        try:
            x = int(input(':'))
            while x < 1 or x > 3:
                print('\nIngreso Erroneo')
                x = int(input(':'))
        except ValueError:
            print('\nIngreso Erroneo')
            continue
        return x
        break

def Validacion_decicion_1():
    while True:
        try:
            x = int(input(':'))
            while x < 1 or x > 2:
                print('\nIngreso Erroneo')
                x = int(input(':'))
        except ValueError:
            print('\nIngreso Erroneo')
            continue
        return x
        break

#------------ VARIABLE PRE-CARGA ----------------
x0 = '|\n|\n|\n|'
#--------------- MENUS -------------------------
def menu_principal():
    limpiar()
    print(signo0)#100 unidades
    #print('|       |       |       |       |       |       |       |       |       |') # un tab son 7  espacios
    print(x0,signo00,'PROTOTIPO 1 DEL SISTEMA DE REGISTRO DE COSTOS')
    print('|\n|',signo00,'\t DESEA ABRIR EL SISTEMA [S/N]\n|')
    print(x0,signo00,'\t\t\t\t\t\t hecho por el grupo #3')
    print(signo0)

def menu_final():
    limpiar()
    print(signo0)
    print(x0,signo00,'\tGRACIAS POR ABRIR EL SISTEMA\n',x0)
    print(signo0)

def menu_inicio():
    limpiar()
    print(signo0)
    print(x0,signo00,'\tBIENVENIDO AL SISTEMA')
    print('| ',signo00,'ES SU PRIMERA VEZ CON EL SISTEMA [S/N]\n',x0, sep='')
    print(signo0)
    
def menu_inicio_0():
    limpiar()
    print(signo0)
    print(x0,signo00,'OPCIONES:\n',x0,signo00,'1  INGRESO DE DATOS\n','|',signo00,
          '2  MODIFICACION DE DATOS\n','|',signo00,'3  VISUALIZACION DE INFORME\n',x0,sep='')
    print(signo0)

def menu_ingreso_general(x):
    limpiar()
    if x == True:
        y = 'INGRESO'
    else:
        y = 'MODIFICACION'
    print(signo0)
    print(x0,signo00,y,' DE DATOS\n','|',signo00,'SELECCIONE UNA OPCION:',x0,signo00,'1  COSTOS DIRECTOS\n','|',signo00,
          '2  COSTOS INDIRECTOS\n',x0,sep='')
    print(signo0)

def menu_ingreso_costos_directos():
    limpiar()
    print(signo0)
    print(x0,'\n|',signo00,'COSTOS DIRECTOS\n','|',signo00,'SELECCIONE UNA OPCION:\n','|\n|',signo00,
          '1   COSTOS DE VIAJES\n','|',signo00,'2   INFORMACION DE VEHICULOS\n','|',signo00,'3   SEGUROS\n',x0,sep='')
    print(signo0)

def menu_ingreso_costos_indirectos():
    limpiar()
    print(signo0)
    print(x0,'\n|',signo00,'COSTOS INDIRECTOS\n','|',signo00,'SELECCIONE UNA OPCION:\n','|\n|',signo00,
          '1   GASTOS ADMINISTRATIVOS\n','|',signo00,'2   PEAJES\n','|',signo00,'3   ENERGIA\n',x0,sep='')
    print(signo0)

#----------------------------------------------------------------------
#------------ variables Necesarias ----------------------------
ancho, altura = tamaño() #definimos el ancho y la altura
signo0 = tamaño0(ancho) #cantidad de apostrofe
signo00 = tamaño00(signo0) #cantidad de espacios