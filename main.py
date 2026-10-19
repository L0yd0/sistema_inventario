import os
import sys
from dotenv import load_dotenv
from db import conectar_bd
import services as srv

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Obtener la URI desde las variables de entorno
uri_atlas = os.getenv("MONGO_URI")

def menu_usuarios():
    while True:
        print("\n--- MÓDULO DE USUARIOS ---")
        print("1. Crear Usuario")
        print("2. Listar Todos los Usuarios")
        print("3. Buscar Usuario por Email")
        print("4. Actualizar Usuario")
        print("5. Eliminar Usuario")
        print("6. Volver al Menú Principal")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n[ Registrar Nuevo Usuario ]")
            email = input("Email: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            srv.crear_usuario(email, nombre, apellido)

        elif opcion == "2":
            print("\n[ Lista de Usuarios ]")
            usuarios = srv.listar_usuarios()
            for u in usuarios:
                print(u)
            if not usuarios:
                print("No hay usuarios registrados en el sistema.")

        elif opcion == "3":
            print("\n[ Buscar Usuario ]")
            email = input("Ingrese el email a buscar: ")
            u = srv.buscar_usuario_por_email(email)
            if u:
                print(f"Encontrado: {u}")
            else:
                print("No se encontró ningún usuario con ese email.")

        elif opcion == "4":
            print("\n[ Actualizar Usuario ]")
            email = input("Ingrese el email del usuario a modificar: ")
            nom = input("Nuevo nombre (presione Enter para mantener el actual): ")
            ape = input("Nuevo apellido (presione Enter para mantener el actual): ")
            srv.actualizar_usuario(
                email, 
                nuevo_nombre=nom if nom else None, 
                nuevo_apellido=ape if ape else None
            )

        elif opcion == "5":
            print("\n[ Eliminar Usuario ]")
            email = input("Ingrese el email del usuario a eliminar: ")
            srv.eliminar_usuario(email)

        elif opcion == "6":
            break 
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_articulos():
    while True:
        print("\n--- MÓDULO DE ARTÍCULOS ---")
        print("1. Crear Artículo")
        print("2. Listar Todos los Artículos")
        print("3. Buscar Artículo por ID")
        print("4. Actualizar Artículo")
        print("5. Eliminar Artículo")
        print("6. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n[ Registrar Nuevo Artículo ]")
            nombre = input("Nombre del artículo: ")
            desc = input("Descripción: ")
            marca = input("Marca: ")
            email_usr = input("Email del usuario responsable: ")
            srv.crear_articulo(nombre, desc, marca, email_usr)

        elif opcion == "2":
            print("\n[ Lista de Artículos ]")
            articulos = srv.listar_articulos()
            for a in articulos:
                print(a)
            if not articulos:
                print("No hay artículos registrados en el sistema.")

        elif opcion == "3":
            print("\n[ Buscar Artículo por ID ]")
            art_id = input("Ingrese el ID del artículo: ")
            a = srv.buscar_articulo_por_id(art_id)
            if a:
                print(f"Encontrado: {a}")
            else:
                print("No se encontró ningún artículo con ese ID.")

        elif opcion == "4":
            print("\n[ Actualizar Artículo ]")
            art_id = input("Ingrese el ID del artículo a modificar: ")
            nom = input("Nuevo nombre (presione Enter para mantener el actual): ")
            desc = input("Nueva descripción (presione Enter para mantener el actual): ")
            marca = input("Nueva marca (presione Enter para mantener el actual): ")
            email_usr = input("Nuevo email de usuario responsable (presione Enter para mantener el actual): ")
            srv.actualizar_articulo(
                art_id,
                nuevo_nombre=nom if nom else None,
                nueva_descripcion=desc if desc else None,
                nueva_marca=marca if marca else None,
                email_usuario_modifico=email_usr if email_usr else None
            )

        elif opcion == "5":
            print("\n[ Eliminar Artículo ]")
            art_id = input("Ingrese el ID del artículo a eliminar: ")
            srv.eliminar_articulo(art_id)

        elif opcion == "6":
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

def main():
    print("Iniciando sistema de inventario...")

    if not uri_atlas:
        print("Error: No se encontró la variable MONGO_URI en el archivo .env")
        sys.exit(1)
    try:
        conectar_bd(uri_atlas)
    except Exception:
        print("no se pudo conectar debido a un fallo en la BD")
        sys.exit(1)

    while True:
        print("SISTEMA DE INVENTARIO")
        print("1. Modulo de usuarios")
        print("2. Modulo de articulos")
        print("3. Salir")

        opcion = input("seleccione una opcion: ").strip()

        if opcion == "1":
            print("\n[Entrando a los usuarios...]")
            menu_usuarios()
        elif opcion == "2":
            print("\n[Entrando a los productos...]")
            menu_articulos()
        elif opcion == "3":
            print("\nGracias por usar el sistema")
            break
        else:
            print("Opcion no valida, favor de poner una opcion valida")

if __name__ == "__main__":
    main()