# Sistema de Gestión de Inventario y Auditoría
## Integrantes: 
## Ricardo Vargas Rodriguez - 00515677
## Carola Mera Dragustinovis - 00553298
Aplicación modular interactiva en consola desarrollada en Python y conectada a MongoDB Atlas utilizando **MongoEngine** (ODM) para auditar un inventario de usuarios y artículos.

---

## 1. Organización del Código (Arquitectura)

El proyecto sigue una arquitectura en capas con separación clara de responsabilidades:

- **`db.py`**: Encargado de establecer y administrar la conexión a MongoDB Atlas mediante MongoEngine.
- **`models.py`**: Define los esquemas y modelos de datos (`Usuario` y `Articulo`) incluyendo sus reglas de validación.
- **`services.py`**: Capa de lógica de negocio que contiene las funciones CRUD, validación de integridad referencial y captura de excepciones.
- **`main.py`**: Interfaz de consola e interactividad con el usuario mediante menús y submenús dinámicos.

---

## 2. Justificación del Almacenamiento

- **Tecnología seleccionada:** MongoDB Atlas + MongoEngine (ODM).
- **Ventajas:**
  - **Esquema flexible y orientado a objetos:** MongoEngine mapea las colecciones directamente a clases de Python, facilitando las validaciones antes del guardado.
  - **Base de datos en la nube:** MongoDB Atlas provee almacenamiento en la nube en tiempo real sin requerir la instalación de un servidor local.
- **Desventajas / Limitaciones:**
  - **Dependencia de red:** Requiere una conexión a internet estable para realizar consultas e inserciones.

---

## 3. Estrategia de Claves (Primary Keys)

- **Usuarios:** Se utiliza el **`email`** como identificador único principal (`unique=True`), garantizando que no existan cuentas duplicadas.
- **Artículos:** Se utiliza el **`id`** (`ObjectId` automático de 24 caracteres de MongoDB). La relación con la persona responsable se maneja mediante un `ReferenceField` apuntando a la entidad `Usuario`.

---

## 4. Guía de Casos de Prueba (Testing)

1. **Flujo CRUD Normal:**
   - Se crearon, leyeron, actualizaron y eliminaron registros en ambas colecciones correctamente desde la consola.
2. **Caso de Fallo 1 (Usuario Inexistente - Integridad Referencial):**
   - Al intentar crear o actualizar un artículo ingresando el email de un usuario que no existe, el sistema rechaza la operación informando al usuario sin interrumpir el programa.
3. **Caso de Fallo 2 (Nombre de Artículo Vacío):**
   - Al intentar guardar un artículo con nombre vacío o compuesto solo por espacios en blanco, la función `.clean()` de MongoEngine activa un `ValidationError` controlado.
