from sqlalchemy import select

from api_test.models import User


def test_create_user(session):
    user = User(
        username='Alex', email='Alex@teste.com', password='Alex@1234567'
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    my_email = session.scalar(
        select(User).where(User.email == 'Alex@teste.com')
    )

    assert user.id == user.id
    assert my_email.username == 'Alex'
