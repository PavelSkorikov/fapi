from fastapi import FastAPI

from model import Employee





app = FastAPI()

@app.get('/')
async def index():
  employee = Employee(
    name="Павел",
    email="spg@mail.ru",
    age=45,
    company="microsoft",
    job_title="fsd",
    gender="муж",
    salary=70
  ).save()
  return {'hello': 'world'}
