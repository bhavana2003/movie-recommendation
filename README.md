# movie-recommendation

PROJECT CODE IS IN MAIN BRANCH.

TECH STACK I USED :

FRONTEND:
Html, Css, Js, Bootstrap + jQuery

BACKEND:
Python, SQLite + Django

RECOMMENDATION ENGINE TYPE:
Content-based filtering


# How to run project on localhost

1. Download source code using git clone or download zip
2. run "pip install -r requirements.txt" in terminal (ensure you are in project path)
3. run "python -m venv .venv" to create virtual environment
4. run ".venv\Scripts\activate" to activate virtual environment
5. (skip initially, if error then follow) run "python manage.py makemigrations", "python manage.py migrate" "python manage.py collectstatic" to ensure all database changes are included
6. In your settings.py file, DEBUG = True.
7. run "python manage.py runserver" to open project in localhost.
