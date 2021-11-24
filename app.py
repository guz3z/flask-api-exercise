from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import cars


app = Flask(__name__)
CORS(app)


@app.route('/')
def home_handler():
    return "Welcome to our cars API"


@app.route('/cars', methods=['GET', 'POST'])
def all_cars():
    fns = {
        'GET': cars.index,
        'POST': cars.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/cars/<int:cars_id>', methods=['GET'])
def specific_car(cars_id):
    fns = {
        'GET': cars.show
    }
    resp, code = fns[request.method] (request, cars_id)
    return jsonify(resp), code


if __name__ == '__main__':
    app.run(debug=True)



