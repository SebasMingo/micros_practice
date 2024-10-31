from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Base de datos simulada
usuarios = [
    {'nombre': 'Sebastian', 'email': 'sebas_mingo@hotmail.com', 'password': generate_password_hash('1234')},
    {'nombre': 'Nicolas', 'email': 'nico_mingo@hotmail.com', 'password': generate_password_hash('5678')}
]

# Ruta para registrar un nuevo usuario
@app.route('/registrar', methods=['POST'])
def registrar():
    datos = request.get_json()
    nombre = datos.get('nombre')
    email = datos.get('email')
    password = datos.get('password')

    # Verificación de duplicado de email
    for usuario in usuarios:
        if usuario['email'] == email:
            return jsonify({'Error': 'El email ya existe'}), 400
    
    # Crear hash de la contraseña y agregar nuevo usuario
    password_hash = generate_password_hash(password)
    nuevo_usuario = {'nombre': nombre, 'email': email, 'password': password_hash}
    usuarios.append(nuevo_usuario)
    
    return jsonify({'Mensaje': 'Usuario registrado exitosamente'}), 201

# Ruta para iniciar sesión
@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    email = datos.get('email')
    password = datos.get('password')

    for usuario in usuarios:
        if usuario['email'] == email:
            if check_password_hash(usuario['password'], password):
                return jsonify({'Mensaje': f'Bienvenido, {usuario["nombre"]}'}), 200
            else:
                return jsonify({'Error': 'El password es incorrecto'}), 400

    # Si el email no existe
    return jsonify({'Error': 'El email no está registrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
