ReviewApp
ReviewApp is a Django project for a community platform focused on sharing and reviewing projects.
Users can browse others’ work, leave detailed reviews with media attachments, and communicate via direct messages.
Features
Authentication – Custom login form supporting either username or email, with authenticated-user redirection.
Review Posting – Submit reviews with images or videos, filter by category, sort by popularity or date, and like other users’ posts.
Profiles – Editable bios and avatars, public profile pages with a list of authored reviews.
Messaging – Direct messaging between users with rate limiting and read-state tracking.
Audit Logging – Automatic logs for user creation, login activity, review lifecycle events, and admin email notifications when a new account is created.
Security – Login attempt throttling via django-axes, CSRF/XSS safeguards, Argon2 password hashing, and input sanitization.
Tech Stack
Backend: Django 4.2
Database: SQLite (default for development)
Libraries: django-axes, django-extensions, Pillow, whitenoise
Frontend: Django templates with Bootstrap-based static assets
Getting Started
Prerequisites
Python 3.10+
pip and venv available
Setup
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Then open http://127.0.0.1:8000/ to view the top page and login screen.
Environment Variables
Set these via .env or another configuration method:
SECRET_KEY=your-secret-key
DEBUG=True
ADMIN_NOTIFICATION_EMAIL=admin@example.com  # optional
If ADMIN_NOTIFICATION_EMAIL is set, the app emails the administrator when a new user registers (requires Replit environment tokens when running on Replit).
Development Notes
Static assets: python manage.py collectstatic → staticfiles_build/
Tests: python manage.py test
Caching: Message rate limiting uses Django’s cache; the default in-memory backend works during development.
Project Structure (excerpt)
reviewpost/        # app code (models, views, forms, etc.)
reviewproject/     # project settings
templates/         # shared templates
static/            # frontend resources
Deployment
Current Environment (Replit)
The project is currently hosted on Replit, which provides an SSH-enabled cloud development environment.
Due to Replit’s free-tier limitations, the app sleeps when inactive and may not run 24/7.
All features remain functional once the app wakes up.
This environment is mainly used for active development and database testing.
Previous Deployment (Vercel)
The app was previously deployed on Vercel, serving the frontend for public demos and performance tests.
Vercel provided a 24/7 live environment during initial development, while Replit now handles full-stack integration and version control through GitHub.
If the Replit app is inactive, please refer to this GitHub repository or the /screenshots folder for previews.
Note for Reviewers
As Replit instances may go to sleep when idle,
please review the source code and screenshots if the live demo is temporarily unavailable.
You may also contact the author for a fresh live link if required.
License
Unspecified (choose one such as MIT or Apache 2.0 based on project requirements).
Author
Developed by tkgggshogo
(Middle school developer aspiring toward global freelance web engineering.)
