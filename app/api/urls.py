from flask import Blueprint

from app.services.services import create_employee, create_address, create_person, delete_employee, delete_address, \
    delete_person, getall_employee, getall_address, getall_person, get_emp, get_person, get_address, update_employee, \
    update_address, update_person, blog, login
import opentracing
from flask_opentracing import FlaskTracing

from flasgger.utils import swag_from

index = Blueprint('index', __name__)


def initialize_tracer():
    return opentracing_tracer

tracing = FlaskTracing(initialize_tracer, ...)


@index.route('/logging')
def logg():
    return blog()


@index.route('/login/user', methods=['POST'])
# @swag_from('utils/login.yml')
def loginuser():
    return login()


@index.route('/create/employee', methods=['POST'])
@swag_from('utils/post_employee.yml')
def employee():
    return create_employee()


@index.route('/create/address', methods=['POST'])
@swag_from('utils/post_address.yml')
def address():
    return create_address()


@index.route('/create/person', methods=['POST'])
@swag_from('utils/post_person.yml')
def person():
    return create_person()


@index.route('/delete/employee/<id>', methods=['DELETE'])
def del_emp(id):
    return delete_employee(id)


@index.route('/delete/address/<id>', methods=['DELETE'])
def del_address(id):
    return delete_address(id)


@index.route('/delete/person/<id>', methods=['DELETE'])
def del_person(id):
    return delete_person(id)


@index.route('/getall/employee', methods=['GET'])
@swag_from('utils/getall_employee.yml')
def getall_emp():
    return getall_employee()


@index.route('/getall/address', methods=['GET'])
@swag_from('utils/getall_address.yml')
def geall_address():
    return getall_address()


@index.route('/getall/person', methods=['GET'])
@swag_from('utils/getall_person.yml')
def getal_per():
    return getall_person()


@index.route('/get/employee/<id>', methods=['GET'])
@swag_from('utils/get_employee.yml')
def getemp_particular(id):
    return get_emp(id)


@index.route('/get/address/<id>', methods=['GET'])
def getaddress_particular(id):
    return get_address(id)


@index.route('/get/person/<id>', methods=['GET'])
def getperson_particular(id):
    return get_person(id)


@index.route('/update/employee/<id>', methods=['PUT'])
def update_emp(id):
    return update_employee(id)


@index.route('/update/address/<id>', methods=['PUT'])
def update_address(id):
    return update_address(id)


@index.route('/update/person/<id>', methods=['PUT'])
def update_empdet(id):
    return update_person(id)
