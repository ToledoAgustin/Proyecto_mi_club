class Actividad:
    def __init__(self, nombre, dia, horario):
        self.nombre = nombre
        self.dia = dia
        self.horario = horario

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_dia(self):
        return self.dia

    def set_dia(self, dia):
        self.dia = dia

    def get_horario(self):
        return self.horario

    def set_horario(self, horario):
        self.horario = horario

    def mostrar_info(self):
        return f'Actividad: {self.nombre}, Día: {self.dia}, Horario: {self.horario}'