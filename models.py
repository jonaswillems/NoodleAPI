#Created by Jonas Willems.
#!/usr/bin/env python3
from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

class Merk(Base):
    __tablename__ = "merken"
    merkId = Column(Integer, primary_key=True)
    merkNaam = Column(String)
    
    smaakId = Column(Integer, ForeignKey('smaken.smaakId'))
    verpakkingId = Column(Integer, ForeignKey('verpakkingen.verpakkingId'))
    
    smaak = relationship("Smaak", back_populates="merk")
    verpakking = relationship("Verpakking", back_populates="merk")
    
    
class Smaak(Base):
    __tablename__ = "smaken"
    smaakId = Column(Integer, primary_key=True)
    smaakNaam = Column(String)
    
    merk = relationship("Merk", back_populates="smaak")


class Verpakking(Base):
    __tablename__ = "verpakkingen"
    verpakkingId = Column(Integer, primary_key=True)
    Type = Column(String)
    
    merk = relationship("Merk", back_populates="verpakking")

