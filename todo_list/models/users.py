from sqlalchemy import Column, Integer, String, Boolean

from todo_list.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    hashed_password = Column(String, index=True)
    is_active = Column(Boolean, default=True)
