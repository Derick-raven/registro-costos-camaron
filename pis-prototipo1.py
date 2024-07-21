import funciones_auxiliares as aux
import validaciones as val
import menus as mn

ancho, altura = aux.tamaño()
while True:            
    mn.menu_principal()
    seleccion_principal = val.Validacion_texto_0()

    if seleccion_principal == 'n':
        mn.menu_final()
        break
    else:
        while True:
            mn.menu_inicio_0()
            seleccion_menu_inicio = val.Validacion_decicion_0()
            if seleccion_menu_inicio == 'x':
                break
            if seleccion_menu_inicio == 1: #modificacion de costos directos
                while True:
                    mn.menu_costos_directos()
                    seleccion_costos_directo = val.Validacion_decicion_directo()

                    if seleccion_costos_directo == 'x':
                        break
                    if seleccion_costos_directo == 1:
                        while True:
                            mn.menu_costos_directos_1()
                            seleccion_costos_directo_1 = val.Validacion_decicion_directo1()

                            if seleccion_costos_directo_1 == 'x':
                                break
                    elif seleccion_costos_directo == 2:
                        while True:
                            mn.menu_costos_directos_2()
                            seleccion_costos_directo_2 = val.Validacion_decicion_directo2()

                            if seleccion_costos_directo_2 == 'x':
                                break
                    elif seleccion_costos_directo == 3:
                        while True:
                            mn.menu_costos_directos_3()
                            seleccion_costos_directo_3 = val.Validacion_decicion_directo3()

                            if seleccion_costos_directo_3 == 'x':
                                break
            elif seleccion_menu_inicio == 2: #modificacion de costos indirectos
                while True:
                    mn.menu_costos_indirectos()
                    seleccion_costos_indirecto = val.Validacion_decicion_indirecto()

                    if seleccion_costos_indirecto == 'x':
                        break
                    if seleccion_costos_indirecto == 1:
                        while True:
                            mn.menu_costos_indirectos_1()
                            seleccion_costos_indirecto_1 = val.Validacion_decicion_indirecto1()

                            if seleccion_costos_indirecto_1 == 'x':
                                break
                    elif seleccion_costos_indirecto == 2:
                        while True:
                            mn.menu_costos_indirectos_2()
                            seleccion_costos_indirecto_2 = val.Validacion_decicion_indirecto2()

                            if seleccion_costos_indirecto_2 == 'x':
                                break
                    elif seleccion_costos_indirecto == 3:
                        while True:
                            mn.menu_costos_indirectos_3()
                            seleccion_costos_indirecto_3 = val.Validacion_decicion_indirecto3()

                            if seleccion_costos_indirecto_3 == 'x':
                                break
                
            elif seleccion_menu_inicio == 3: # opciones de pedido
                while True:
                    mn.menu_pedido()
                    seleccion_pedido = val.Validacion_decicion_pedidos()

                    if seleccion_pedido == 'x':
                        break
                    if seleccion_pedido == 1:
                        while True:
                            mn.menu_pedido_ingreso()
                            seleccion_pedido_ingreso = val.Validacion_decicion_pedidos_ingreso()

                            if seleccion_pedido_ingreso == 'x':
                                break
                            if seleccion_pedido_ingreso == 1: # orden de compra empresa
                                pass
                            else: # orden de compra persona
                                fecha, orden_compra, pais, region, ciudad, nombre_cliente, numero_cedula, numero_tel_cliente, correo_cliente = mn.menu_orden_compra_encabezado_cliente()
                                mn.menu_orden_compra_encabezado_cliente_final(fecha, orden_compra, pais, region, ciudad, nombre_cliente, numero_cedula, numero_tel_cliente, correo_cliente)
                    elif seleccion_pedido == 2:
                        while True:
                            mn.menu_pedido_modificacion()
                            seleccion_pedido_modificacion = val.Validacion_decicion_pedidos_modificacion()

                            if seleccion_pedido_modificacion == 'x':
                                break
                    elif seleccion_pedido == 3:
                        while True:
                            mn.menu_pedido_eliminar()
                            seleccion_pedido_eliminar = val.Validacion_decicion_pedidos_eliminar()

                            if seleccion_pedido_eliminar == 'x':
                                break
            elif seleccion_menu_inicio == 4:
                print()