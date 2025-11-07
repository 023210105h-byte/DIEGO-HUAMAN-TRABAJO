class Vehiculo:
    def __init__(self, marca, modelo, matricula):
        self.__marca = marca
        self.__modelo = modelo
        self.__matricula = matricula

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getMatricula(self):
        return self.__matricula

    def setMarca(self, marca):
        self.__marca = marca

    def setModelo(self, modelo):
        self.__modelo = modelo

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def costo_por_km(self):
        raise NotImplementedError("Este método debe implementarse en las subclases.")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, matricula, consumo_litros_km, precio_gasolina):
        super().__init__(marca, modelo, matricula)
        self.__consumo_litros_km = consumo_litros_km
        self.__precio_gasolina = precio_gasolina

    def getConsumo(self):
        return self.__consumo_litros_km

    def getPrecioGasolina(self):
        return self.__precio_gasolina

    def costo_por_km(self):
        return self.__consumo_litros_km * self.__precio_gasolina


class Camion(Vehiculo):
    def __init__(self, marca, modelo, matricula, consumo_litros_km, precio_diesel):
        super().__init__(marca, modelo, matricula)
        self.__consumo_litros_km = consumo_litros_km
        self.__precio_diesel = precio_diesel

    def costo_por_km(self):
        return (self.__consumo_litros_km * self.__precio_diesel) * 1.10


class CocheElectrico(Coche):
    def __init__(self, marca, modelo, matricula, consumo_kwh_km, precio_kwh):
        super().__init__(marca, modelo, matricula, consumo_kwh_km, precio_kwh)

    def costo_por_km(self):
        return self.getConsumo() * self.getPrecioGasolina()


def calcular_costes(vehiculos, kms):
    resultados = []
    for v in vehiculos:
        coste = v.costo_por_km() * kms
        resultados.append((v.getMarca(), v.getModelo(), round(coste, 2)))
    return resultados


if __name__ == "__main__":
    vehiculos = []

    while True:
        print("\n----- MENÚ PRINCIPAL -----")
        print("1. Agregar un Coche")
        print("2. Agregar un Camión")
        print("3. Agregar un Coche Eléctrico")
        print("4. Mostrar todos los vehículos")
        print("5. Calcular costes por km")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            print("\n--- Agregar Coche ---")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            matricula = input("Matrícula: ")
            consumo = float(input("Consumo (litros/km): "))
            precio = float(input("Precio gasolina (€/litro): "))
            coche = Coche(marca, modelo, matricula, consumo, precio)
            vehiculos.append(coche)
            print("Coche agregado correctamente.")

        elif opcion == "2":
            print("\n--- Agregar Camión ---")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            matricula = input("Matrícula: ")
            consumo = float(input("Consumo (litros/km): "))
            precio = float(input("Precio diésel (€/litro): "))
            camion = Camion(marca, modelo, matricula, consumo, precio)
            vehiculos.append(camion)
            print("Camión agregado correctamente.")

        elif opcion == "3":
            print("\n--- Agregar Coche Eléctrico ---")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            matricula = input("Matrícula: ")
            consumo = float(input("Consumo (kWh/km): "))
            precio = float(input("Precio energía eléctrica (€/kWh): "))
            electrico = CocheElectrico(marca, modelo, matricula, consumo, precio)
            vehiculos.append(electrico)
            print("Coche eléctrico agregado correctamente.")

        elif opcion == "4":
            print("\n--- Vehículos registrados ---")
            if len(vehiculos) == 0:
                print("No hay vehículos registrados.")
            else:
                for i, v in enumerate(vehiculos):
                    print(f"{i+1}. {v.getMarca()} {v.getModelo()} ({v.getMatricula()})")

        elif opcion == "5":
            if len(vehiculos) == 0:
                print("Primero debe registrar al menos un vehículo.")
            else:
                kms = float(input("Ingrese la cantidad de kilómetros a recorrer: "))
                resultados = calcular_costes(vehiculos, kms)
                print("\n--- Costes Totales ---")
                for marca, modelo, coste in resultados:
                    print(f"{marca} {modelo}: {coste} € para {kms} km")

        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

