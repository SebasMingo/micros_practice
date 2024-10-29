# // CREAR lista "usuarios"

# // DEFINIR función "registrar_usuario"
# //     OBTENER datos JSON de la solicitud
# //     EXTRAER "email" y "password"
    
# //     SI "email" O "password" es NULO
# //         DEVOLVER mensaje de error y código 400
# //     SINO
# //         AGREGAR usuario a la lista "usuarios"
# //         DEVOLVER mensaje de éxito y código 201
# //     FIN SI
# // FIN FUNCIÓN

# // SI el archivo es el principal
# //     EJECUTAR la aplicación en modo debug
# // FIN SI
from flask import Flask, requests, jsonify

app= Flask(__name__)

usuarios = []

@app.route("/registrar_usuario", methods=["POST"])
def registrar_usuarios():
    datos = requests.get_json()
    email = datos.get("email")
    password = datos.get("password")

    if not email or not password:
        return jsonify({"Error": "El email y la contrasena son requeridos en el campo"}),400
    else:
        usuarios.append({"email": email, 'password': password} )
        return jsonify({"Mensaje": " Respuesta exitosa"}),200
    
if __name__ == '__main__':
    app.run(debug= True)

