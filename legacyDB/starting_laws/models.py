from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from legacyDB.db import Base


class StartingLaw(Base):
    __tablename__ = "starting_law"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    description = Column(String(255))
    law_type = Column(String(50))
