from flask import Flask
from data.data_productos import productos, categorias

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola, soy Sofia Sferco. Me gusta programar en Python y estoy aprendiendo Flask."

@app.route('/productos')
def listar_productos():
    salida = ""
    for producto in productos:
        salida += f"ID: {producto['id']} - {producto['descripcion']} - Categoría: {producto['categoria_id']}<br>"
    return salida

@app.route('/categorias')
def listar_categorias():
    salida = ""
    for categoria in categorias:
        salida += f"ID: {categoria['id']} - {categoria['descripcion']}<br>"
    return salida

if __name__ == '__main__':
    app.run(debug=True)

