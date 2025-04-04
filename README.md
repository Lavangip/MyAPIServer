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
psql -U postgres -d myapiserverdb -f "path to indian_banks.sql in the indian_banks folder"
```

### 7. Populate the `branches` Table
Here the originally provided branches.csv which was encoded in WIN1252 (Windows-1252) is not used rather the UTF-8 encode version of the same file is used as, PostgreSQL expects UTF-8.
The steps to get UTF-8 encoded csv file.
NOTE: the UTF-8 file is already provided in the repository.
```sh
Get-Content "path to _branches.csv in indian_banks folder" | 
Set-Content -Encoding utf8 "path to _utf8.csv file in indian_banks folder"
```
Populating the 'branches' table
```sh
\copy branches(ifsc, bank_id, branch, address, city, district, state, bank_name) FROM 'path to _utf8.csv file in indian_banks folder' WITH (FORMAT csv, HEADER true, DELIMITER ',');
```

### 8. Run Test Cases
```sh
pytest bank_api/test_main.py
```

### 9. Start the API Server
```sh
uvicorn bank_api.main:app --reload
```


## 📸 Snapshots
![Live API Screenshot](https://github.com/Lavangip/MyAPIServer/blob/main/Workin_Snapshots/Get_branch_info.png)
![Live API Screenshot](https://github.com/Lavangip/MyAPIServer/blob/main/Workin_Snapshots/get_banks.png)
![Live API Screenshot](https://github.com/Lavangip/MyAPIServer/blob/main/Workin_Snapshots/invalid_branch.png)
![Live API Screenshot](https://github.com/Lavangip/MyAPIServer/blob/main/Workin_Snapshots/Testcases.png)

---

