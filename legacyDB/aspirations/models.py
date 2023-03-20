# from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
# from sqlalchemy.orm import relationship
# from legacyDB.db import Base
#
#
# class Aspiration(Base):
#     __tablename__ = "aspiration"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50))
#     description = Column(String(255))
#     icon_url = Column(String(50))
#     aspiration_type = Column(String(50))
#
#     def __int__(self, name, description, icon_url, aspiration_type):
#         self.name = name
#         self.description = description
#         self.icon_url = icon_url
#         self.aspiration_type = aspiration_type
