
from plugin import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emp_name = db.Column(db.String(50))
    emp_position = db.Column(db.String(50))
    emp_experience = db.Column(db.String(50))
    emp_salary = db.Column(db.String(50))
    addresses = db.relationship('Address', backref='emp', lazy='joined')
    person = db.relationship('Person',backref='empref', lazy=True)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    fname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    street = db.Column(db.String(50))
    city = db.Column(db.String(50))
    pin_code = db.Column(db.Integer)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    lname = db.Column(db.String(50))

