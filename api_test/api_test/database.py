from sqlalchemy import create_engine, select
from api_test.settings import Settings
from sqlalchemy.orm import Session
from api_test.models import User

engine = create_engine(Settings().DATABASE_URL)

def get_session():
    with Session(engine) as session:
        return session
    
        # db_user = session.scalar(
        #     select(User).order_by(
        #         User.id.desc()
        #     )
        # )