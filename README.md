# ReviewApp

ReviewApp is a Django project for a community site built around sharing and reviewing projects. Users can browse other members’ work, leave reviews with media attachments, and communicate via direct messages.

## Features

- Authentication: Custom login form supporting either username or email, with authenticated-user redirection.
- Review posting: Submit reviews with images or videos, filter by category, sort by popularity or date, and like other users’ posts.
- Profiles: Editable bios and avatars, public profile pages with a list of authored reviews.
- Messaging: Direct messaging between users with rate limiting and read-state tracking.
- Audit logging: Automatic logs for user creation, login activity, review lifecycle events, and admin email notifications when a new account is created.
- Security: Login attempt throttling via django-axes, CSRF/XSS safeguards, Argon2 password hashing, and input sanitization.

## Tech Stack

- Django 4.2
- SQLite (default for development)
- django-axes, django-extensions, Pillow, whitenoise
- Frontend: Django templates with Bootstrap-based static assets

## Getting Started

### Prerequisites

- Python 3.10+
- pip and venv available

### Setup

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser  # create an admin user
python manage.py runserver
Open http://127.0.0.1:8000/ to view the top page and log-in screen.

Environment Variables
Configure via .env or another method:


SECRET_KEY=your-secret-key
DEBUG=True
ADMIN_NOTIFICATION_EMAIL=admin@example.com  # optional
If ADMIN_NOTIFICATION_EMAIL is set, the app emails the administrator when a new user registers (requires Replit environment tokens when running on Replit).
Development Notes
Static assets: run python manage.py collectstatic to populate staticfiles_build/.
Tests: run python manage.py test.
Caching: Message rate limiting uses Django’s cache; the default in-memory backend works during development.
Project Structure (excerpt)

reviewpost/        # app code (models, views, forms, etc.)
reviewproject/     # project settings
templates/         # shared templates
static/            # frontend resources
License
Unspecified (add one to match your project requirements).



- Login, reviews, messaging views: `reviewpost/views.py:32`, `reviewpost/views.py:55`, `reviewpost/views.py:150`
- Review/profile/message models: `reviewpost/models.py:11`, `reviewpost/models.py:43`, `reviewpost/models.py:65`
- Custom authentication backend: `reviewpost/backends.py:7`
- Rate limiting and sanitization helpers: `reviewpost/decorators.py:8`, `reviewpost/utils.py:9`
- Audit logging and notification mailer: `reviewpost/signals.py:11`, `reviewpost/email_utils.py:94`
- Security settings and django-axes setup: `reviewproject/settings.py:33`, `reviewproject/settings.py:144`

If you’d like me to adjust the tone or add sections (e.g., deployment notes, screenshots), just let me know!
