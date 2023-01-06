#Created by Jonas Willems.
#!/usr/bin/env python3
from sqlalchemy.orm import Session
import models
import schemas



# Alle POST requests
def create_smaak(db: Session, smaak: schemas.SmaakCreate):
    db_item = models.Smaak(**smaak.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
    
def create_verpakking(db: Session, verpakking: schemas.VerpakkingCreate):
    db_item = models.Verpakking(**verpakking.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
    
def create_merk(db: Session, merk: schemas.MerkCreate):
    db_item = models.Merk(**merk.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# Alle GET requests
def get_all_merken(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Merk).offset(skip).limit(limit).all()

def get_merk(db: Session, Id: int):
    return db.query(models.Merk).filter(models.Merk.merkId == Id).first()

def get_all_smaken(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Smaak).offset(skip).limit(limit).all()

def get_all_verpakkingen(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Verpakking).offset(skip).limit(limit).all()
     

#Alle PUT requests
def update_merk(db: Session, merk_id: int, merk_update: schemas.MerkUpdate):
    merk = db.query(models.Merk).filter(models.Merk.merkId == merk_id).first()
    merk.merkNaam = merk_update.merkNaam
    merk.smaakId = merk_update.smaakId
    merk.verpakkingId = merk_update.verpakkingId
    db.commit()
    db.refresh(merk)
    return merk

#Alle DELETE requests
def delete_merk(db: Session, merk_id: int):
    merk = db.query(models.Merk).filter(models.Merk.merkId == merk_id).first()
    db.delete(merk)
    db.commit()
    return merk
