import datetime
from functools import wraps

import jwt
from flask import request, make_response, jsonify, app, Flask
from plugin import db
from app.models.models import Employee,Person,Address


def blog():
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    return f"Welcome to the Blog"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token = request.headers.get('token')
        except Exception as e:
            return jsonify({'message': 'Token is missing'})
        try:
            data = jwt.decode(token, key="my@12345", algorithms=["HS256"])
        except Exception as e:
            return jsonify({'message': "Token is invalid"})
        return f(*args, **kwargs)
    return decorated


def login():
    data = request.json
    user = Person.query.filter_by(username=data["username"]).first()
    try:
        if user and user.password:
            token = jwt.encode({'user': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, key="my@12345", algorithm='HS256')
            return token
        else:
            return "check username and password"
    except Exception as e:
        response = {"error": e}
        return response


def create_employee():
    data = request.json
    employee = Employee(**data)
    db.session.add(employee)
    db.session.commit()
    return "Employee Added Successfully"


def create_address():
    data = request.json
    employee =data.pop('emp_id')
    value = Employee.query.filter_by(id=employee).first()
    address = Address(**data, emp=value)
    db.session.add(address)
    db.session.commit()
    return "Address Added Successfully"


def create_person():
    data = request.json
    employee =data.pop('emp_id')
    value = Employee.query.filter_by(id=employee).first()
    person = Person(**data, empref=value)
    db.session.add(person)
    db.session.commit()
    return "Person Added Successfully"

@token_required
def delete_employee(id):
    db.session.query(Employee).filter_by(id=id).delete()
    db.session.commit()
    return "Employee deleted"

@token_required
def delete_address(id):
    db.session.query(Address).filter_by(id=id).delete()
    db.session.commit()
    return "Address deleted"

@token_required
def delete_person(id):
    db.session.query(Person).filter_by(id=id).delete()
    db.session.commit()
    return "Person deleted"

@token_required
def getall_employee():
    employees = Employee.query.all()
    employee_list = []
    for employee in employees:
        getemp = employee.__dict__
        del getemp["_sa_instance_state"]
        del getemp['addresses']
        employee_list.append(getemp)
    return jsonify(employee_list)

@token_required
def getall_address():
    address = Address.query.all()
    address_list = []
    for addresses in address:
        getemp = addresses.__dict__
        del getemp["_sa_instance_state"]
        address_list.append(getemp)
    return jsonify(address_list)

@token_required
def getall_person():
    person = Person.query.all()
    person_list = []
    for persones in person:
        getemp = persones.__dict__
        del getemp["_sa_instance_state"]
        person_list.append(getemp)
    return jsonify(person_list)


def get_emp(id):
    employee = Employee.query.get(id)
    emp = employee.__dict__
    del emp["_sa_instance_state"]
    del emp['addresses']
    return jsonify(emp)


def get_address(id):
    address = Address.query.get(id)
    address_dict = address.__dict__
    del address_dict["_sa_instance_state"]
    return jsonify(address_dict)


def get_person(id):
    person = Person.query.get(id)
    person_dict = person.__dict__
    del person_dict["_sa_instance_state"]
    return jsonify(person_dict)


@token_required
def update_employee(id):
    data = request.json
    if data.emp_position == "HR":
        employee = Employee.query.get(id).update(data)
        db.session.commit()
        return jsonify(employee)
    else:
        return "permission denied"


def update_person(id):
    data = request.json
    employee = Employee.query.get(id).update(data)
    db.session.commit()
    return jsonify(employee)


def update_address(id):
    data = request.json
    employee = Employee.query.get(id).update(data)
    db.session.commit()
    return jsonify(employee)















