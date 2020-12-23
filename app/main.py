from fastapi import FastAPI

from model import Employee


def employee_to_dict(employee):

    return {
        "name": employee["name"],
        "email": employee["email"],
        "age": employee["age"],
        "company": employee["company"],
        "join_date": employee["join_date"],
        "job_title": employee["job_title"],
        "gender": employee["gender"],
        "salary": employee["salary"]
    }


app = FastAPI()


@app.get('/api/employees/')
async def get_employees(company: str):

    employees_by_company = []

    try:
        for employee in Employee.objects(company=company):
            employees_by_company.append(employee_to_dict(employee))
    except Exception as e:
        raise ValueError(e)

    return employees_by_company