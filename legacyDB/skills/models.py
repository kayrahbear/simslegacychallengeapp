# from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
# from sqlalchemy.orm import relationship
# from legacyDB.db import Base
#
#
# class Skill(Base):
#     __tablename__ = "skill"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50))
#     description = Column(String(255))
#
#
# class MemberSkill(Base):
#     __tablename__ = "member_skill"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     skill_id = Column(Integer, ForeignKey("skill.id"))
#     member_id = Column(Integer, ForeignKey("member.id"))
#     skill = relationship("Skill", back_populates="member_skills")
#     member = relationship("Member", back_populates="member_skills")
#     level = Column(Integer)
