from .vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, patente, marca, modelo, año, puertas):
        super().__init__(patente, marca, modelo, año)
        self.puertas = puertas

    def consumo(self, km):
        return km * 0.08  # Ejemplo