from datetime import date
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    nombre_admin = "Francisco"
    tienda = "TecnoMarket"
    fecha = date.today()
    productos = [
        {'nombre': 'ratón', 'precio': 7.99, 'stock': 5, 'categoría': 'electrónica'},
        {'nombre': 'teclado', 'precio': 18.50, 'stock': 7, 'categoría': 'electrónica'},
        {'nombre': 'monitor', 'precio': 150.99, 'stock': 0, 'categoría': 'electrónica'},
        {'nombre': 'silla', 'precio': 9.50, 'stock': 10, 'categoría': 'muebles'},
        {'nombre': 'mesa', 'precio': 39.99, 'stock': 4, 'categoría': 'muebles'},
        {'nombre': 'sillon-relax', 'precio':125.50, 'stock': 1, 'categoría': 'muebles'},
        {'nombre': 'camiseta', 'precio': 19.50, 'stock': 8, 'categoría': 'ropa'},
        {'nombre': 'pantalón', 'precio': 24.50, 'stock': 2, 'categoría': 'ropa'},
        {'nombre': 'calcetines', 'precio': 3.99, 'stock': 20, 'categoría': 'ropa'},
        {'nombre': 'consola-Switch', 'precio': 399.00, 'stock': 0, 'categoría': 'consola'}
    ]
    clientes = [
        {'nombre': 'Fran', 'email': 'fran@gmail.com', 'activo': True, 'pedidos': 3},
        {'nombre': 'José', 'email': 'jose@gmail.com', 'activo': False, 'pedidos': 1},
        {'nombre': 'Ana', 'email': 'ana@gmail.com', 'activo': True, 'pedidos': 5},
        {'nombre': 'Juan', 'email': 'juan@gmail.com', 'activo': True, 'pedidos': 1}
    ]
    pedidos = [
        {'cliente': 'Fran', 'total': 36.48, 'fecha': '24-10-2024'},
        {'cliente': 'Fran', 'total': 58.99, 'fecha': '10-1-2025'},
        {'cliente': 'Fran', 'total': 45.98, 'fecha': '5-3-2025'},
        {'cliente': 'José', 'total': 125.50, 'fecha': '20-2-2025'},
        {'cliente': 'Ana', 'total': 63.95, 'fecha': '13-5-2024'},
        {'cliente': 'Ana', 'total': 77.99, 'fecha': '8-9-2024'},
        {'cliente': 'Ana', 'total': 53.98, 'fecha': '16-12-2024'},
        {'cliente': 'Ana', 'total': 63.95, 'fecha': '5-2-2025'},
        {'cliente': 'Ana', 'total': 39.90, 'fecha': '22-5-2025'},
        {'cliente': 'Juan', 'total': 45.49, 'fecha': '1-4-2025'}
    ]
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run()
