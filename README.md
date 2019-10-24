# reclama

A bug sprint experiment for events

## install

This assumes that you have already cloned the repo locally and installed `python-virtualenvwrapper`.

On first run you should create a new virtualenv

`mkvirtualenv reclama -a [your_code_path]`

Activate your virtualenv and install requirements:

```
workon reclama
pip install -r requirements/dev.txt
```

Set your environmental variables:

`cp .env-dist .env`

Setup the database:

`./manage.py migrate`

And run the app

`./manage.py runserver`
