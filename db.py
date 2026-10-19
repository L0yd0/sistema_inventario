import mongoengine as me 

def conectar_bd(uri_atlas: str):
    try:
        me.connect(host=uri_atlas)
        print("coneccion exitosa a mongo atlas")
    except Exception as e:
        print("Error al conectar a la base de datos")
        raise e

    