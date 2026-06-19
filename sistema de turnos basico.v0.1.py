import os

turnos = []
def menu():
     opciones =[
     "agregar_turnos",
     "mostrar_turnos",
     "buscar_turnos",
     "eliminar_turnos",
     "salir"
    ]
     while True:                                    # ← el while sube aquí
        print("------MENU DE TURNOS------")        # ← el print queda dentro
        for i, opciones1 in enumerate(opciones, start=1):
            print(f"{i}. {opciones1}")
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 5:
            print("Opción inválida.")
        elif opcion == 1:
            agregar_turnos()
        elif opcion == 2:
            mostrar_turnos()
        elif opcion == 3:
            buscar_turnos()
        elif opcion == 4:
            eliminar_turnos()
        elif opcion == 5:
            print("saliendo del programa")
            break
def cargar_turnos():
    try:
        with open("turnos.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 3:               # ← validación defensiva
                    turno = {
                        "nombre": datos[0],
                        "fecha": datos[1],
                        "hora": datos[2]
                    }
                    turnos.append(turno)
        print("Turnos cargados:", len(turnos))
    except FileNotFoundError:
        print("No existe ningún archivo de turnos todavía.")
def agregar_turnos():
        nombre = input("Ingrese el nombre y apellido del paciente: ")
        while not nombre:
            print("El nombre no puede estar vacío.")
            nombre = input("Ingrese el nombre y apellido del paciente: ")
        while True:
         fecha = input("Ingrese la fecha del turno (dd/mm): ")
         partes = fecha.split("/")
         if len(partes) != 2:
             print("Fecha inválida.")
             continue
         try:
             dia = int(partes[0])
             mes = int(partes[1])
         except ValueError:
            print("Fecha inválida.")
            continue
         if dia < 1 or dia > 31 or mes < 1 or mes > 12:
            print("Fecha inválida.")
            continue
         print("Fecha agregada correctamente.")
         for t in turnos:
             if t["nombre"] == nombre and t["fecha"] == fecha:
                 print("El paciente ya tiene un turno en esa fecha.")
                 return
         break
        horarios = [
         "9:00 - 10:00",
         "10:00 - 11:00",
         "13:00 - 14:00",
         "14:00 - 15:00",
         "15:00 - 16:00"
         ]
        print("Horarios disponibles:") 
        for i, hora in enumerate(horarios, start=1):
             print(f"{i}. {hora}")
        while True:
             opcion = int(input("Seleccione una opción: "))
             if opcion < 1 or opcion > len(horarios):
                 print("Opción inválida.")
             else:
                  hora = horarios[opcion - 1]
                  turno = {
                 "nombre": nombre,
                 "fecha": fecha,
                 "hora": hora
                 }
             turnos.append(turno)
             print(
                "Turno seleccionado para",
                nombre,
                "en la fecha",
                fecha,
                "entre las",
                hora
                )
             guardar_turnostxt()
             return
def mostrar_turnos():
        if not turnos:
                 print("No hay turnos agendados.")
                 return
        else:
                 for turno in turnos:
                  print(turno["nombre"],
                  "-",
                 turno["fecha"],
                  "-",
                  turno["hora"]
                 )
        return
def buscar_turnos():
    nombre = input("Ingrese el nombre del paciente a buscar: ")

    for turno in turnos:
        if turno["nombre"] == nombre:
            print(
                turno["nombre"],
                "-",
                turno["fecha"],
                "-",
                turno["hora"]
            )
            return
    print("Paciente no encontrado.")
def eliminar_turnos():
    nombre = input("Ingrese el nombre del paciente a eliminar: ")
    for turno in turnos:
        if turno["nombre"] == nombre:
            turnos.remove(turno)
            print(f"Turno de {nombre} eliminado correctamente.")
            guardar_turnostxt()
            return
    print("Paciente no encontrado.")
def guardar_turnostxt():
        with open("turnos.txt", "w") as f:
            for turno in turnos:
                f.write(f"{turno['nombre']},{turno['fecha']},{turno['hora']}\n")
        print("Turnos guardados en un archivo de texto...")


cargar_turnos()
menu()