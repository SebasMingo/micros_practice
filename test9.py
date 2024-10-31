# Crear la Ruta para Obtener Productos (GET): Define una ruta que responda al método GET y devuelva una lista de productos. La lista puede ser estática o vacía al principio y se enviará en formato JSON.

from flask import Flask, request, jsonify

app = Flask(__name__)

productos = ["Coca cola", "Pepsi", "Fanta"]

@app.route('/productos', methods=['GET'])
def productos_func():
    #datos = request.get_json()

    return jsonify(productos)

if __name__ == '__main__':
    app.run(debug= True)