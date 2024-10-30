# Crear un registro de usuarios: Configura un diccionario o base de datos donde se guardarán los datos de los usuarios.

# Recibir datos por método POST: Diseña el sistema para recibir información, como el correo electrónico y la contraseña del usuario, utilizando el método POST.

# Validación de parámetros obligatorios: Asegúrate de que todos los campos necesarios, como correo electrónico y contraseña, estén completos antes de procesar los datos.

# Verificar unicidad del nombre de usuario: Revisa que el nombre de usuario no exista ya en el registro o base de datos; es decir, que no haya usuarios duplicados.

# Enviar los datos si todos los campos son válidos: Solo cuando todas las condiciones estén correctas, envía o guarda la información del usuario en el sistema.

from flask import Flask, request, jsonify

app = Flask(__name__)

if __name__ == 'main':
    app.run(debug=True)
