# Sticky Notes App — Django Assignment 2

**Course:** Web Engineering  
**University:** National University of Computing and Emerging Sciences (FAST NUCES)

---

## Setup Instructions

Use Python 3.12 or newer. Open Windows CMD in the folder containing manage.py and run:

```bat
py -3.12 -m venv .venv
call .venv\Scripts\activate.bat
python -m pip install -r requirements.txt
for /f %K in ('python -c "import secrets; print(secrets.token_hex(32))"') do set "DJANGO_SECRET_KEY=%K"
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/register/ and create an account. Keep the same DJANGO_SECRET_KEY across sessions to preserve logins. These settings are for local development.

---

## Features
- User Registration with Profile Picture
- Login / Logout
- Create, Edit, Delete Notes
- Colorful Sticky Notes UI
- Each user sees only their own notes



