from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_zero.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', status_code=200)
def read_root():
    return {'message': 'Hello, World!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id


@app.delete('/users/`{users_id}', response_model=Message)
def deleteUser(user_id: int):
    if user_id > len(database) or user_id <= 0:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    del database[user_id - 1]

    return {'message': 'User deleted!'}
