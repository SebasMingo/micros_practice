from flask import Flask, request, jsonify

productos = [{'producto1':'Cocacola'},{'producto2':'Pepsi'}, {'producto3':'Fanta'}]

app= Flask(__name__)

@app.route('/productos', methods=['GET'])
def productos_funcion(producto):
    # datos = request.get_json()
    # producto1 = datos.get("Cocacola")
    # producto2 = datos.get('Pepsi')
    # producto3 = datos.get('Fanta')
    for producto in productos:
        if producto == {'producto3':'Fanta'}:
            return productos[2]['producto3']

variable = productos_funcion("Fanta")
print(f'Lo que estas buscando es {variable}')

if __name__ == '__main__':
    app.run(debug=True)