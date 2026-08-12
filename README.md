# News — Django News Portal

A multilingual news website built with Django. Users can browse news by category, read full articles with view-count tracking, leave comments, register/manage a profile, and submit contact messages. Superusers get a lightweight CRUD interface for managing news content.

## Features

- **News listing & detail pages** — published news articles with slugs, hit-count tracking (`django-hitcount`), and comments.
- **Category pages** — dedicated views for Local (`Mahalliy`), Sport, Abroad (`Xorij`), Technology (`Texnologiya`), and Auto (`Avto`) news.
- **Search** — keyword search across news titles and body content.
- **Comments** — authenticated users can comment on articles; anonymous users are redirected to log in.
- **Accounts** — registration, login, profile dashboard, and profile editing (user info + avatar) via both function-based views and class-based views.
- **Admin page** — staff-only view listing all superusers.
- **Contact form** — a simple contact page that stores submitted messages.
- **Superuser-only content management** — create, update, and delete news via `OnlyLoggedSuperUser`-protected views.
- **Internationalization** — English and Russian locale files (`django.po` / `django.mo`).
- **Styling** — Bootstrap-based SCSS, Owl Carousel, and custom static assets.

## Tech Stack

- **Backend:** Django
- **Package management:** Pipenv (`Pipfile`, `Pipfile.lock`)
- **Database:** SQLite (`db.sqlite3`)
- **View tracking:** `django-hitcount`
- **Frontend:** Bootstrap (SCSS), Owl Carousel, vanilla JS
- **i18n:** Django's built-in translation framework (`en`, `ru`)

## Project Structure

```
News/
├── accounts/          # User authentication, profiles, registration
├── news/              # Project settings, root URLs, WSGI/ASGI entrypoints
├── news_app/           # Core news app: models, views, forms, admin, permissions
├── templates/          # HTML templates (news, accounts, crud, registration, pages)
├── static/             # CSS/SCSS, JS, images, third-party libraries
├── media/               # Uploaded images (news & user avatars)
├── locale/              # Translation files (en, ru)
├── manage.py
├── Pipfile / Pipfile.lock
└── db.sqlite3
```

### Key apps

**`news_app`**
- `models.py` — `News`, `Category`, `Comment`, `Contact`
- `views.py` — home page, news list/detail, category views, search, contact form, admin page, CRUD views for news
- `custom_permissions.py` — `OnlyLoggedSuperUser` mixin restricting create/update/delete to superusers
- `forms.py` — `ContactForm`, `CommentForm`
- `translation.py` — model translation registration

**`accounts`**
- `models.py` — `Profile` (extends `User`)
- `views.py` — login, registration, dashboard, profile editing (function- and class-based)
- `forms.py` — `LoginForm`, `RegisterForm`, `UserEditForm`, `ProfileEditForm`

## Getting Started

### Prerequisites
- Python 3.x
- [Pipenv](https://pipenv.pypa.io/)

### Installation

```bash
# Clone the repository
git clone https://github.com/davlatbekzoirov/News.git
cd News

# Install dependencies
pipenv install

# Activate the virtual environment
pipenv shell

# Apply database migrations
python manage.py migrate

# Create a superuser (needed for content management)
python manage.py createsuperuser

# Compile translation files
python manage.py compilemessages

# Run the development server
python manage.py runserver
```

The site will be available at `http://127.0.0.1:8000/`.

### Environment

Update `news/settings.py` with your own `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and database settings before deploying to production. Static and media files should be collected and served appropriately (`collectstatic`) in production.

## Usage Notes

- Only superusers can create, edit, or delete news articles (`/news/create/`, `/news/<pk>/edit/`, `/news/<pk>/delete/` — exact URL names depend on `news_app/urls.py`).
- Staff users can access the admin overview page listing all superusers.
- Authenticated users can comment on news articles and edit their profile (including avatar) from the dashboard.
- The search view matches against both the news title and body text (case-insensitive).