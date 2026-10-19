import mongoengine as me 
import datetime

class Usuario(me.Document):
    email = me.EmailField(required=True, unique=True)
    nombre = me.StringField(required=True, max_length=100)
    apellido = me.StringField(required=True, max_length=100)
    fecha_creado = me.DateTimeField(default=lambda: datetime.datetime.now(datetime.timezone.utc))

    meta = {'collection': 'usuarios'}

    def __str__(self):
        return f"Email: {self.email} | Nombre: {self.nombre} {self.apellido}"

class Articulo(me.Document):
    nombre = me.StringField(required=True)
    descripcion = me.StringField(default="")
    marca = me.StringField(default="")

    usuario_modifico = me.ReferenceField(Usuario, required=True, reverse_delete_rule=me.DENY)
    meta = {'collection': 'productos'}

    def clean(self):
        if not self.nombre or not self.nombre.strip():
            raise me.ValidationError("el nombre del articulo no puede estar vacio")

    def __str__(self):
        email_resp = self.usuario_modifico.email if self.usuario_modifico else "Sin usuario"
        return f"ID: {self.id} | Articulo: {self.nombre} | Marca: {self.marca} | Modificado por {email_resp}"

    