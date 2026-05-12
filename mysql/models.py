from mysql.mysql import Base
from sqlalchemy import Column, String, Integer


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, nullable=False)
    category = Column(String(100), index=True, nullable=False)
    time = Column(String(100), nullable=False)