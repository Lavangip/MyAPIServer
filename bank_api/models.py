from sqlalchemy import Column, Integer, String, ForeignKey  
from sqlalchemy.orm import relationship  
from .database import Base  

# Bank model representing the 'banks' table  
class Bank(Base):  
    __tablename__ = "banks"  
    id = Column(Integer, primary_key=True, index=True)  # Unique bank ID  
    name = Column(String, index=True)  # Bank name  

# Branch model representing the 'branches' table  
class Branch(Base):  
    __tablename__ = "branches"  
    ifsc = Column(String, primary_key=True, index=True)  # Unique IFSC code  
    bank_id = Column(Integer, ForeignKey("banks.id"))  # Foreign key linking to banks  
    branch = Column(String, index=True)  # Branch name  
    address = Column(String)  # Branch address  
    city = Column(String)  # City name  
    district = Column(String)  # District name  
    state = Column(String)  # State name  
    bank_name = Column(String)  # Bank name (stored redundantly)  
