from datetime import date
from http import HTTPStatus

from fastapi.testclient import TestClient

from api_test.app import app


def returning():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    day = str(date.today()).split('-', 2)[2]
    month = str(date.today()).split('-', 2)[1]
    year = str(date.today()).split('-', 2)[0]
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'Month': month,
        'Day': day,
        'Year': year,
    }  # Assert


def test_create_user():
    client = TestClient(app)
    response = client.post(
        '/users/',
        json={
            'usersname': 'test_user',
            'password': '1234567',
            'email': 'user_tester@gmail.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'usersname': 'test_user',
        'email': 'user_tester@gmail.com',
        'id': 1,
    }
