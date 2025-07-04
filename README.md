# 🗳️ Flask Voting System

A complete and simple web-based voting system built with **Python Flask**, **SQLite**, and **Bootstrap 5**. It supports secure user login, vote submission, API access, and real-time statistics.

---

## ⚙️ Tech Stack & Requirements

- Python 3.11+
- Flask 3.1.1
- Flask-SQLAlchemy 3.1.1
- Flask-Login
- SQLite (default, easily switchable to PostgreSQL/MySQL)

### Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App (Step-by-Step)

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/voting-system.git
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

## 🧾 Data Models

### Voter

| Field        | Type    | Description          |
|--------------|---------|----------------------|
| id           | Integer | Primary Key          |
| name         | String  | Required             |
| email        | String  | Unique, Required     |
| has_voted    | Boolean | Defaults to False    |

### Candidate

| Field     | Type    | Description       |
|-----------|---------|-------------------|
| id        | Integer | Primary Key       |
| name      | String  | Required          |
| party     | String  | Optional          |
| votes     | Integer | Defaults to 0     |

### Vote

| Field         | Type    | Description              |
|---------------|---------|--------------------------|
| id            | Integer | Primary Key              |
| voter_id      | Integer | Foreign Key to Voter     |
| candidate_id  | Integer | Foreign Key to Candidate |

### User (Login)

| Field     | Type    | Description              |
|-----------|---------|--------------------------|
| id        | Integer | Primary Key              |
| username  | String  | Unique, Required         |
| password  | String  | Hashed Password (SHA256) |

---

## 🌐 Web Pages

| Route                | Description                      |
|----------------------|----------------------------------|
| `/`                  | Home menu                        |
| `/register-voter`    | Form to register a new voter     |
| `/register-candidate`| Form to register a candidate     |
| `/vote`              | Submit a vote                    |
| `/statistics`        | Voting statistics                |
| `/login`             | Login page (user/password)       |

---
FOR TEST EACH ENDPOINT USE POSTMAN OR A SIMILAR APP

## 📡 REST API Endpoints

### VOTERS

- `POST /voters` — Register a new voter
- `GET /voters` — Get all voters
- `GET /voters/<id>` — Get voter by ID
- `DELETE /voters/<id>` — Delete voter by ID

### CANDIDATES

- `POST /candidates` — Register a new candidate
- `GET /candidates` — Get all candidates
- `GET /candidates/<id>` — Get candidate by ID
- `DELETE /candidates/<id>` — Delete candidate

### VOTES

- `POST /votes` — Cast a vote `{voter_id, candidate_id}`
- `GET /votes` — Get all votes
- `GET /votes/statistics` — Statistics (votes per candidate, percent, etc.)

---

## ✅ Business Rules

- A user **cannot be both a candidate and a voter**
- Each voter can **only vote once**
- Candidate vote count and voter status are updated automatically
- Passwords are stored securely (hashed)

---

## 🔧 Configuration

To switch databases:

```python
# In app.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting_system.db'
```

Replace with:

- PostgreSQL: `'postgresql://user:password@localhost/dbname'`
- MySQL: `'mysql+pymysql://user:password@localhost/dbname'`

---

## 🗂️ Project Structure

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

📸 Add a screenshot of the `/statistics` page in the repo to showcase voting results.
IN THE SCREENSHOT WEE CAN SEE WHAT HERE  WE HAS 5 VOTES. THAT S ARE THE TOTAL OF VOTED TIMES.
HOW I ERASE IT, NOT APPEAR THE TOTAL OF VOTERS, BUT YES IS THE REGISTER OF HOW MUCH VOTES GOES UNTIL THE MOMENT.
---

## 🔐 Enabling the Login Functionality

The login system is already **implemented** using `Flask-Login`, but not fully active. To enable:

1. **Uncomment this line in `app.py`:**

```python
# login_manager.login_view = 'auth_bp.login'
```

2. This ensures unauthorized users are redirected to the login page.

---

## 🧪 Create Admin User for Login (Manual)

You can create a user manually to log in:

### 1. Generate a password hash

```bash
python
```

```python
from werkzeug.security import generate_password_hash
print(generate_password_hash("yourpassword"))
```

Copy the hashed password.

### 2. Open SQLite CLI and insert the user

```bash
sqlite3 voting_system.db
```

```sql
INSERT INTO user (username, password) VALUES ('admin', 'PASTE_HASHED_PASSWORD_HERE');
.exit
```

Now go to `/login` and try logging in with the credentials.

> 💡 Don't forget: The login only protects endpoints that use `@login_required` in `auth_routes.py`. You can add it elsewhere if needed.

---

## 🚀 Suggestions for Improvement

- Use JWT for API login
- Add pagination and search on candidate list
- Export results as CSV
- Create admin dashboard with Flask-Admin
- Add unit tests for endpoints

---

## 🧠 Summary

✔️ Vote registration  
✔️ Candidacy registration  
✔️ One-time voting enforcement  
✔️ REST API + Web Forms  
✔️ Login system (ready to enable)  
✔️ Statistics view  
✔️ Clean code with MVC organization

---

Made with ❤️ using Flask.  
Feel free to contribute with issues or pull requests!
