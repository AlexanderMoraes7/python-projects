from datetime import date
from http import HTTPStatus


def test_read_root(client):  # Arrange
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


def test_create_user(client):
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


def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'usersname': 'test_user',
                'email': 'user_tester@gmail.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        'users/1',
        json={
            'password': '123',
            'usersname': 'test_username2',
            'email': 'user_tester@gmail.com',
            'id': 1,
        },
    )
    assert response.json() == {
        'usersname': 'test_username2',
        'email': 'user_tester@gmail.com',
        'id': 1,
    }
