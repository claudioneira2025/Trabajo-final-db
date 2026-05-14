class Vehiculo:
    def __init__(self, patente, marca, modelo, año):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        return f"[{self.patente}] {self.marca} {self.modelo} ({self.año}) - Tipo: {self.__class__.__name__}"

    def consumo(self, km):
        raise NotImplementedError("Este método debe implementarse en las subclases.")