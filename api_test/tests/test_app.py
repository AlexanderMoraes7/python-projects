from datetime import date
from http import HTTPStatus
from sqlalchemy.orm import Session
from api_test.settings import Settings
from sqlalchemy import create_engine, select
from api_test.models import User


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
    engine = create_engine(Settings().DATABASE_URL)
    
    with Session(engine) as session:
        db_user = session.scalar(
            select(User).order_by(
                User.id.desc()
            )
        )
    
    response = client.post(
        '/users/',
        json={
            'username': db_user.username,
            'email': db_user.email,
            'password': db_user.password,
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': db_user.username,
        'email': db_user.email,
        'id': db_user,
    }


def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'test_user',
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
            'username': 'test_username2',
            'email': 'user_tester@gmail.com',
            'id': 1,
        },
    )
    assert response.json() == {
        'username': 'test_username2',
        'email': 'user_tester@gmail.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted!'}
