from functools import wraps
from flask import Flask
from flask import request, jsonify
from cryptography.fernet import Fernet

# from flask_mongoengine import MongoEngine

app = Flask(__name__)

def cargar_clave():
	return open("clave.key","rb").read()


clave = cargar_clave()
f = Fernet(clave)
API_KEY='000000111111'

def api_key_required(api_key_info):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            api_key = request.headers.get('X-API-KEY')
            currenKey = api_key_info['key']
            allow = api_key_info['allow']

            if(api_key == None or allow == False):
                return jsonify({'message': 'Acceso no autorizado'}), 401
            try:
                decript = f.decrypt(api_key).decode()
                if decript == currenKey:
                    return func(*args, **kwargs)
            except:
                return jsonify({'message': 'Acceso no autorizado'}), 401

        return decorated_function
    return decorator


@app.route('/group01')
@api_key_required({'key': API_KEY, 'allow': True})
def group01():
    return jsonify({'result': 'este es el grupo 01'})


@app.route('/group02')
@api_key_required({'key': API_KEY, 'allow': False})
def group02():
    return jsonify({'result': 'este es el grupo 02'})


@app.route('/group03')
@api_key_required({'key': API_KEY, 'allow': False})
def group03():
    return jsonify({'result': 'este es el grupo 03'})


@app.route('/group04')
@api_key_required({'key': API_KEY, 'allow': False})
def group04():
    return jsonify({'result': 'este es el grupo 04'})


if __name__ == "__main__":
    app.run(debug=True, port=5000)

# readme
# pip install flask
