from .vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, patente, marca, modelo, año, cilindrada):
        super().__init__(patente, marca, modelo, año)
        self.cilindrada = cilindrada

    def consumo(self, km):
        factor = 0.04 if self.cilindrada < 250 else 0.06
        return km * factor