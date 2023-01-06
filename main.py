#Created by Jonas Willems.
#CPFED-API: Cheapest Price For Energy Drinks API
#!/usr/bin/env python3


from fastapi import Depends, FastAPI, HTTPException
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
import crud
import models
import schemas
import os
import json

app = FastAPI()

origins = [
    "http://127.0.0.1:8080/",
    "http://127.0.0.1:8000/post/smaak/",
    "http://127.0.0.1:8000/post/verpakking/",
    "http://127.0.0.1:8000/post/merk/",
    "http://127.0.0.1:8000/get/merken/",
    "http://127.0.0.1:8000/get/merk/",
    "http://127.0.0.1:8000/get/smaken/",
    "http://127.0.0.1:8000/get/verpakkingen/",
    "http://127.0.0.1:8000/update/merk/",
    "http://127.0.0.1:8000/delete/merk/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

#Alle POST requests
@app.post("/post/smaak/", response_model=schemas.Smaak)
def add_smaak(Smaak: schemas.SmaakCreate, db: Session = Depends(get_db)):
        return crud.create_smaak(db=db, smaak=Smaak)

@app.post("/post/verpakking/", response_model=schemas.Verpakking)
def add_verpakking(Verpakking: schemas.VerpakkingCreate, db: Session = Depends(get_db)):
        return crud.create_verpakking(db=db, verpakking=Verpakking)
    
@app.post("/post/merk/", response_model=schemas.Merk)
def add_merk(Merk: schemas.MerkCreate, db: Session = Depends(get_db)):
        return crud.create_merk(db=db, merk=Merk)

#Alle GET requests
@app.get("/get/merken/")
def get_merken(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    merken = crud.get_all_merken(db)
    if merken is None:
        raise HTTPException(status_code=404, detail="Geen merken gevonden!")
    return merken    
        
@app.get("/get/merk/{Id}", response_model=schemas.Merk)
def get_merk(Id: int, db: Session = Depends(get_db)):
    db_api = crud.get_merk(db, Id=Id)
    if db_api is None:
        raise HTTPException(status_code=404, detail="Merk niet gevonden!")
    return db_api  

@app.get("/get/smaken/")
def get_smaken(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    smaken = crud.get_all_smaken(db)
    if smaken is None:
        raise HTTPException(status_code=404, detail="Geen smaken gevonden!")
    return smaken  

@app.get("/get/verpakkingen/")
def get_verpakkingen(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    verpakkingen = crud.get_all_verpakkingen(db)
    if verpakkingen is None:
        raise HTTPException(status_code=404, detail="Geen verpakkingen gevonden!")
    return verpakkingen 

#Alle PUT requests
@app.put("/update/merk/{merk_id}", response_model=schemas.Merk)
def update_merk(merk_id: int, merk_update: schemas.MerkUpdate, db: Session = Depends(get_db)):
    return crud.update_merk(db=db, merk_id=merk_id, merk_update=merk_update)


#Alle DELETE requests
@app.delete("/delete/merk/{merk_id}", response_model=schemas.Merk)
def delete_merk(merk_id: int, db: Session = Depends(get_db)):
    return crud.delete_merk(db=db, merk_id=merk_id)