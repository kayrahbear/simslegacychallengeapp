from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from legacyDB.db import Base


class Family(Base):
    __tablename__ = "legacy_family"
    id = Column(Integer, primary_key=True, autoincrement=True)
    legacy_name = Column(String(50), nullable=False)
    funds = Column(Integer)
    gender_law = Column(Integer, ForeignKey("starting_law.id", ondelete="CASCADE"))
    bloodline_law = Column(Integer, ForeignKey("starting_law.id", ondelete="CASCADE"))
    heir_law = Column(Integer, ForeignKey("starting_law.id", ondelete="CASCADE"))
    species_law = Column(Integer, ForeignKey("starting_law.id", ondelete="CASCADE"))
    exemplar_trait = Column(Integer, ForeignKey("trait.id", ondelete="CASCADE"))
    type_of_start = Column(String(50))
    use_points = Column(Boolean, nullable=False)
    points = Column(Integer)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
