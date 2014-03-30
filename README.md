Pantry
======
A recipe suggestion app, currently being developed for web 

1. Installation
2. Set up virtualenvwrapper.
3. Make a new virtualenv
4. pip install -r stable-req.txt
5. python run.py db upgrade
6. python run.py runserver
7. *Bon Appétit!*

This app is broken into 4 main parts:
-------------------------------------
- models (db models)
- forms (simple data processing)
- views (hooking the backend to the frontend)
- templates (frontend)
- static (css, libraries, and assets)

Important components
--------------------
- flask-login (simpler logins)
- flask-openid(to incorporate google login)
- flask-script (makes run.py work)
- flask-migrate (adds a simple way to make basic migrations)
- flask-sqlalchemy (models)
- flask-wtforms (forms)

