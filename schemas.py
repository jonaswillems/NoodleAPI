#Created by Jonas Willems.
#!/usr/bin/env python3
from pydantic import BaseModel


class MerkBase(BaseModel):
    merkNaam: str
    smaakId: int
    verpakkingId: int

class MerkUpdate(BaseModel):
    merkNaam: str
    smaakId: int
    verpakkingId: int

class MerkCreate(MerkBase):
    pass

class Merk(MerkBase):
    merkId: int

    
    class Config:
        orm_mode = True
        
        
class SmaakBase(BaseModel):
    smaakNaam: str

class SmaakCreate(SmaakBase):
    pass

class Smaak(SmaakBase):
    smaakId: int
    
    class Config:
        orm_mode = True
        
        
class VerpakkingBase(BaseModel):
    Type: str

class VerpakkingCreate(VerpakkingBase):
    pass

class Verpakking(VerpakkingBase):
    verpakkingId: int
    
    class Config:
        orm_mode = True