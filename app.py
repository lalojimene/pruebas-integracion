from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Datos simulados
productos = [
    {"id": 1, "nombre": "Camiseta", "precio": 20},
    {"id": 2, "nombre": "Pantalón", "precio": 35},
    {"id": 3, "nombre": "Zapatos", "precio": 50}
]
carrito = []

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

@app.route('/agregar/<int:id>')
def agregar(id):
    p = next((x for x in productos if x["id"] == id), None)
    if p:
        carrito.append(p)
    return redirect(url_for('index'))

@app.route('/carrito')
def ver():
    return render_template('carrito.html', carrito=carrito, total=sum(x["precio"] for x in carrito))

if __name__ == "__main__":
    app.run(debug=True)
