# Ejercicio: API REST para Gestionar Tareas
# Descripción
# Crea una API que permita gestionar una lista de tareas. La API tendrá las siguientes rutas GET:

# GET /tareas

# Descripción: Devuelve una lista de todas las tareas.
# Respuesta esperada: Una lista en formato JSON que contenga todas las tareas, donde cada tarea debe incluir un ID y una descripción.
# GET /tareas/<id>

# Descripción: Devuelve una tarea específica por su ID.
# Parámetros: ID de la tarea (entero).
# Respuesta esperada: Detalles de la tarea correspondiente al ID proporcionado. Si la tarea no se encuentra, debe devolver un mensaje de error con el código 404.
# GET /tareas/completadas

# Descripción: Devuelve una lista de tareas que están marcadas como completadas.
# Respuesta esperada: Una lista en formato JSON que contenga solo las tareas que están marcadas como completadas.
# Pruebas de la API
# Obtener todas las tareas:

# Realiza una solicitud GET a /tareas para obtener la lista completa de tareas.
# Obtener una tarea específica por ID:

# Realiza una solicitud GET a /tareas/1 para obtener la tarea con ID 1.
# Obtener solo tareas completadas:

# Realiza una solicitud GET a /tareas/completadas para obtener la lista de tareas que han sido completadas.
# Ejercicio Extra
# Agregar un manejo de errores: Implementa un manejo de errores para devolver mensajes personalizados si no se encuentra la tarea solicitada.
# Este ejercicio es sencillo y te ayudará a practicar la creación de rutas GET en una API REST. ¡Diviértete programando!

from flask import Flask, request, jsonify

app = Flask(__name__)

tareas = [{'id':'1','descripcion':'Limpiar'},
          {'id':'2','descripcion':'Pasear'},
          {'id':'3','descripcion':'Cortar'}]

@app.route('/tareas', methods=['GET'])
def tareas_func():
    return jsonify(tareas)

@app.route('/tareas/<id>', methods=['GET'])
def tareas_func():
    

if __name__ == '__main__':
    app.run(debug=True)