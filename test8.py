from flask import Flask, request, jsonify

app = Flask(__name__)

diccionario = [{"clave1": "valor1"},{"clave2": "valor2"},{"clave3": "valor3"} ]


#traer titulo y descripcion siendo las claves y los valores estos ultimos
@app.route('/traer', methods=['GET'])
def traer():
    for clave in diccionario:
        return diccionario[0]['clave1'], diccionario[1]['clave2']
        
print(traer())


if __name__ == '__main__':
    app.run(debug= True)