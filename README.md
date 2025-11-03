# ReviewApp

ReviewApp is a Django project for a community site built around sharing and reviewing projects. Users can browse other members’ work, leave reviews with media attachments, and communicate via direct messages.

---

## ✨ Features

- **Authentication:** Custom login form supporting either username or email, with authenticated-user redirection.  
- **Review posting:** Submit reviews with images or videos, filter by category, sort by popularity or date, and like other users’ posts.  
- **Profiles:** Editable bios and avatars, public profile pages with a list of authored reviews.  
- **Messaging:** Direct messaging between users with rate limiting and read-state tracking.  
- **Audit logging:** Automatic logs for user creation, login activity, review lifecycle events, and admin email notifications when a new account is created.  
- **Security:** Login attempt throttling via django-axes, CSRF/XSS safeguards, Argon2 password hashing, and input sanitization.

---

## 🛠 Tech Stack

- Django 4.2  
- SQLite (default for development)  
- django-axes, django-extensions, Pillow, whitenoise  
- Frontend: Django templates with Bootstrap-based static assets  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+  
- pip and venv available  

### Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser  # create an admin user
   ```

4. Start the server:
   ```bash
   python manage.py runserver
   ```

5. Open the following URL to view the top page and log-in screen:
   ```
   http://127.0.0.1:8000/
   ```

---

## ⚙️ Environment Variables

Configure via `.env` or another method:

```
SECRET_KEY=your-secret-key
DEBUG=True
ADMIN_NOTIFICATION_EMAIL=admin@example.com  # optional
```

If `ADMIN_NOTIFICATION_EMAIL` is set, the app emails the administrator when a new user registers (requires Replit environment tokens when running on Replit).

---

## 🧩 Development Notes

- Static assets: run `python manage.py collectstatic` to populate `staticfiles_build/`.  
- Tests: run `python manage.py test`.  
- Caching: Message rate limiting uses Django’s cache; the default in-memory backend works during development.

---

## 📂 Project Structure (excerpt)

```
reviewpost/        # app code (models, views, forms, etc.)
reviewproject/     # project settings
templates/         # shared templates
static/            # frontend resources
```

---

## ☁️ Deployment

### Current Environment (Replit)

The project is currently hosted on **Replit**, providing a convenient cloud-based development and SSH environment.  
Due to Replit’s free-tier limitations, the app **sleeps when inactive** and may not run 24/7.  
However, all authentication and review features remain fully functional when active.

### Previous Deployment (Vercel)

The project was **previously deployed on Vercel** for front-end testing and demonstration.  
Vercel was used to host the public-facing interface, while Replit now serves as the main full-stack environment for backend development and database operations.

If the Replit instance is inactive, please refer to the GitHub repository or screenshots in the `/screenshots` directory for UI reference.

---

## 🧭 Note for Reviewers (Universities / Recruiters)

This repository demonstrates full-stack Django development, including authentication, CRUD operations, security configurations, and deployment workflows across both **Vercel** and **Replit** environments.  
As Replit projects may sleep during inactivity, please check the source code or screenshots for verification.  
Live demonstration access can be provided upon request.

---

## 🪪 License

Unspecified (you may add MIT, Apache 2.0, or another open license as needed).

---

## 🔍 Key File References

- Login, reviews, messaging views: `reviewpost/views.py:32`, `reviewpost/views.py:55`, `reviewpost/views.py:150`  
- Review/profile/message models: `reviewpost/models.py:11`, `reviewpost/models.py:43`, `reviewpost/models.py:65`  
- Custom authentication backend: `reviewpost/backends.py:7`  
- Rate limiting and sanitization helpers: `reviewpost/decorators.py:8`, `reviewpost/utils.py:9`  
- Audit logging and notification mailer: `reviewpost/signals.py:11`, `reviewpost/email_utils.py:94`  
- Security settings and django-axes setup: `reviewproject/settings.py:33`, `reviewproject/settings.py:144`

---

**Developed by EndoShogo**  
📍 Built for practical Django learning, portfolio use, and university admission demonstration.

---

## 📱 Mobile UI Preview (Smartphone Screens)
<img width="293" alt="image" src="https://github.com/user-attachments/assets/0310870e-c4b0-44e0-98f7-58c0d33f6bb8" />

