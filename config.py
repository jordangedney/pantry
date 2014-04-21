import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'pantry.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

PROFILE_IMAGE_PATH = os.path.join(basedir, 'uploads', 'profile_images')
RECIPE_IMAGE_PATH = os.path.join(basedir, 'uploads', 'recipe_images')