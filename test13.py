# Ejercicio 2: API REST para Gestionar Usuarios
# Crear la Ruta para Obtener Usuarios (GET): Define una ruta que responda al método GET y devuelva una lista de usuarios. Cada usuario debe tener un nombre y un correo electrónico.

# Crear la Ruta para Registrar Usuarios (POST): Define una ruta que responda al método POST, recibiendo en formato JSON los datos de un usuario nuevo (nombre y correo). Agrega el usuario a la lista de usuarios si el correo electrónico no se repite; en caso contrario, envía un mensaje de error indicando que el correo ya está registrado.

# Probar la API:

# Envía una solicitud GET para obtener la lista inicial de usuarios.
# Luego, realiza solicitudes POST para agregar varios usuarios, y verifica que no se permite registrar dos veces el mismo correo electrónico.
from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = [{'nombre':'sebasmingo', 'email':'sebas_mingo@hotmail.com'}, 
            {'nombre':'nico_mingo','email':'nico_mingo@hotmail.com'}]

@app.route('/obtener_usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)


@app.route('/registrar_usuarios', methods=['POST'])
def registrar_usuarios():
    datos = request.get_json()
    nombre = datos.get('nombre')
    email = datos.get('email')

    for usuario in usuarios:
        if email == usuario["email"]:
            return jsonify({'Error':'El correo ya esta registrado'}),400
            
        
    
    usuarios.append({'nombre':nombre,'email':email})
    return jsonify({'Mensaje':'El usuario ha sido registrado con exito'}), 201

if __name__ == '__main__':
    app.run(debug=True)