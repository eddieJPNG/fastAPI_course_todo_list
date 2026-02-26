from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_must_return_hello_world_and_ok():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}


def test_create_user():
    client = TestClient(app)

    response = client.post(
        '/users/',
        json={
            'username': 'john_doe',
            'email': 'johndoe34@gmail.com',
            'password': '758849',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'john_doe',
        'email': 'johndoe34@gmail.com',
        'id': 1,
    }
