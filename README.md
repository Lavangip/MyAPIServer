# Bank API Server

## Problem Statement
The goal of this assignment is to create an API server that provides access to bank details and branches using a REST API.

### Requirements:
- Use any Python web framework to develop the API service.
- The database structure and data are provided in the repository.
- Implement REST API endpoints to:
  - Retrieve a list of banks.
  - Fetch branch details for a specific branch.
- Clean and maintainable code will be appreciated.
- Bonus points for including test cases.

---

## ✅ Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/Lavangip/MyAPIServer APIServerProject
```

### 2. Set Up Virtual Environment
```sh
python -m venv venv
```
Activate the virtual environment:
- **Windows**
  ```sh
  venv\Scripts\activate
  ```
- **Linux/macOS**
  ```sh
  source venv/bin/activate
  ```

### 3. Install Required Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL Database
```sh
psql -U postgres
```
Inside the `psql` shell, create the database:
```sql
CREATE DATABASE myapiserverdb;
```

### 5. Configure Environment Variables
- Add the database URL to a `.env` file:
  ```ini
  DATABASE_URL=postgresql://<username>:<password>@localhost/myapiserverdb
  ```

### 6. Initialize Database with Provided Data
```sh
psql -U postgres -d myapiserverdb -f "C:/Users/lavan/OneDrive/Desktop/New folder/APIServerProject/indian_banks/indian_banks.sql"
```

### 7. Populate the `branches` Table
```sh
\copy branches(ifsc, bank_id, branch, address, city, district, state, bank_name) FROM 'C:/Users/lavan/OneDrive/Desktop/New folder/APIServerProject/indian_banks/bank_branches_utf8.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');
```

### 8. Run Test Cases
```sh
pytest bank_api/test_main.py
```

### 9. Start the API Server
```sh
uvicorn bank_api.main:app --reload
```

### 🔗 API Documentation
Once the server is running, access the API documentation at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📸 Snapshots


---

