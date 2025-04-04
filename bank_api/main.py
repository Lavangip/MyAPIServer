from fastapi import FastAPI, HTTPException, Depends  # Importing FastAPI framework and dependencies
from sqlalchemy.orm import Session  # Importing SQLAlchemy session for database interactions
from .database import engine, get_db  # Importing database engine and session dependency
from .models import Base, Bank, Branch  # Importing ORM models for the database tables
from sqlalchemy.future import select  # Importing SQLAlchemy's select function for querying

# Creating an instance of FastAPI
app = FastAPI()

# Ensuring that database tables are created when the application starts
Base.metadata.create_all(bind=engine) 

# Endpoint to retrieve the list of banks
@app.get("/banks", tags=["Banks"]) 
def get_banks(db: Session = Depends(get_db)):  
    result = db.execute(select(Bank)) # Query to fetch all banks from the database 
    return result.scalars().all() 

# Endpoint to retrieve branch details by IFSC code
@app.get("/branches/{ifsc}", tags=["Branches"])
def get_branch(ifsc: str, db: Session = Depends(get_db)): 
    result = db.execute(select(Branch).where(Branch.ifsc == ifsc))  # Query to fetch branch details by IFSC
    branch = result.scalar_one_or_none()  # Fetch the first matching record or return None if not found
    if not branch:  # If no matching branch is found, raise a 404 error
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch 
