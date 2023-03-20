from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime

from legacyDB.db import Base


class FamilyMember(Base):
    __tablename__ = "legacy_family_member"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    legacy_family = Column(Integer, ForeignKey("legacy_family.id", ondelete="CASCADE"))
    birth_status = Column(String(50))
    gender = Column(String(50))
    age = Column(String(50))
    species = Column(String(50))
    infant_trait = Column(Integer, ForeignKey("trait.id", ondelete="CASCADE"))
    toddler_trait = Column(Integer, ForeignKey("trait.id", ondelete="CASCADE"))
    child_trait = Column(Integer, ForeignKey("trait.id", ondelete="CASCADE"))
    teen_trait = Column(Integer, ForeignKey("trait.id", ondelete="CASCADE"))
    ya_trait = Column(Integer, ForeignKey("trait.id", ondelete="CASCADE"))
    child_aspiration = Column(Integer, ForeignKey("aspiration.id", ondelete="CASCADE"))
    teen_aspiration = Column(Integer, ForeignKey("aspiration.id", ondelete="CASCADE"))
    ya_aspiration = Column(Integer, ForeignKey("aspiration.id", ondelete="CASCADE"))
    adult_aspiration = Column(Integer, ForeignKey("aspiration.id", ondelete="CASCADE"))
    university_attended = Column(String(50))
    university_major = Column(String(50))
    parent_1 = Column(
        Integer, ForeignKey("legacy_family_member.id", ondelete="CASCADE")
    )
    parent_2 = Column(
        Integer, ForeignKey("legacy_family_member.id", ondelete="CASCADE")
    )
    spouse = Column(Integer, ForeignKey("legacy_family_member.id", ondelete="CASCADE"))
    legacy_role = Column(Integer, ForeignKey("legacy_role.id", ondelete="CASCADE"))
    in_household = Column(Boolean, nullable=False)
    is_dead = Column(Boolean, nullable=False)
    death_caused_by = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
