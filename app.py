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
        {'nombre': 'raton','precio': 7.55,'stock': 4,'categoria':'electronica'},
        {'nombre': 'raton','precio': 7.55,'stock': 4,'categoria':'electronica'},
        {'nombre': 'raton','precio': 7.55,'stock': 4,'categoria':'electronica'},
        {'nombre': 'raton','precio': 7.55,'stock': 4,'categoria':'electronica'},
        {'nombre': 'raton','precio': 7.55,'stock': 4,'categoria':'electronica'},
        {'nombre': 'raton','precio': 7.55,'stock': 4,'categoria':'electronica'},
        {'nombre': 'raton','precio': 7.55,'stock': 4,'categoria':'electronica'},
        {'nombre': 'raton','precio': 7.55,'stock': 4,'categoria':'electronica'},
        {'nombre': 'raton','precio': 7.55,'stock': 4,'categoria':'electronica'},
        {'nombre': 'raton','precio': 7.55,'stock': 4,'categoria':'electronica'},
        ]
    clientes = [
        {'nombre': 'Fran','email': 'fran@gmail.com','activo': True,'pedidos': 3},
        {'nombre': 'Fran','email': 'fran@gmail.com','activo': True,'pedidos': 3},
        {'nombre': 'Fran','email': 'fran@gmail.com','activo': True,'pedidos': 3},
        {'nombre': 'Fran','email': 'fran@gmail.com','activo': True,'pedidos': 3},
        {'nombre': 'Fran','email': 'fran@gmail.com','activo': True,'pedidos': 3},
        {'nombre': 'Fran','email': 'fran@gmail.com','activo': True,'pedidos': 3},
        {'nombre': 'Fran','email': 'fran@gmail.com','activo': True,'pedidos': 3},
        {'nombre': 'Fran','email': 'fran@gmail.com','activo': True,'pedidos': 3},
        {'nombre': 'Fran','email': 'fran@gmail.com','activo': True,'pedidos': 3},
        {'nombre': 'Fran','email': 'fran@gmail.com','activo': True,'pedidos': 3},
    ]
    pedidos = [
        {'cliente':'Fran','total':15,'fecha':'12-12-24'}
    ]
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run()
