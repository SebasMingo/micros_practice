# //EJERCICIO

# // Descripción: Crea un sistema de registro donde el usuario debe ingresar un nombre, un email y una contraseña.
# // Requisitos:
# // Encripta la contraseña utilizando un método de hash seguro (puedes usar bcrypt o sha256).
# // Valida que el usuario ingrese todos los parámetros (nombre, email, contraseña).
# // Asegúrate de que el nombre de usuario no esté ya en uso (puedes usar una lista simulada de usuarios existentes).
# // Envía los datos a un servidor utilizando el método POST (simulado con un print).



from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

usuarios = ["Nicolas", "Fabio", "Chiara"]

@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    nombre = datos.get("nombre")
    email = datos.get("email")
    contrasena = datos.get("contrasena")

    if not nombre or not email or not contrasena:
        return jsonify({"error":"El nombre, el email y la contrasena son requeridos"}), 400
    
    if  nombre in usuarios:
        return jsonify({"error": "Este nombre de usuario ya existe"}), 400
    
    hash_object = hashlib.sha256(contrasena.encode('utf-8'))
    hashed_password = hash_object.hexdigest()

    print({
        "nombre": nombre, 
       "email" : email,
       "contrasena": hashed_password
       })

    usuarios.append(nombre)
    return jsonify({"mensaje":"Registro exitoso"}), 201

if __name__ == '__main__':
    app.run(debug=True)