import funciones_auxiliares as aux
import validaciones as val
import menus as mn

ancho, altura = aux.tamaño()
fecha_hf = aux.fecha_hoy()# Obtener la fecha de hoy

#--------------------- variables encabezado venta -------------------
ubicacion = mn.ubicacion_data()
pais = mn.pais_data(ubicacion)
region = mn.region_data(ubicacion)
ciudad = mn.ciudad_data(ubicacion)
orden_compra = int(aux.numero_orden()) #numero de factura
siguiente = 1

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
                            #---------------------------------------------------------------------------
                    elif seleccion_costos_directo == 2:
                        while True:
                            mn.menu_costos_directos_2()
                            seleccion_costos_directo_2 = val.Validacion_decicion_directo2()

                            if seleccion_costos_directo_2 == 'x':
                                break
                            #----------------------------------------------------------------------------
                    elif seleccion_costos_directo == 3:
                        while True:
                            mn.menu_costos_directos_3()
                            seleccion_costos_directo_3 = val.Validacion_decicion_directo3()

                            if seleccion_costos_directo_3 == 'x':
                                break
                            #-------------------------------------------------------------------------
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
                    seleccion_pedido = val.Validacion_decicion_pedidos() #--------------------------ingreso 

                    if seleccion_pedido == 'x': # retroce
                        break
                    if seleccion_pedido == 1: # ingreso de pedido
                        while True:
                            mn.menu_pedido_ingreso()
                            seleccion_pedido_ingreso = val.Validacion_decicion_pedidos_ingreso()

                            if seleccion_pedido_ingreso == 'x':
                                break
                            if seleccion_pedido_ingreso == 1: # orden de compra empresa
                                while True:
                                    mn.menu_orden_compra_empresa_nombre()
                                    nombre_empresa = val.validacion_empresa_nombre()
                                    if nombre_empresa == False:
                                        break
                                    else: 

                                        while True:
                                            mn.menu_orden_compra_empresa_ruc(nombre_empresa)
                                            ruc = val.validacion_ruc(nombre_empresa)
                                            if ruc == 'x':
                                                break
                                            else:

                                                while True:
                                                    mn.menu_orden_compra_empresa_encargado(nombre_empresa,ruc)
                                                    nombre_encargado = val.validacion_empresa_encargado(nombre_empresa,ruc)
                                                    if nombre_encargado == False:
                                                        break
                                                    else:
                                                    
                                                        while True:
                                                            mn.menu_orden_compra_empresa_cedula(nombre_empresa,ruc,nombre_encargado)
                                                            numero_cedula = val.validacion_empresa_cedula_f(nombre_empresa,ruc,nombre_encargado)
                                                            if numero_cedula == False:
                                                                break
                                                            else:
                                                            
                                                                while True:
                                                                    mn.menu_orden_compra_empresa_numero_telefonico(nombre_empresa,ruc,nombre_encargado, numero_cedula)
                                                                    numero_tel_cliente = val.validacion_empresa_telefono(nombre_empresa,ruc,nombre_encargado,numero_cedula)
                                                                    if numero_tel_cliente == False:
                                                                        break
                                                                    else:
                                                                    
                                                                        while True:
                                                                            mn.menu_orden_compra_empresa_correo(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente)
                                                                            correo_cliente = val.validacion_empresa_correo(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente)
                                                                            if correo_cliente == False:
                                                                                break
                                                                            else:
                                                                            
                                                                                while True:
                                                                                    mn.menu_orden_compra_empresa_ruta(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                    mn.menu_rutas()
                                                                                    ruta = val.validacion_rutas()
                                                                                    if ruta == 'x':
                                                                                        break
                                                                                    else:
                                                                                    
                                                                                        precio_ruta, ruta = aux.calculo_valor_ruta(ruta)
                                                                                        while True:
                                                                                            mn.menu_orden_compra_empresa_parte1(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                            mn.menu_orden_compra_camaron(ruta)
                                                                                            mn.menu_tipo_camaron()
                                                                                            camaron_t = val.validacion_tipos_camaron()
                                                                                            if camaron_t == 'x':
                                                                                                break
                                                                                            else:
                                                                                            
                                                                                                precio_camaron, camaron_t = aux.calculo_valor_camaron(camaron_t)
                                                                                                while True:
                                                                                                    mn.menu_orden_compra_empresa_parte1(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                                    mn.menu_orden_compra_cantidad_compra(ruta,camaron_t)
                                                                                                    mn.menu_cantidad_compra()
                                                                                                    cant_compra = val.validacion_cantidad_carga()
                                                                                                    if cant_compra == 'x':
                                                                                                        break
                                                                                                    else:
                                                                                                    
                                                                                                        cant_camion, sub_precio = aux.calcular_valor_venta(cant_compra,precio_camaron,precio_ruta)
                                                                                                        while True:
                                                                                                            pedidos = []
                                                                                                            momentaneo = []
                                                                                                            momentaneo.append(ruta)
                                                                                                            momentaneo.append(precio_ruta)#2
                                                                                                            momentaneo.append(camaron_t)
                                                                                                            momentaneo.append(precio_camaron)
                                                                                                            momentaneo.append(cant_compra)
                                                                                                            momentaneo.append(cant_camion)#1
                                                                                                            momentaneo.append(sub_precio)#3 - 6
                                                                                                            pedidos.append(momentaneo)

                                                                                                            mn.menu_orden_compra_empresa_parte1(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                                            mn.menu_orden_compra_parte2(ruta,camaron_t,cant_compra)
                                                                                                            mn.menu_orden_compra_parte3()
                                                                                                            mn.menu_orden_compra_parte4(cant_camion, precio_ruta, sub_precio)
                                                                                                            mn.asegurar_orde_compra()
                                                                                                            seleccion_otra_compra = val.validacion_otra_compra()
                                                                                                            if seleccion_otra_compra == 's': #validar
                                                                                                            
                                                                                                                #------------------------- bucle de guardado de varios pedidos
                                                                                                                while True:
                                                                                                                    pedido = []
                                                                                                                    mn.menu_orden_compra_ruta(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                                                    mn.menu_rutas()
                                                                                                                    ruta = val.validacion_rutas()
                                                                                                                    if ruta == 'x':
                                                                                                                        pedidos.pop()
                                                                                                                        break
                                                                                                                    else:
                                                                                                                    
                                                                                                                        precio_ruta, ruta = aux.calculo_valor_ruta(ruta)
                                                                                                                        while True:
                                                                                                                            mn.menu_orden_compra_empresa_parte1(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                                                            mn.menu_orden_compra_camaron(ruta)
                                                                                                                            mn.menu_tipo_camaron()
                                                                                                                            camaron_t = val.validacion_tipos_camaron()
                                                                                                                            if camaron_t == 'x':
                                                                                                                                break
                                                                                                                            else:
                                                                                                                            
                                                                                                                                precio_camaron, camaron_t = aux.calculo_valor_camaron(camaron_t)
                                                                                                                                while True:
                                                                                                                                    mn.menu_orden_compra_empresa_parte1(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                                                                    mn.menu_orden_compra_cantidad_compra(ruta,camaron_t)
                                                                                                                                    mn.menu_cantidad_compra()
                                                                                                                                    cant_compra = val.validacion_cantidad_carga()
                                                                                                                                    if cant_compra == 'x':
                                                                                                                                        break
                                                                                                                                    else:
                                                                                                                                        cant_camion, sub_precio = aux.calcular_valor_venta(cant_compra,precio_camaron,precio_ruta)
                                                                                                                                        pedido.append(ruta) # 11 -0
                                                                                                                                        pedido.append(precio_ruta)#2
                                                                                                                                        pedido.append(camaron_t) #22 -2
                                                                                                                                        pedido.append(precio_camaron)
                                                                                                                                        pedido.append(cant_compra)#33 - 4
                                                                                                                                        pedido.append(cant_camion)#1
                                                                                                                                        pedido.append(sub_precio)#3 - 6
                                                                                                                                        pedidos.append(pedido)

                                                                                                                                        mn.asegurar_orde_compra()
                                                                                                                                        seleccion_otra_compra = val.validacion_otra_compra()
                                                                                                                                        if seleccion_otra_compra == 's':
                                                                                                                                            break
                                                                                                                                        else:
                                                                                                                                            sub_total = aux.calculo_sub_total(pedidos)
                                                                                                                                            iva = aux.calculo_iva(sub_total)
                                                                                                                                            total_final = aux.calculo_precio_final(sub_total,iva)
                                                                                                                                            mn.menu_orden_compra_empresa_parte1(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                                                                            mn.mostar_menu_orden_compra_masiva(pedidos,sub_total,iva,total_final)
                                                                                                                                            mn.asegurar_orde_compra_final()
                                                                                                                                            opcion = val.Validacion_orden_empresa_final_masiva(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente,sub_total,iva,total_final,pedidos)
                                                                                                                                            if opcion == 'x':
                                                                                                                                                break
                                                                                                                                            elif opcion == 's':
                                                                                                                                                print('estamos guardando la info')

                                                                                                                                                #informacion a guardar
                                                                                                                                                nombre_arch = fecha_hf + ','  + ruc + ',' + numero_cedula + ',' + nombre_empresa + ',' + nombre_encargado + ',' + numero_tel_cliente + ',' + str(orden_compra)

                                                                                                                                                # guardando informacion
                                                                                                                                                aux.guardar_info_orden_empresa_masiva(nombre_arch,fecha_hf,str(orden_compra),numero_cedula,ruc,nombre_empresa,nombre_cliente,numero_tel_cliente,correo_cliente,sub_total,iva,total_final,pedidos)

                                                                                                                                                #actualizar orden de factura
                                                                                                                                                orden_compra += 1
                                                                                                                                                aux.numero_orden_actualizado(str(orden_compra))
                                                                                                                                                #aux.esperar(2)
                                                                                                                                                siguiente = val.validacion_siguiente()
                                                                                                                                                if siguiente == 1:
                                                                                                                                                    siguiente = 0
                                                                                                                                                else:
                                                                                                                                                    siguiente = None
                                                                                                                                            elif opcion == 'n':
                                                                                                                                                nombre_empresa = nombre_encargado = ruc = numero_cedula = numero_tel_cliente = correo_cliente = ruta = precio_ruta = camaron_t = precio_camaron = cant_compra = sub_total = iva = total_final = None 

                                                                                                                                                siguiente = val.validacion_siguiente()
                                                                                                                                                if siguiente == 1:
                                                                                                                                                    siguiente = 0
                                                                                                                                                else:
                                                                                                                                                    siguiente = None 

                                                                                                                                        if siguiente == None or siguiente == 0:
                                                                                                                                            break 
                                                                                                                                if seleccion_otra_compra == 's':
                                                                                                                                    break
                                                                                                                                if siguiente == None or siguiente == 0:
                                                                                                                                    break
                                                                                                                        #if seleccion_otra_compra == 's':
                                                                                                                        #    break
                                                                                                                        if siguiente == None or siguiente == 0:
                                                                                                                            break
                                                                                                                if siguiente == None or siguiente == 0:
                                                                                                                    break
                                                                                                            elif seleccion_otra_compra == 'n':
                                                                                                                sub_total = sub_precio
                                                                                                                iva = aux.calculo_iva(sub_total)
                                                                                                                total_final = aux.calculo_precio_final(sub_total,iva)
                                                                                                                mn.menu_orden_compra_empresa_parte1(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                                                mn.menu_orden_compra_parte2(ruta,camaron_t,cant_compra)
                                                                                                                mn.menu_orden_compra_parte3()
                                                                                                                mn.menu_orden_compra_parte4(cant_camion, precio_ruta, sub_precio)
                                                                                                                mn.menu_orden_compra_parte5(sub_total,iva,total_final)
                                                                                                                mn.asegurar_orde_compra_final()
                                                                                                                opcion = val.Validacion_orden_empresa_final(nombre_empresa,ruc,nombre_encargado,numero_cedula,numero_tel_cliente,correo_cliente,ruta,camaron_t,cant_compra,cant_camion,precio_ruta,sub_total,iva,total_final)
                                                                                                                if opcion == 'x':
                                                                                                                    break
                                                                                                                elif opcion == 's':
                                                                                                                    print('estamos guardando la info')

                                                                                                                    #informacion a guardar
                                                                                                                    nombre_arch = fecha_hf + ',' + ruc + ',' + numero_cedula + ',' + nombre_empresa + ',' + nombre_encargado + ',' + numero_tel_cliente + ',' + str(orden_compra)

                                                                                                                    # guardando informacion
                                                                                                                    aux.guardar_info_orden_empresa(nombre_arch,fecha_hf,str(orden_compra),numero_cedula,ruc,nombre_empresa,nombre_cliente,numero_tel_cliente,correo_cliente,ruta,precio_ruta,camaron_t,cant_compra,cant_camion,sub_precio,sub_total,iva,total_final,precio_camaron)
                                                                                                                    orden_compra += 1
                                                                                                                    aux.numero_orden_actualizado(str(orden_compra))
                                                                                                                    #aux.esperar(2)
                                                                                                                    siguiente = val.validacion_siguiente()
                                                                                                                    if siguiente == 1:
                                                                                                                        siguiente = 0
                                                                                                                    else:
                                                                                                                        siguiente = None
                                                                                                                elif opcion == 'n':
                                                                                                                    nombre_empresa = nombre_encargado = ruc = numero_cedula = numero_tel_cliente = correo_cliente = ruta = precio_ruta = camaron_t = precio_camaron = cant_compra = sub_precio = None 

                                                                                                                    siguiente = val.validacion_siguiente()
                                                                                                                    if siguiente == 1:
                                                                                                                        siguiente = 0
                                                                                                                    else:
                                                                                                                        siguiente = None

                                                                                                            if siguiente == None or siguiente == 0:
                                                                                                                break
                                                                                                    if siguiente == None or siguiente == 0:
                                                                                                        break
                                                                                            if siguiente == None or siguiente == 0:
                                                                                                break
                                                                                    if siguiente == None or siguiente == 0:
                                                                                        break
                                                                            if siguiente == None or siguiente == 0:
                                                                                break
                                                                    if siguiente == None or siguiente == 0:
                                                                        break
                                                            if siguiente == None or siguiente == 0:
                                                                    break
                                                    if siguiente == None or siguiente == 0:
                                                        break
                            if siguiente == None:
                                break

                            if seleccion_pedido_ingreso == 2: # orden de compra persona
                                while True:
                                    mn.menu_orden_compra_nombre()
                                    nombre_cliente = val.validacion_nombre()
                                    if nombre_cliente == False:
                                        break
                                    else:

                                        while True:
                                            mn.menu_orden_compra_cedula(nombre_cliente)
                                            numero_cedula = val.validacion_cedula_f(nombre_cliente)
                                            if numero_cedula == False:
                                                break
                                            else:

                                                while True:
                                                    mn.menu_orden_compra_numero_telefonico(nombre_cliente,numero_cedula)
                                                    numero_tel_cliente = val.validacion_telefono(nombre_cliente,numero_cedula)
                                                    if numero_tel_cliente == False:
                                                        break
                                                    else:

                                                        while True:
                                                            mn.menu_orden_compra_correo(nombre_cliente,numero_cedula,numero_tel_cliente)
                                                            correo_cliente = val.validacion_correo(nombre_cliente,numero_cedula,numero_tel_cliente)
                                                            if correo_cliente == False:
                                                                break
                                                            else:

                                                                while True:
                                                                    mn.menu_orden_compra_ruta(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                    mn.menu_rutas()
                                                                    ruta = val.validacion_rutas()
                                                                    if ruta == 'x':
                                                                        break
                                                                    else:

                                                                        precio_ruta, ruta = aux.calculo_valor_ruta(ruta)
                                                                        while True:
                                                                            mn.menu_orden_compra_parte1(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                            mn.menu_orden_compra_camaron(ruta)
                                                                            mn.menu_tipo_camaron()
                                                                            camaron_t = val.validacion_tipos_camaron()
                                                                            if camaron_t == 'x':
                                                                                break
                                                                            else:

                                                                                precio_camaron, camaron_t = aux.calculo_valor_camaron(camaron_t)
                                                                                while True:
                                                                                    mn.menu_orden_compra_parte1(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                    mn.menu_orden_compra_cantidad_compra(ruta,camaron_t)
                                                                                    mn.menu_cantidad_compra()
                                                                                    cant_compra = val.validacion_cantidad_carga()
                                                                                    if cant_compra == 'x':
                                                                                        break
                                                                                    else:

                                                                                        cant_camion, sub_precio = aux.calcular_valor_venta(cant_compra,precio_camaron,precio_ruta)
                                                                                        while True:
                                                                                            pedidos = []
                                                                                            momentaneo = []
                                                                                            momentaneo.append(ruta)
                                                                                            momentaneo.append(precio_ruta)#2
                                                                                            momentaneo.append(camaron_t)
                                                                                            momentaneo.append(precio_camaron)
                                                                                            momentaneo.append(cant_compra)
                                                                                            momentaneo.append(cant_camion)#1
                                                                                            momentaneo.append(sub_precio)#3 - 6
                                                                                            pedidos.append(momentaneo)

                                                                                            mn.menu_orden_compra_parte1(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                            mn.menu_orden_compra_parte2(ruta,camaron_t,cant_compra)
                                                                                            mn.menu_orden_compra_parte3()
                                                                                            mn.menu_orden_compra_parte4(cant_camion, precio_ruta, sub_precio)
                                                                                            mn.asegurar_orde_compra()
                                                                                            seleccion_otra_compra = val.validacion_otra_compra()
                                                                                            if seleccion_otra_compra == 's': #validar
                                                                             
                                                                                                #------------------------- bucle de guardado de varios pedidos
                                                                                                while True:
                                                                                                    pedido = []
                                                                                                    mn.menu_orden_compra_ruta(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                                    mn.menu_rutas()
                                                                                                    ruta = val.validacion_rutas()
                                                                                                    if ruta == 'x':
                                                                                                        pedidos.pop()
                                                                                                        break
                                                                                                    else:
                                                                                                    
                                                                                                        precio_ruta, ruta = aux.calculo_valor_ruta(ruta)
                                                                                                        while True:
                                                                                                            mn.menu_orden_compra_parte1(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                                            mn.menu_orden_compra_camaron(ruta)
                                                                                                            mn.menu_tipo_camaron()
                                                                                                            camaron_t = val.validacion_tipos_camaron()
                                                                                                            if camaron_t == 'x':
                                                                                                                break
                                                                                                            else:
                                                                                                            
                                                                                                                precio_camaron, camaron_t = aux.calculo_valor_camaron(camaron_t)
                                                                                                                while True:
                                                                                                                    mn.menu_orden_compra_parte1(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                                                    mn.menu_orden_compra_cantidad_compra(ruta,camaron_t)
                                                                                                                    mn.menu_cantidad_compra()
                                                                                                                    cant_compra = val.validacion_cantidad_carga()
                                                                                                                    if cant_compra == 'x':
                                                                                                                        break
                                                                                                                    else:
                                                                                                                        cant_camion, sub_precio = aux.calcular_valor_venta(cant_compra,precio_camaron,precio_ruta)
                                                                                                                        pedido.append(ruta) # 11 -0
                                                                                                                        pedido.append(precio_ruta)#2
                                                                                                                        pedido.append(camaron_t) #22 -2
                                                                                                                        pedido.append(precio_camaron)
                                                                                                                        pedido.append(cant_compra)#33 - 4
                                                                                                                        pedido.append(cant_camion)#1
                                                                                                                        pedido.append(sub_precio)#3 - 6
                                                                                                                        pedidos.append(pedido)
                                                                                                                        
                                                                                                                        mn.asegurar_orde_compra()
                                                                                                                        seleccion_otra_compra = val.validacion_otra_compra()
                                                                                                                        if seleccion_otra_compra == 's':
                                                                                                                            break
                                                                                                                        else:
                                                                                                                            sub_total = aux.calculo_sub_total(pedidos)
                                                                                                                            iva = aux.calculo_iva(sub_total)
                                                                                                                            total_final = aux.calculo_precio_final(sub_total,iva)
                                                                                                                            mn.menu_orden_compra_parte1(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                                                            mn.mostar_menu_orden_compra_masiva(pedidos,sub_total,iva,total_final)
                                                                                                                            mn.asegurar_orde_compra_final()
                                                                                                                            opcion = val.Validacion_orden_final_masiva(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente,sub_total,iva,total_final,pedidos)
                                                                                                                            if opcion == 'x':
                                                                                                                                break
                                                                                                                            elif opcion == 's':
                                                                                                                                print('estamos guardando la info')
                                                                                                                                ruc = 'xxxxxxxxxxxxx'

                                                                                                                                #informacion a guardar
                                                                                                                                nombre_arch = fecha_hf + ',' + ruc + ',' + numero_cedula + ',' + nombre_cliente + ',' + numero_tel_cliente + ',' + str(orden_compra)

                                                                                                                                # guardando informacion
                                                                                                                                aux.guardar_info_orden_masiva(nombre_arch,fecha_hf,str(orden_compra),numero_cedula,nombre_cliente,numero_tel_cliente,correo_cliente,sub_total,iva,total_final,pedidos)
                                                                                                                                
                                                                                                                                #actualizar orden de factura
                                                                                                                                orden_compra += 1
                                                                                                                                aux.numero_orden_actualizado(str(orden_compra))
                                                                                                                                #aux.esperar(2)
                                                                                                                                siguiente = val.validacion_siguiente()
                                                                                                                                if siguiente == 1:
                                                                                                                                    siguiente = 0
                                                                                                                                else:
                                                                                                                                    siguiente = None
                                                                                                                            elif opcion == 'n':
                                                                                                                                nombre_cliente = numero_cedula = numero_tel_cliente = correo_cliente = ruta = precio_ruta = camaron_t = precio_camaron = cant_compra = sub_total = iva = total_final = None 
                                                                                                                                
                                                                                                                                siguiente = val.validacion_siguiente()
                                                                                                                                if siguiente == 1:
                                                                                                                                    siguiente = 0
                                                                                                                                else:
                                                                                                                                    siguiente = None 

                                                                                                                        if siguiente == None or siguiente == 0:
                                                                                                                            break 
                                                                                                                if seleccion_otra_compra == 's':
                                                                                                                    break
                                                                                                                if siguiente == None or siguiente == 0:
                                                                                                                    break
                                                                                                        #if seleccion_otra_compra == 's':
                                                                                                        #    break
                                                                                                        if siguiente == None or siguiente == 0:
                                                                                                            break
                                                                                                if siguiente == None or siguiente == 0:
                                                                                                    break
                                                                                            elif seleccion_otra_compra == 'n':
                                                                                                sub_total = sub_precio
                                                                                                iva = aux.calculo_iva(sub_total)
                                                                                                total_final = aux.calculo_precio_final(sub_total,iva)
                                                                                                mn.menu_orden_compra_parte1(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente)
                                                                                                mn.menu_orden_compra_parte2(ruta,camaron_t,cant_compra)
                                                                                                mn.menu_orden_compra_parte3()
                                                                                                mn.menu_orden_compra_parte4(cant_camion, precio_ruta, sub_precio)
                                                                                                mn.menu_orden_compra_parte5(sub_total,iva,total_final)
                                                                                                mn.asegurar_orde_compra_final()
                                                                                                opcion = val.Validacion_orden_final(nombre_cliente,numero_cedula,numero_tel_cliente,correo_cliente,ruta,camaron_t,cant_compra,cant_camion,precio_ruta,sub_total,iva,total_final)
                                                                                                if opcion == 'x':
                                                                                                    break
                                                                                                elif opcion == 's':
                                                                                                    print('estamos guardando la info')

                                                                                                    ruc = 'xxxxxxxxxxxxx'

                                                                                                    #informacion a guardar
                                                                                                    nombre_arch = fecha_hf + ',' + ruc + ',' + numero_cedula + ',' + nombre_cliente + ',' + numero_tel_cliente  + ',' + str(orden_compra)

                                                                                                    # guardando informacion
                                                                                                    aux.guardar_info_orden(nombre_arch,fecha_hf,str(orden_compra),numero_cedula,nombre_cliente,numero_tel_cliente,correo_cliente,ruta,precio_ruta,camaron_t,cant_compra,cant_camion,sub_precio,sub_total,iva,total_final,str(precio_camaron))
                                                                                                    orden_compra += 1
                                                                                                    aux.numero_orden_actualizado(str(orden_compra))
                                                                                                    #aux.esperar(2)
                                                                                                    siguiente = val.validacion_siguiente()
                                                                                                    if siguiente == 1:
                                                                                                        siguiente = 0
                                                                                                    else:
                                                                                                        siguiente = None
                                                                                                elif opcion == 'n':
                                                                                                    nombre_cliente = numero_cedula = numero_tel_cliente = correo_cliente = ruta = precio_ruta = camaron_t = precio_camaron = cant_compra = sub_precio = None 
                                                                                                    
                                                                                                    siguiente = val.validacion_siguiente()
                                                                                                    if siguiente == 1:
                                                                                                        siguiente = 0
                                                                                                    else:
                                                                                                        siguiente = None

                                                                                            if siguiente == None or siguiente == 0:
                                                                                                break
                                                                                    if siguiente == None or siguiente == 0:
                                                                                        break
                                                                            if siguiente == None or siguiente == 0:
                                                                                break
                                                                    if siguiente == None or siguiente == 0:
                                                                        break
                                                            if siguiente == None or siguiente == 0:
                                                                break
                                                    if siguiente == None or siguiente == 0:
                                                        break
                                            if siguiente == None or siguiente == 0:
                                                    break
                                    if siguiente == None or siguiente == 0:
                                        break
                            if siguiente == None:
                                break
                    if siguiente == None:
                        break
                                                                                        
                    if seleccion_pedido == 2: #consulta
                        mn.menu_consulta()
                        mn.menu_busqueda()
                        seleccion_pedido_consulta = val.validacion_menu_consulta()

                        if seleccion_pedido_consulta == 'x':
                            break
                        elif seleccion_pedido_consulta == 1:
                            while True:
                                busqueda = val.validacion_busqueda_consulta_fecha()
                                if busqueda == 'x':
                                    break

                        elif seleccion_pedido_consulta == 2:
                            while True:
                                busqueda = val.validacion_busqueda_consulta_numero_factura()
                                if busqueda == 'x':
                                    break

                        elif seleccion_pedido_consulta == 3:
                            while True:
                                busqueda = val.validacion_busqueda_consulta_cedula()
                                if busqueda == 'x':
                                    break

                        elif seleccion_pedido_consulta == 4:
                            while True:
                                busqueda = val.validacion_busqueda_consulta_ruc()
                                if busqueda == 'x':
                                    break

                        elif seleccion_pedido_consulta == 5:
                            while True:
                                busqueda = val.validacion_busqueda_consulta_nombre()
                                if busqueda == 'x':
                                    break

                        elif seleccion_pedido_consulta == 6:
                            while True:
                                busqueda = val.validacion_busqueda_consulta_nombre_empresa()
                                if busqueda == 'x':
                                    break

                        elif seleccion_pedido_consulta == 7:
                            while True:
                                busqueda = val.validacion_busqueda_consulta_telefono()
                                if busqueda == 'x':
                                    break
                        
                    elif seleccion_pedido == 3: #modificacion
                        while True:
                            mn.menu_modificacion() 
                            mn.menu_busqueda()
                            seleccion_pedido_modificacion = val.validacion_menu_modificacion()
                            
                            if seleccion_pedido_modificacion == 'x':
                                break
                            elif seleccion_pedido_modificacion == 1:
                                while True:
                                    busqueda = val.validacion_busqueda_modificacion_fecha()
                                    if busqueda == 'x':
                                        break

                            elif seleccion_pedido_modificacion == 2:
                                while True:
                                    busqueda = val.validacion_busqueda_modificacion_numero_factura()
                                    if busqueda == 'x':
                                        break

                            elif seleccion_pedido_modificacion == 3:
                                while True:
                                    busqueda = val.validacion_busqueda_modificacion_cedula()
                                    if busqueda == 'x':
                                        break

                            elif seleccion_pedido_modificacion == 4:
                                while True:
                                    busqueda = val.validacion_busqueda_modificacion_ruc()
                                    if busqueda == 'x':
                                        break

                            elif seleccion_pedido_modificacion == 5:
                                while True:
                                    busqueda = val.validacion_busqueda_modificacion_nombre()
                                    if busqueda == 'x':
                                        break

                            elif seleccion_pedido_modificacion == 6:
                                while True:
                                    busqueda = val.validacion_busqueda_modificacion_nombre_empresa()
                                    if busqueda == 'x':
                                        break

                            elif seleccion_pedido_modificacion == 7:
                                while True:
                                    busqueda = val.validacion_busqueda_modificacion_telefono()
                                    if busqueda == 'x':
                                        break

                    elif seleccion_pedido == 4:#eliminar
                        while True:
                            mn.menu_pedido_eliminar()
                            seleccion_pedido_eliminar = val.Validacion_decicion_pedidos_eliminar()

                            if seleccion_pedido_eliminar == 'x':
                                break
                            elif seleccion_pedido_eliminar == 1:
                                while True:
                                    busqueda = val.validacion_busqueda_eliminacion_fecha()
                                    if busqueda == 'x':
                                        break

                            elif seleccion_pedido_eliminar == 2:
                                while True:
                                    busqueda = val.validacion_busqueda_eliminacion_numero_factura()
                                    if busqueda == 'x':
                                        break

                            elif seleccion_pedido_eliminar == 3:
                                while True:
                                    busqueda = val.validacion_busqueda_eliminacion_cedula()
                                    if busqueda == 'x':
                                        break

                            elif seleccion_pedido_eliminar == 4:
                                while True:
                                    busqueda = val.validacion_busqueda_eliminacion_ruc()
                                    if busqueda == 'x':
                                        break

                            elif seleccion_pedido_eliminar == 5:
                                while True:
                                    busqueda = val.validacion_busqueda_eliminacion_nombre()
                                    if busqueda == 'x':
                                        break

                            elif seleccion_pedido_eliminar == 6:
                                while True:
                                    busqueda = val.validacion_busqueda_eliminacion_nombre_empresa()
                                    if busqueda == 'x':
                                        break

                            elif seleccion_pedido_eliminar == 7:
                                while True:
                                    busqueda = val.validacion_busqueda_eliminacion_telefono()
                                    if busqueda == 'x':
                                        break


            #if siguiente == None:
            #    break
            if seleccion_menu_inicio == 4:
                print()