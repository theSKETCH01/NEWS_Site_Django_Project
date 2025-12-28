# Django News Site

A login-based Django news website where users can publish and manage their own news posts.

## Features
- Public news reading
- User registration and login
- Manual news publishing
- Fixed categories: Technology, Sports, Business, General News
- Users can edit/delete only their own posts

## Tech Stack
- Python
- Django
- SQLite

## Setup
```bash
python -m venv env
env\Scripts\activate
pip install django
python manage.py migrate
python manage.py runserver
