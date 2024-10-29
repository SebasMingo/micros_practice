from flask import Flask, jsonify, request

#Inicializar la aplicacion de Flask
app = Flask(__name__)

# Datos de ejemplo
usuarios = {
    1: {"nombre": "Alice", "edad": 25},
    2: {"nombre": "Bob", "edad": 30}
}

# Ruta de inicio
@app.route("/")
def servidor():
    return "Bienvenido a mi servidor Flask!"

# Ruta de saludo con parametro en la URl
@app.route('/saludo/<nombre>', methods=['GET'])
def saludo(nombre):
    return jsonify( {"mensaje": f"Hola, {nombre}!"})

# Ruta para sumar dos numeros pasados como parametros en la URL
@app.route('/sumar', methods=['GET']) 
def sumar():
    #Obtener los parametros de la solicitud
    numero1 = request.args.get("numero1", default=0, type=int)
    numero2 = request.args.get("numero2", default=0, type=int)
    resultado = numero1 + numero2
    return jsonify({"resultado": resultado})

# Ruta para recibir y responder a datos en formato JSON
@app.route("/mensaje", methods=["POST"])
def mensaje():
    datos = request.get_json()
    mensaje = datos.get("mensaje", "")
    



if __name__ == '__main__':
    app.run(port=9000, debug=True)