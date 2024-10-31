# from flask import Flask, request, jsonify

productos = [{'producto1':'Cocacola','producto2':'Pepsi','producto3':'Fanta'},{'producto4':'Niko','producto5':'DelaCosta','producto6':'Piri'}]

# app= Flask(__name__)

# @app.route('/productos', methods=['GET'])
def productos_funcion(producto):
    # datos = request.get_json()
    # producto1 = datos.get("Cocacola")
    # producto2 = datos.get('Pepsi')
    # producto3 = datos.get('Fanta')
    for producto in productos:
        if productos[1]['producto6'] == 'Piri':
            return productos
        

variable = productos_funcion("Piri")
print(f'Lo que estas buscando es {variable}')

# if __name__ == '__main__':
#     app.run(debug=True)