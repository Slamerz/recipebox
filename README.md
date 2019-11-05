Run `pipenv install`
To get into pipenv, `pipenv shell`

Start the server with `python manage.py runserver`

Go to `http://localhost:8000/login` to login. Login button on homepage redirects there when logged out.

Go to `http://localhost:8000/logout` to logout. Logout button on homepage when logged in.

Go to `http://localhost:8000/addauthor` to add a new author. Must be logged in as Admin. Regular users are redirected automatically to homepage.

Go to `http://localhost:8000/addrecipe` to add a new recipe. Must be logged in. Admin user can add recipe to any author. Regular user can only add recipe to themself.

Go to `http://localhost:8000/` for list of recipes.

Go to `http://localhost:8000/recipes/<recipe id>` for a recipe's detail page.

Go to `http://localhost:8000/authors/<author id>` for an author's detail page and list of recipes.

Go to `http://localhost:8000/admin` to add authors and recipes.
login with

Admin user
username: elizabethscheidt
password: asdf

Regular user
username: notadmin
password: notadmin
