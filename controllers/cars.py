from werkzeug.exceptions import BadRequest

cars = [
    {"id": 4, "make": "Toyota", "year": 1999},
    {"id": 2, "make": "Mercedes", "year": 1967},
    {"id": 1, "make": "BMW", "year": 2013},
    {"id": 3, "make": "Rolls-Royce", "year": 1990}
]

def index(req):
    return [c for c in cars], 200

def show(req, uid):
    return find_by_uid(uid), 200

def create(req):
    new_car = req.get_json()
    new_car['id'] = sorted([c['id'] for c in cars])[-1] + 1
    cars.append(new_car)
    return new_car, 201


def find_by_uid(uid):
    try:
        return next(car for car in cars if car['id'] == uid)
    except:
        raise BadRequest(f"We don't have that car with id: {uid}!")