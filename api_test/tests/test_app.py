from http import HTTPStatus

from fastapi.testclient import TestClient

from api_test.app import app


def returning():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'Day': '09',
        'Month': '03',
        'Year': '2025',
    }  # Assert
