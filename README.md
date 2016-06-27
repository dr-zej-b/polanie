# costume-inventory

This is a minimalistic app designed to keep track of costume inventory in an amature folk dance group.  The app uses django-heroku template. 

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Installing

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd costume-inventory
$ sudo pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

$ createdb costume-inventory

$ python manage.py migrate
$ python manage.py collectstatic
$ ./run.sh

$ #heroku local
```

Your app should now be running on [localhost:7890](http://localhost:7890/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
