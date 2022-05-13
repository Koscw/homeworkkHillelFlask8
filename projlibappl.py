from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class EmployeeModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(), unique=True)
    name = db.Column(db.String())
    creation_date = db.Column(db.Integer())
    description = db.Column(db.String(80))
    deadline = db.Column(db.Integer())

    def __init__(self, employee_id, name, creation_date, description, deadline):
        self.employee_id = employee_id
        self.name = name
        self.creation_date = creation_date
        self.description = description
        self.deadline = deadline
    def __repr__(self):
        return f"{self.name}:{self.employee_id}"
