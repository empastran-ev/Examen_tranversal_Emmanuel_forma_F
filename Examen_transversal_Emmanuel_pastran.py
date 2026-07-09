def validar_titulo(titulo):
    return len(titulo.strip()) > 0


def validar_duracion(duracion_str):
    if duracion_str.isdigit():
        duracion = int(duracion_str)
        return duracion > 0
    return False


def validar_calificacion(calificacion_str):
    try:
        calificacion = float(calificacion_str)
        return 0.0 <= calificacion <= 10.0
    except ValueError:
        return False

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    opcion = input("Seleccione una opción (1-6): ")
    if opcion.isdigit():
        return int(opcion)
    return -1


def agregar_pelicula(lista_peliculas):
    titulo = input("Ingrese el título de la película: ")
    duracion_raw = input("Ingrese la duración (en minutos): ")
    calificacion_raw = input("Ingrese la calificación (0.0 a 10.0): ")

    if not validar_titulo(titulo):
        print("Error: El título no puede estar vacío ni contener solo espacios.")
        return

    if not validar_duracion(duracion_raw):
        print("Error: La duración debe ser un número entero mayor que cero.")
        return

    if not validar_calificacion(calificacion_raw):
        print("Error: La calificación debe ser un número decimal entre 0.0 y 10.0.")
        return

    nueva_pelicula = {
        "titulo": titulo.strip(),
        "duracion": int(duracion_raw),
        "calificacion": float(calificacion_raw),
        "disponible": False
    }

    lista_peliculas.append(nueva_pelicula)
    print(f"¡Película '{titulo}' agregada con éxito!")


def buscar_pelicula(lista_peliculas, titulo_buscar):
    for i in range(len(lista_peliculas)):
        if lista_peliculas[i]["titulo"] == titulo_buscar:
            return i
    return -1


def eliminar_pelicula(lista_peliculas):
    titulo_eliminar = input("Ingrese el título de la película a eliminar: ")

    posicion = buscar_pelicula(lista_peliculas, titulo_eliminar)

    if posicion != -1:
        pelicula_eliminada = lista_peliculas.pop(posicion)
        print(f"¡La película '{pelicula_eliminada['titulo']}' fue eliminada exitosamente!")
    else:
        print(f"La película '{titulo_eliminar}' no se encuentra registrada.")


def actualizar_disponibilidad(lista_peliculas):
    for pelicula in lista_peliculas:
        if pelicula["calificacion"] >= 7.0:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False


def mostrar_peliculas(lista_peliculas):
    actualizar_disponibilidad(lista_peliculas)

    if not lista_peliculas:
        print("\nNo hay películas registradas en el sistema.")
        return

    print("\n=== LISTA DE PELICULAS ===")
    for pelicula in lista_peliculas:
        estado_visual = "DISPONIBLE" if pelicula["disponible"] else "NO RECOMENDADA"

        print(f"Título: {pelicula['titulo']}")
        print(f"Duración: {pelicula['duracion']}")
        print(f"Calificación: {pelicula['calificacion']}")
        print(f"Estado: {estado_visual}")
        print("********************************************")


def main():
    peliculas = []

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_pelicula(peliculas)

        elif opcion == 2:
            titulo_b = input("Ingrese el título de la película a buscar: ")
            posicion = buscar_pelicula(peliculas, titulo_b)

            if posicion != -1:
                p = peliculas[posicion]
                estado_visual = "DISPONIBLE" if p["disponible"] else "NO RECOMENDADA"
                print(f"\n[Película Encontrada en la posición {posicion}]")
                print(f"Título: {p['titulo']}")
                print(f"Duración: {p['duracion']} minutos")
                print(f"Calificación: {p['calificacion']}")
                print(f"Estado: {estado_visual}")
            else:
                print("Película no encontrada.")

        elif opcion == 3:
            eliminar_pelicula(peliculas)

        elif opcion == 4:
            actualizar_disponibilidad(peliculas)
            print("¡Disponibilidad de todas las películas actualizada con éxito!")

        elif opcion == 5:
            mostrar_peliculas(peliculas)

        elif opcion == 6:
            print("“Gracias por usar el sistema. Vuelva Pronto”")
            break

        else:
            print("Opción inválida. Por favor, intente nuevamente.")


if __name__ == "__main__":
    main()