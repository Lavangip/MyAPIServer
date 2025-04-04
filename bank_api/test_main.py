import pytest
from fastapi.testclient import TestClient
from bank_api.main import app
from bank_api.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bank_api.models import Base, Bank, Branch

# Set up a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Using SQLite for testing
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create test database tables
Base.metadata.create_all(bind=engine)

@pytest.fixture
def db():
    session = TestingSessionLocal()
    # Clean up the tables before each test to avoid IntegrityError
    session.query(Branch).delete()
    session.query(Bank).delete()
    session.commit()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture
def client(db):
    def override_get_db():
        yield db
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

def test_get_banks(client, db):
    # Add test data
    bank = Bank(id=1, name="Test Bank")
    db.add(bank)
    db.commit()

    response = client.get("/banks")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Test Bank"}]

def test_get_branch(client, db):
    # Add test data
    bank = Bank(id=1, name="Test Bank")
    db.add(bank)
    db.commit()

    branch = Branch(ifsc="TEST1234", bank_id=1, branch="Test Branch", address="123 Test St",
                    city="Test City", district="Test District", state="Test State", bank_name="Test Bank")
    db.add(branch)
    db.commit()

    response = client.get("/branches/TEST1234")
    assert response.status_code == 200
    assert response.json()["ifsc"] == "TEST1234"

def test_get_branch_not_found(client):
    response = client.get("/branches/INVALID123")
    assert response.status_code == 404
    assert response.json()["detail"] == "Branch not found"
