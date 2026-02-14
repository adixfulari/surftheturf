"""Local settings for development.

This file is intended for local development only. It switches the database to
SQLite so you can run migrations and start the dev server without PostgreSQL.
Do NOT commit production secrets here.
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
