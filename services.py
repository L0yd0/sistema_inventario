import mongoengine as me 
from models import Usuario, Articulo 

def crear_usuario(email: str, nombre: str, apellido: str):
    try:
        nuevo_usuario = Usuario(
            email=email.strip().lower(),
            nombre=nombre.strip(),
            apellido=apellido.strip()
        )
        nuevo_usuario.save()
        print(f"\n Usuario '{email}' registrado exitosamente")
        return nuevo_usuario
    except me.NotUniqueError:
        print(f"Error ya existe un usuario con el email {email}")
    except Exception as e:
        print(f"\n Error al registrar el usuario: {e}")
    return None

def listar_usuario():
    return list(Usuario.objects())

def buscar_usuario_por_correo(email:str):
    try:
        return Usuario.objects.get(email=email.strip().lower())
    except Usuario.DoesNotExist:
        return None

def actualizar_usuario(email: str, nuevo_nombre:str=None, nuevo_apellido: str = None):
    usuario=buscar_usuario_por_correo(email)
    if not usuario:
        print("no existe ese usuario")
        return None
    if nuevo_nombre:
        usuario.nombre = nuevo_nombre.strip()
    if nuevo_apellido:
        usuario.apellido = nuevo_apellido.strip()

    usuario.save()
    print(f"usuario '{email}' actualizado correctamente")
    return usuario

def eliminar_usuario(email:str):
    usuario = buscar_usuario_por_correo(email)
    if not usuario:
        print("no existe ese usuario")
        return False

    try:
        usuario.delete()
        print(f"Usuario '{email}' borrado correctamente")
        return True
    except me.OperationError:
        print(f"\n operacion rechazada: no se puede eliminar el usuario por que tiene articulos relacionados")
        return False

#--------ARTICULOS--------------
def crear_articulo(nombre: str, descripcion: str, marca: str, email_usuario: str):
    
    usuario = buscar_usuario_por_correo(email_usuario)
    if not usuario:
        print(f"\n❌ Operación rechazada: El usuario responsable con email '{email_usuario}' NO existe.")
        return None

    try:
        articulo = Articulo(
            nombre=nombre.strip(),
            descripcion=descripcion.strip(),
            marca=marca.strip(),
            usuario_modifico=usuario
        )
        articulo.clean() 
        articulo.save()
        print(f"\nArtículo '{nombre}' registrado exitosamente.")
        return articulo
    except me.ValidationError as ve:
        print(f"\nError de validación: {ve}")
    except Exception as e:
        print(f"\nError al crear el artículo: {e}")
    return None


def listar_articulos():
    return list(Articulo.objects())


def buscar_articulo_por_id(articulo_id: str):
    try:
        return Articulo.objects.get(id=articulo_id)
    except Exception:
        return None

def actualizar_articulo(
    articulo_id: str, 
    nuevo_nombre: str = None, 
    nueva_descripcion: str = None, 
    nueva_marca: str = None, 
    email_usuario_modifico: str = None
):
    articulo = buscar_articulo_por_id(articulo_id)
    if not articulo:
        print(f"\nError: No existe un artículo con el ID '{articulo_id}'.")
        return None

    if email_usuario_modifico:
        usuario = buscar_usuario_por_correo(email_usuario_modifico)
        if not usuario:
            print(f"\nOperación rechazada: El usuario responsable con email '{email_usuario_modifico}' NO existe.")
            return None
        articulo.usuario_modifico = usuario

    if nuevo_nombre is not None:
        articulo.nombre = nuevo_nombre.strip()
    if nueva_descripcion is not None:
        articulo.descripcion = nueva_descripcion.strip()
    if nueva_marca is not None:
        articulo.marca = nueva_marca.strip()

    try:
        articulo.clean() 
        articulo.save()
        print(f"\nArtículo con ID '{articulo_id}' actualizado correctamente.")
        return articulo
    except me.ValidationError as ve:
        print(f"\nError de validación: {ve}")
    except Exception as e:
        print(f"\nError al actualizar el artículo: {e}")
    return None


def eliminar_articulo(articulo_id: str):
    articulo = buscar_articulo_por_id(articulo_id)
    if not articulo:
        print(f"\nError: No existe un artículo con el ID '{articulo_id}'.")
        return False

    articulo.delete()
    print(f"\nArtículo eliminado exitosamente.")
    return True