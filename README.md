# ReviewApp

**ReviewApp** is a Django project for a community platform focused on sharing and reviewing projects.  
Users can browse others’ work, leave detailed reviews with media attachments, and communicate via direct messages.

---

## Features

- **Authentication** – Custom login form supporting either username or email, with authenticated-user redirection.  
- **Review Posting** – Submit reviews with images or videos, filter by category, sort by popularity or date, and like other users’ posts.  
- **Profiles** – Editable bios and avatars, public profile pages with a list of authored reviews.  
- **Messaging** – Direct messaging between users with rate limiting and read-state tracking.  
- **Audit Logging** – Automatic logs for user creation, login activity, review lifecycle events, and admin email notifications when a new account is created.  
- **Security** – Login attempt throttling via `django-axes`, CSRF/XSS safeguards, Argon2 password hashing, and input sanitization.

---

## Tech Stack

- **Backend:** Django 4.2  
- **Database:** SQLite (default for development)  
- **Libraries:** django-axes, django-extensions, Pillow, whitenoise  
- **Frontend:** Django templates with Bootstrap-based static assets

---

## Getting Started

### Prerequisites
- Python 3.10+  
- `pip` and `venv` available

### Setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
