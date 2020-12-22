from mongoengine import *


connect("base", username='mongo', password='mongo',
        authentication_source='root',
        host='mongo', port=27017)


class Employee(Document):
    name = StringField()
    email = StringField(unique=True, required=True)
    age = IntField()
    company = StringField()
    join_date = DateTimeField()
    job_title = StringField()
    gender = StringField()
    salary = IntField(default=0)