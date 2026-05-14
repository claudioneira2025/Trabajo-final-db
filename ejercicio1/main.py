#con esta import conectamos a la base de datos 
from conexion import vehiculos

from clases.automovil   import Automovil
from clases.motocicleta import Motocicleta
from clases.camion      import Camion
from clases.flota       import Flota

#mostrar menu es el sistema para registrar modificar buscar en la base de datos
def mostrar_menu():
    print("\n     SISTEMA DE GESTIÓN DE FLOTA     \n")
    print("1- Registrar vehículo")
    print("2- Eliminar vehículo")
    print("3- Buscar vehículo")
    print("4- Mostrar todos los vehículos")
    print("5- Consumo total de la flota")
    print("6- Actualizar vehiculo")
    print("7- Salir")
    return input("\nSeleccione una opción: ")


def registrar_vehiculo(flota):

    print("\n    Registrar Vehículo    \n")

    patente = input("Patente: ").upper()
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = int(input("Año: "))

    print("\nTipo de vehículo:")
    print("1- Automóvil")
    print("2- Motocicleta")
    print("3- Camión")

    tipo = input("Opción: ")

    datos_extra = {}

    if tipo == "1":

        tipo_texto = "automovil"

        puertas = int(input("Cantidad de puertas: "))
        combustible = input("Combustible: ")
        rendimiento = float(input("Rendimiento km/l: "))
        cilindrada = float(input("Cilindrada (ej: 1600 o 1.6): "))

        v = Automovil(patente, marca, modelo, año, puertas)

        datos_extra = {
            "puertas": puertas,
            "combustible": combustible,
            "rendimiento_km_l": rendimiento,
            "cilindrada_cc": cilindrada
        }

    elif tipo == "2":

        tipo_texto = "motocicleta"

        cilindrada = float(input("Cilindrada (ej: 250 o 0.25): "))
        rendimiento = float(input("Rendimiento km/l: "))

        v = Motocicleta(patente, marca, modelo, año, cilindrada)

        datos_extra = {
            "cilindrada_cc": cilindrada,
            "rendimiento_km_l": rendimiento
        }

    elif tipo == "3":

        tipo_texto = "camion"

        carga = float(input("Capacidad de carga (kg): "))
        ejes = int(input("Número de ejes: "))
        rendimiento = float(input("Rendimiento km/l: "))
        cilindrada = float(input("Cilindrada (ej: 5000 o 5.0): "))

        v = Camion(patente, marca, modelo, año, carga)

        datos_extra = {
            "capacidad_carga": carga,
            "numero_ejes": ejes,
            "rendimiento_km_l": rendimiento,
            "cilindrada_cc": cilindrada
            
        }

    else:
        print("Opción inválida.")
        return

    if flota.agregar(v):

        vehiculos.insert_one({

            "patente": patente,
            "marca": marca,
            "modelo": modelo,
            "anio": año,
            "tipo": tipo_texto,
            "detalles": datos_extra
        })

        print("Vehículo agregado correctamente.")

    else:
        print("Error: ya existe un vehículo con esa patente.")


def eliminar_vehiculo(flota):

    patente = input("Patente a eliminar: ").upper()

    resultado = vehiculos.delete_one({"patente": patente})

    if resultado.deleted_count > 0:
        print("Vehículo eliminado.")
    else:
        print("No existe ese vehículo.")

def actualizar_vehiculo():

    patente = input("Patente del vehículo a actualizar: ").upper()

    v = vehiculos.find_one({
        "patente": patente
    })

    if not v:
        print("Vehículo no encontrado.")
        return

    print("\n    Datos actuales    \n")

    print(v)

    print("\n    Nuevos datos    \n")

    nueva_marca = input("Nueva marca: ")
    nuevo_modelo = input("Nuevo modelo: ")
    nuevo_anio = int(input("Nuevo año: "))

    tipo = v["tipo"]

    detalles = {}

    if tipo == "automovil":

        puertas = int(input("Cantidad de puertas: "))
        combustible = input("Combustible: ")
        rendimiento = float(input("Rendimiento km/l: "))
        cilindrada = float(input("Cilindrada (ej: 1600 o 1.6): "))

        detalles = {
            "puertas": puertas,
            "combustible": combustible,
            "rendimiento_km_l": rendimiento,
            "cilindrada_cc": cilindrada
        }

    elif tipo == "motocicleta":

        cilindrada = float(input("Cilindrada (ej: 250 o 0.25): "))
        rendimiento = float(input("Rendimiento km/l: "))

        detalles = {
            "cilindrada_cc": cilindrada,
            "rendimiento_km_l": rendimiento
        }

    elif tipo == "camion":

        carga = float(input("Capacidad de carga: "))
        ejes = int(input("Número de ejes: "))
        rendimiento = float(input("Rendimiento km/l: "))
        cilindrada = float(input("Cilindrada (ej: 5000 o 5.0): "))

        detalles = {
            "capacidad_carga_ton": carga,
            "numero_ejes": ejes,
            "rendimiento_km_l": rendimiento,
            "cilindrada_cc": cilindrada
        }

    vehiculos.update_one(

        {"patente": patente},

        {
            "$set": {

                "marca": nueva_marca,
                "modelo": nuevo_modelo,
                "anio": nuevo_anio,
                "detalles": detalles
            }
        }
    )

    print("\nVehículo actualizado correctamente.")       

#En busar vehivulo como en las otras funciones incorporamos upper para buscar sin problemas de mayusculas 
# y minisculas y la busqueda sea mas fluida y la busqueda la dejamos por patente ya que es mas exacta  
def buscar_vehiculo(flota):

    patente = input("Patente: ").upper()

    v = vehiculos.find_one({
        "patente": patente
    })

    if v:

        print("\n    Vehículo encontrado    \n")

        print(f"Patente: {v['patente']}")
        print(f"Marca: {v['marca']}")
        print(f"Modelo: {v['modelo']}")
        print(f"Año: {v['anio']}")
        print(f"Tipo: {v['tipo']}")

        print("\n--- Detalles ---")

        detalles = v.get("detalles", {})

        for clave, valor in detalles.items():

            if isinstance(valor, float):
                print(f"{clave}: {valor:g}")
            else:
                print(f"{clave}: {valor}")

        print("\n-------------------------")

    else:
        print("Vehículo no encontrado.")

#En esta funcion mostramos los vehiculos que estan en studio3t con 5 descripciones las mas relevantes patente,marca,modelo,
# año y tipo (automovil,motocicleta,camion)
# ademas incertamos una funcion para que aparesca tanto cilindrada 
# como 1600 o como 1.6 y otra funcion para que no aparesca ceros inecesario
# como 1600.0 solo aparecera 1600 o 1.6 ejemplo en studio3t cilindrada se guardara como 2.0 en python aparecera como 2
def mostrar_vehiculos(flota):

    print("\n    Vehículos registrados en Mi Base De Datos    \n")

    datos = vehiculos.find()

    for v in datos:

        print(f"Patente: {v['patente']}")
        print(f"Marca: {v['marca']}")
        print(f"Modelo: {v['modelo']}")
        print(f"Año: {v['anio']}")
        print(f"Tipo: {v['tipo']}")

        print("\n--- Detalles ---")

        detalles = v.get("detalles", {})

        for clave, valor in detalles.items():

            if isinstance(valor, float):
                print(f"{clave}: {valor:g}")
            else:
                print(f"{clave}: {valor}")

        print("\n-------------------------\n")


def consumo_total_flota(flota):
    km = float(input("Kilómetros del trayecto: "))
    total = flota.consumo_total(km)
    print(f"Consumo total estimado: {total:.2f} litros")


def main():
    flota = Flota()
#esto lo ocultamos ya que es del trabajo anteriorel cual no ocuparemos
#porque ahora exportamos directo de la base de datos 
    """# Vehículos Cargados de ejemplo
    flota.agregar(Automovil("AA1111", "Toyota", "Corolla", 2020, 4))
    flota.agregar(Motocicleta("BB2222", "Honda", "CBR300", 2019, 300))
    flota.agregar(Camion("CC3333", "Volvo", "FH16", 2018, 8000))
    flota.agregar(Automovil("DD4444", "SUBARU","IMPREZA",2007,1600))"""

    while True:
        op = mostrar_menu()

        if op == "1":
            registrar_vehiculo(flota)
        elif op == "2":
            eliminar_vehiculo(flota)
        elif op == "3":
            buscar_vehiculo(flota)
        elif op == "4":
            mostrar_vehiculos(flota)
        elif op == "5":
            consumo_total_flota(flota)
        elif op == "6":
            actualizar_vehiculo()
        elif op == "7":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()