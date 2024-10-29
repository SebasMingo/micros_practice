# // DEFINIR función "registrar_estudiante"
#     // OBTENER datos JSON de la solicitud
#     // EXTRAER "nombre", "edad" y "curso"

#     // SI "nombre", "edad" O "curso" es NULO
#         // DEVOLVER error 400
#     // FIN SI

#     // SI "edad" NO es positivo
#         // DEVOLVER error 400
#     // FIN SI

#     // AGREGAR estudiante a la lista "estudiantes"
#     // DEVOLVER éxito 201
# // FIN FUNCIÓN

# // SI el archivo es el principal
#     // INICIALIZAR "estudiantes" como lista vacía
#     // EJECUTAR aplicación en modo debug
# // FIN SI

from flask import Flask, requests, jsonify

app = Flask(__name__)

estudiantes = []

@app.route('/registrar_estudiante', methods=['POST'])
def registrar_estudiante():
    datos = requests.get_json()
    nombre = datos.get("nombre")
    edad = datos.get("edad")
    curso = datos.get("curso")

    if not nombre or not edad or not curso:
        return jsonify({"error": "La edad no es positiva"}), 401 
    if  edad <= 0:
        return jsonify({"error": "La edad no es positiva"}), 401 


    estudiantes.append({"nombre": nombre, "edad":edad, "curso": curso})
    return jsonify({"mensaje": "exito"}), 201


if __name__ == '__main__':
    app.run(debug= True)