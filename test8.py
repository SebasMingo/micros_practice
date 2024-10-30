from flask import Flask, request, jsonify

app = Flask(__name__)

diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}

@app.route('/traer', methods=['GET'])
def traer():
    for clave in diccionario:
        return diccionario['clave1'], diccionario['clave2']
        
print(traer())


if __name__ == '__main__':
    app.run(debug= True)