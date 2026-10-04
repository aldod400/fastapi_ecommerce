from sqlalchemy.orm import Session

from app.modules.users.model import User


class UserRepository:
    def __init__(self, db: Session):
        self.session = db

    def get_user_by_email(self, email: str):
        return self.session.query(User).filter(User.email == email).first()

    def create_user(self, user: User):
        self.session.add(user)
        self.session.flush()

        return user
