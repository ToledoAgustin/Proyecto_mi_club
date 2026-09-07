# Pruebas_de_socio

# socio1 = Socio("Matias Galarza Borja", 2, "DNI", 49903017, "Argentina", "23/02/2026", "Activo", "MatiCABJ", "MATIAS2011")


# socio1.mostrar_clubes()
# socio1.dar_baja_club(club_2)
# socio1.mostrar_clubes()

# socio1.generar_cuota("Agosto 2026", 15000)
# socio1.generar_cuota("Septiembre 2026", 15000)
# socio1.mostrar_cuotas()
# socio1.tiene_deudas()
# socio1.cantidad_cuotas_pendientes()
# socio1.pagar_cuota("Agosto 2026")
# socio1.tiene_deudas()
# socio1.cantidad_cuotas_pendientes()

# socio1.suspender()
# socio1.reactivar()

# socio1.verificar_acceso("PepeArgento2006", "holamundo123")
# socio1.verificar_acceso("PepeArgento2006", "clave_erronea")
# socio1.cambiar_contrasenia("holamundo123", "nuevaClave456")
# socio1.verificar_acceso("PepeArgento2006", "nuevaClave456")

# socio1.mostrar_datos()


# -----------------------------------------------------------------------------------------------------------

# Pruebas de Club

# club1 = Club("9 de julio Rafaela", "Club de fútbol", "Santa Fe", "Lucas Astrada", "09/07/1904")
# club2 = Club("Inter Miami", "Club de la MLS", "Miami", "David Beckham", "09/12/2018")

# club1.set_presidente("Juan Román Riquelme")

# club1.mostrar_info()
# club2.mostrar_info()

# -----------------------------------------------------------------------------------------------------------


# Pruebas de Cuota

# # Cuota vencida (fecha pasada, sin pagar)
# cuota1 = Cuota("Pendiente", "25/09/2026", "Septiembre 2026")
# cuota1.mostrar_cuota()
# print("¿Está vencida?", cuota1.esta_vencida())
# cuota1.dias_para_vencimiento()
# cuota1.actualizar_estado()
# cuota1.mostrar_cuota()
# print()
# # Cuota que aún no vence
# cuota2 = Cuota("Pendiente", "30/09/2026", "Septiembre 2026")
# cuota2.mostrar_cuota()
# print("¿Está vencida?", cuota2.esta_vencida())
# cuota2.dias_para_vencimiento()
# cuota2.actualizar_estado()
# cuota2.mostrar_cuota()
# print()
# # Registrar pago y renovar
# cuota2.registrar_pago()
# cuota2.mostrar_cuota()
# cuota2.renovar("Enero 2027", "31/01/2027")
# cuota2.mostrar_cuota()

# ------------------------------------------------------------------------------------------

# persona

# persona1 = Persona("Maxi Jackson", 10, "DNI", "uuf9e409", "Peru")
# persona1.mostrar_datos()
# persona2 = Persona("Santi Pérez", 15, "DNI", "", "Uruguay")
# persona2.mostrar_datos()