from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime

from todo_list.database import Base


class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    completed = Column(Boolean)
    owner = Column(Integer, ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"))
    due_time = Column(DateTime, nullable=False, default=datetime.utcnow)
