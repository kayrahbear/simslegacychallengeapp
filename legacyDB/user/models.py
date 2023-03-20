from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from legacyDB.db import Base
from . import hashing


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, nullable=False)
    is_superuser = Column(Boolean, nullable=False)

    def __init__(self, name, email, password, created_at, updated_at, *args, **kwargs):
        self.name = name
        self.email = email
        self.password = hashing.get_password_hash(password)
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_active = True
        self.is_superuser = False

    def check_password(self, password):
        return hashing.verify_password(self.password, password)
