# 🗳️ Flask Voting System

A complete and simple web-based voting system built with **Python Flask**, **SQLite**, and **Bootstrap 5**. It supports secure user login, vote submission, API access, and real-time statistics.

---

## 💻 Database: SQLite + DB Browser

This project uses **SQLite** as the database.

### 💾 How to View the Data with DB Browser for SQLite

#### ✅ Prerequisites

* Install [**DB Browser for SQLite**](https://sqlitebrowser.org/dl/).

#### 📂 Step-by-Step Instructions

1. **Open DB Browser for SQLite**
2. **Click on "Open Database"**, then choose:

   * `voting_system.db` from your project folder
3. **Click on "Browse Data" tab**

   * Use the dropdown to view:

     * `voter`
     * `candidate`
     * `vote`
     * `user`
4. **Click on "Execute SQL" tab** (optional)

   * Run queries like:

```sql
SELECT * FROM voter;
SELECT * FROM candidate;
SELECT * FROM vote;
SELECT * FROM user;
```

5. **Edit or Add Data (if needed)**

   * Use "New Record" or edit cells
   * Click **"Write Changes"** (top-left toolbar)
6. **Save and Close**

   * `File → Write Changes`
   * Then `File → Close Database`

---

## ⚙️ Tech Stack & Requirements

* Python 3.11+
* Flask 3.1.1
* Flask-SQLAlchemy 3.1.1
* Flask-Login
* SQLite (default, easily switchable to PostgreSQL/MySQL)

### Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App (Step-by-Step)

1. **Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/voting-system.git
cd voting-system
```

2. **Create and Activate Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install Requirements**

```bash
pip install -r requirements.txt
```

4. **Run the App**

```bash
python app.py
```

5. **Open in Browser**

```
http://127.0.0.1:5000/
```

---

## 🗒️ Data Models

### Voter

| Field      | Type    | Description       |
| ---------- | ------- | ----------------- |
| id         | Integer | Primary Key       |
| name       | String  | Required          |
| email      | String  | Unique, Required  |
| has\_voted | Boolean | Defaults to False |

### Candidate

| Field | Type    | Description   |
| ----- | ------- | ------------- |
| id    | Integer | Primary Key   |
| name  | String  | Required      |
| party | String  | Optional      |
| votes | Integer | Defaults to 0 |

### Vote

| Field         | Type    | Description              |
| ------------- | ------- | ------------------------ |
| id            | Integer | Primary Key              |
| voter\_id     | Integer | Foreign Key to Voter     |
| candidate\_id | Integer | Foreign Key to Candidate |

### User (Login)

| Field    | Type    | Description              |
| -------- | ------- | ------------------------ |
| id       | Integer | Primary Key              |
| username | String  | Unique, Required         |
| password | String  | Hashed Password (SHA256) |

---

## 🌐 Web Pages

| Route                 | Description                  |
| --------------------- | ---------------------------- |
| `/`                   | Home                         |
| `/register-voter`     | Register a new voter         |
| `/register-candidate` | Register a new candidate     |
| `/vote`               | Submit a vote                |
| `/statistics`         | View voting results          |
| `/login`              | Login with username/password |

---

## 📡 REST API Endpoints (Test via Postman or curl)

### Voters

* `POST /voters` — Register voter
* `GET /voters` — List all voters
* `GET /voters/<id>` — Get voter by ID
* `DELETE /voters/<id>` — Delete voter

### Candidates

* `POST /candidates` — Register candidate
* `GET /candidates` — List all candidates
* `GET /candidates/<id>` — Get candidate by ID
* `DELETE /candidates/<id>` — Delete candidate

### Votes

* `POST /votes` — Cast a vote `{voter_id, candidate_id}`
* `GET /votes` — List all votes
* `GET /votes/statistics` — Stats: totals, percentages

---

## ✅ Business Rules

* Voter **cannot be a candidate** and vice versa
* Each voter **can only vote once**
* After voting, voter's `has_voted = True`
* Candidate's vote count auto-increments
* Passwords are securely hashed

---

## 🔧 Configuration (for DB change)

In `app.py`, change:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting_system.db'
```

Replace with:

* PostgreSQL: `'postgresql://user:pass@localhost/dbname'`
* MySQL: `'mysql+pymysql://user:pass@localhost/dbname'`

---

## 📂 Project Structure

```
.
├── app.py                   # Main Flask app
├── extensions.py            # DB and Login manager
├── models/                  # SQLAlchemy models
│   ├── voter.py
│   ├── candidate.py
│   ├── vote.py
│   └── user.py
├── routes/                  # API Blueprints
│   ├── voter_routes.py
│   ├── candidate_routes.py
│   ├── vote_routes.py
│   └── auth_routes.py
├── templates/               # HTML Templates
├── requirements.txt
└── README.md
```

---

## ☁️ Upload to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/voting-system.git
git push -u origin main
```

Add a screenshot of the `/statistics` page showing voting results (e.g., **5 votes** so far).

---

## 🔐 Enabling the Login System

1. In `app.py`, uncomment:

```python
# login_manager.login_view = 'auth_bp.login'
```

2. This will redirect unauthorized users to `/login`

---

## 🦖 Create Admin User (Manually)

1. **Generate hashed password:**

```bash
python
```

```python
from werkzeug.security import generate_password_hash
print(generate_password_hash("yourpassword"))
```

2. **Insert user into DB:**

```bash
sqlite3 voting_system.db
```

```sql
INSERT INTO user (username, password) VALUES ('admin', 'HASHED_PASSWORD');
.exit
```

Login via `/login`

---

## 🚀 Suggestions for Improvement

* Use JWT for API login
* Add pagination and filtering
* CSV export of vote data
* Admin dashboard with Flask-Admin
* Unit tests with Pytest

---

## 🤔 Summary

✔️ Register voters & candidates
✔️ Secure voting system (1 vote per person)
✔️ Clean REST API & HTML forms
✔️ Login system ready-to-use
✔️ Real-time vote statistics
✔️ DB browser-friendly (SQLite)

---

Made with ❤️ using Flask. Pull requests welcome!
