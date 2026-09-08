class Persona:
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad):
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.__tipo_identificacion = tipo_identificacion
        self.__identificacion = identificacion
        self.__nacionalidad = nacionalidad

    def get_tipo_identificacion(self):
        return self.__tipo_identificacion

    def set_tipo_identificacion(self, tipo_identificacion):
        self.__tipo_identificacion = tipo_identificacion
    
    def get_identificacion(self):
        return self.__identificacion

    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion

    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    def mostrar_datos(self):
        return f'Nombre completo: {self.nombre_completo}, Edad: {self.edad}, Tipo de ID: {self.__tipo_identificacion}, Nacionalidad: {self.__nacionalidad}, Estado legal: {self.es_mayor_de_edad()}, Validación: {self.validar_identificacion()}'

    # --- Métodos de las consignas ---

    def validar_edad(self):
        return self.edad in range(1, 111)

    def es_mayor_de_edad(self):
        validacion = self.validar_edad()
        if validacion != "Edad válida.":
            return validacion
        if self.edad >= 18:
            return "Es mayor de edad."
        else:
            return "Es menor de edad." 

    def validar_identificacion(self):
        identificacion = str(self.__identificacion)
        if identificacion == "":
            return "Identificación inválida (está vacía)."
        if not identificacion.isdigit():
            return "Identificación inválida (solo se permiten números)."
        if len(identificacion) not in (7, 8):
            return "Identificación inválida (debe tener 7 u 8 dígitos)."
        return "Identificación válida."