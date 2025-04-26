# Autor: Yoporolo
# Proyecto: Gestor de tareas
# Descripcion: Una app de consola que te permite gestionar tus tareas.

import sqlite3
import time
import os

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def menu_principal():
    ejecutando = True
    while ejecutando:
        os.system("clear")
        print("Gestor de tareas.\n\n1. Añadir tarea\n2. Eliminar tarea\n3. Editar tarea\n4. Listar tareas\n5. Completar tarea\n6. Salir\n")
        usrInput = input("Selecciona una opcion: ")

        match (usrInput):
            case "1":
                titulo = input("Titulo: ")
                descripcion = input("Descripcion: ")
                fechaLimite = input("Fecha limite (XX/XX/XXXX): ")
                cursor.execute("insert into tareas (titulo, descripcion, fechaLimite) values (?, ?, ?)", (titulo, descripcion, fechaLimite))
                print("Tarea agregada correctamente.")
                connection.commit()
                time.sleep(1)
            case "2":
                titulo = input("Titulo: ")
                exist = cursor.execute("select * from tareas where titulo = ?", (titulo,)).fetchone()
                if exist:
                    cursor.execute("delete from tareas where titulo = ?", (titulo,))
                    print("Tarea eliminada correctamente.")
                    connection.commit()
                else:
                    print("No existe ninguna tarea con ese titulo.")
                time.sleep(1)
            case "3":
                titulo = input("Titulo: ")
                exist = cursor.execute("select * from tareas where titulo = ?", (titulo,)).fetchone()
                if exist:
                    newTitulo = input("Nuevo titulo: ")
                    newDescripcion = input("Nueva descripcion: ")
                    newFecha = input("Nueva fecha limite (XX/XX/XXXX): ")
                    cursor.execute("update tareas set titulo = ?, descripcion = ?, fechaLimite = ? where titulo = ?", (newTitulo, newDescripcion, newFecha, titulo))
                    print("La tarea se ha actualizado correctamente.")
                else:
                    print("No hay ninguna tarea con ese titulo.")
                time.sleep(1)
            case "4":
                os.system("clear")
                print("TAREAS")
                tareas = cursor.execute("select * from tareas").fetchone()
                while tareas:
                    print(f"\nTitulo: {tareas[0]}")
                    print(f"Descripcion: {tareas[1]}")
                    print(f"Fecha limite: {tareas[2]}")
                    print(f"Estatus: {tareas[3]}")
                    tareas = cursor.fetchone()
                input("\nPresiona ENTER para volver.")

            case "5":
                titulo = input("Titulo: ")
                exist = cursor.execute("select * from tareas where titulo = ?", (titulo,)).fetchone()
                if exist:
                    cursor.execute("update tareas set estatus = 'Completada' where titulo = ?", (titulo,))
                    print("Tarea completada correctamente.")
                    time.sleep(1)
            case "6":
                print("Saliendo...")
                connection.close()
                ejecutando = False
            case _:
                print("Opción inválida.")
                time.sleep(1)

menu_principal()