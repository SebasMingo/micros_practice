# Crear la Ruta para Agregar Productos (POST): Define una ruta que responda al método POST, la cual recibe datos en formato JSON para agregar un nuevo producto a la lista de productos. Los datos recibidos deben validarse mínimamente (por ejemplo, verificar que incluyan nombre y precio).

from flask import Flask, request, jsonify

app = Flask(__name__)

productos = []

@app.route('/productos', methods=["POST"])
def productos_func():
    datos = request.get_json()
    nombre = datos.get("nombre")
    precio = datos.get("precio")

    if not nombre or  precio is None:
        return jsonify({"Error":"Debe incluir nombre y precio"}),400
    
    nuevo_producto = {"nombre":nombre,"precio":precio}
    productos.append(nuevo_producto)
    
    return jsonify({"Mensaje":'Producto agregado exitosamente', 'Producto': nuevo_producto}),200

if __name__ == '__main__':
    app.run(debug=True)