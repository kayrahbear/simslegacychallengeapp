from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from legacyDB.db import Base


class Trait(Base):
    __tablename__ = "trait"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    description = Column(String(255))
    icon_url = Column(String(50))
    trait_type = Column(String(50))
