import os 
import funciones_auxiliares

ancho, altura = funciones_auxiliares.tamaño()

funciones_auxiliares.menu_principal()
seleccion_0 = funciones_auxiliares.Validacion_texto_0()

if seleccion_0 == 'n':
    funciones_auxiliares.menu_final()
else:
    funciones_auxiliares.menu_inicio()
    seleccion_01 = funciones_auxiliares.Validacion_texto_0()
    if seleccion_01 == 's':
        print("tuto")
    else:
        funciones_auxiliares.menu_inicio_0()
        seleccion_02 = funciones_auxiliares.Validacion_decicion_0()
        if seleccion_02 == 1: #ingresar valores y/o sobre escribir los escritos
            momentaneo = True
            funciones_auxiliares.menu_ingreso_general(momentaneo)
            seleccion_03 = funciones_auxiliares.Validacion_decicion_1()
            if seleccion_03 == 1:
                funciones_auxiliares.menu_ingreso_costos_directos()
                seleccion_04 = funciones_auxiliares.Validacion_decicion_0()
            else:
                funciones_auxiliares.menu_ingreso_costos_indirectos()
                seleccion_04 = funciones_auxiliares.Validacion_decicion_0()
        elif seleccion_02 == 2: #modificar valores ya establecidos
            momentaneo = False
            funciones_auxiliares.menu_ingreso_general(momentaneo)
            seleccion_03 = funciones_auxiliares.Validacion_decicion_1()
            if seleccion_03 == 1:
                funciones_auxiliares.menu_ingreso_costos_directos()
                seleccion_04 = funciones_auxiliares.Validacion_decicion_0()
            else:
                funciones_auxiliares.menu_ingreso_costos_indirectos()
                seleccion_04 = funciones_auxiliares.Validacion_decicion_0()
        elif seleccion_02 == 3:
            print('xd')