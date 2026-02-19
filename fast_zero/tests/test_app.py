from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_must_return_hello_world_and_ok():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}


def test_nome_must_be_return_html_and_ok():
    client = TestClient(app)

    response = client.get('/home')

    assert response.status_code == HTTPStatus.OK
    assert response.headers['content-type'] == 'text/html; charset=utf-8'
