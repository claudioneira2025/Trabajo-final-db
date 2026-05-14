class Flota:
    def __init__(self):
        self.vehiculos = {}

    def agregar(self, vehiculo):
        if vehiculo.patente in self.vehiculos:
            return False
        self.vehiculos[vehiculo.patente] = vehiculo
        return True

    def eliminar(self, patente):
        return self.vehiculos.pop(patente, None)

    def buscar(self, patente):
        return self.vehiculos.get(patente)

    def listar(self):
        return list(self.vehiculos.values())

    def consumo_total(self, km):
        return sum(v.consumo(km) for v in self.vehiculos.values())