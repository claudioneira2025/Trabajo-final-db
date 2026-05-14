from .vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, patente, marca, modelo, año, capacidad_carga):
        super().__init__(patente, marca, modelo, año)
        self.capacidad_carga = capacidad_carga

    def consumo(self, km):
        base = 0.2
        adicional = self.capacidad_carga / 5000 * 0.05
        return km * (base + adicional)