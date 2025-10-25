class Persona:
    institucion = "UAC"
    
    def __init__(self, _dni, _nombre):
        self.__dni = _dni
        self.nombre = _nombre
        
    def mostrar(self):
        print(f"la institucion es: {self.institucion} el DNI es: {self.__dni} y el nombre es: {self.nombre}")
        
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, _updateDni):
        if len(_updateDni) == 8:
            self.__dni = _updateDni
        else:
            print("Error de longitud")
            
if __name__ == "__main__":
    persona1 = Persona("11111111", "Fulanito Mengano")
    persona1.mostrar()