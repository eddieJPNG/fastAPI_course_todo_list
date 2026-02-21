from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fast_zero.schemas import UserSchema
from http import HTTPStatus

app = FastAPI()


@app.get('/', status_code=200)
def read_root():
    return {'message': 'Hello, World!'}

@app.post('/users/', status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    return user