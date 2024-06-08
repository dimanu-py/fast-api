from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from todo_list.database import Base


class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    priority = Column(Integer, index=True)
    completed = Column(Boolean, index=False)
    owner = Column(Integer, ForeignKey("users.id"), index=True)
