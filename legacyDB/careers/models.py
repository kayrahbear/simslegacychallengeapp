from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from legacyDB.db import Base


class Career(Base):
    __tablename__ = "career"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    description = Column(String(255))

    def __int__(self, name, description):
        self.name = name
        self.description = description


class MemberCareer(Base):
    __tablename__ = "member_career"
    id = Column(Integer, primary_key=True, autoincrement=True)
    member_id = Column(Integer, ForeignKey("legacy_family_member.id"))
    career_id = Column(Integer, ForeignKey("career.id"))
    member = relationship("Member", back_populates="careers")
    career = relationship("Career", back_populates="legacy_family_member")
    level = Column(Integer)

    def __int__(self, member_id, career_id, level):
        self.member_id = member_id
        self.career_id = career_id
        self.level = level
