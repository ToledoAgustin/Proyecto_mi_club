from datetime import datetime

class Cuota:
    def __init__(self, estado, fecha_de_vencimiento, periodo):
        self.__estado = estado
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.periodo = periodo

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    # 1) Registrar una cuota como pagada
    def registrar_pago(self):
        self.__estado = "Pagada"
        return f'La cuota del período {self.periodo} fue registrada como pagada.'

    # 2) Determinar si una cuota está vencida
    def esta_vencida(self):
        fecha_vencimiento = datetime.strptime(self.fecha_de_vencimiento, "%d/%m/%Y").date()
        fecha_actual = datetime.now().date()

        if self.__estado != "Pagada" and fecha_actual > fecha_vencimiento:
            return True
        return False

    # 3) Actualizar automáticamente el estado de la cuota
    def actualizar_estado(self):
        if self.__estado == "Pagada":
            return f'La cuota del período {self.periodo} ya está pagada, no se actualiza.'

        if self.esta_vencida():
            self.__estado = "Vencida"
            return f'La cuota del período {self.periodo} fue marcada como vencida.'

        self.__estado = "Pendiente"
        return f'La cuota del período {self.periodo} sigue pendiente.'

    # 4) Informar cuántos días faltan para el vencimiento
    def dias_para_vencimiento(self):
        fecha_vencimiento = datetime.strptime(self.fecha_de_vencimiento, "%d/%m/%Y").date()
        fecha_actual = datetime.now().date()
        diferencia = fecha_vencimiento - fecha_actual
        dias = diferencia.days

        if dias > 0:
            return f"Faltan {dias} día(s) para el vencimiento de la cuota del período {self.periodo}."
        if dias == 0:
            return f"La cuota del período {self.periodo} vence hoy."
        return f"La cuota del período {self.periodo} venció hace {abs(dias)} día(s)."

    # 5) Renovar la cuota para un nuevo período
    def renovar(self, nuevo_periodo, nueva_fecha_vencimiento):
        self.periodo = nuevo_periodo
        self.fecha_de_vencimiento = nueva_fecha_vencimiento
        self.__estado = "Pendiente"
        return f'La cuota fue renovada para el período {nuevo_periodo}, vence el {nueva_fecha_vencimiento}.'

    def mostrar_cuota(self):
        return f"Período: {self.periodo}, Fecha de vencimiento: {self.fecha_de_vencimiento}, Estado: {self.__estado}"