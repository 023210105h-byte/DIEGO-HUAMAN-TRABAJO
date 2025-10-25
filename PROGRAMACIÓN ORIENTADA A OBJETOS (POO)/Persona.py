class Persona:
    def __init__(self, DNI="00000000", Nombres="Sin Nombre", Apellidos="Sin Apellido"):
        self.__DNI = DNI
        self.__Nombres = Nombres
        self.__Apellidos = Apellidos

    def getDNI(self):
        return self.__DNI

    def getNombres(self):
        return self.__Nombres

    def getApellidos(self):
        return self.__Apellidos

    def setDNI(self, DNI):
        self.__DNI = DNI

    def setNombres(self, Nombres):
        self.__Nombres = Nombres

    def setApellidos(self, Apellidos):
        self.__Apellidos = Apellidos
        
personal = Persona("11111111", "JUANITO", "ARCOIRIS")
print(personal.getDNI())
print(personal.getNombres())
print(personal.getApellidos())

personal.setDNI("77777777")
print(personal.getDNI())