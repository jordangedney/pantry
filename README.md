Pantry
======
1. A recipe suggestion app, currently being developed for web 
2. Installation
3. Set up virtualenvwrapper.
4. Make a new virtualenv
5. pip install -r stable-req.txt
6. python run.py db upgrade
7. python run.py runserver
8. *Bon Appétit!*

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

