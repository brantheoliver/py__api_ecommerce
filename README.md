# How to use

## Clone Repository

```
$ git clone https://github.com/brantheoliver/py__api_ecommerce.git

$ cd py__api_ecommerce
```

## Create Virtualenv and Install Dependencies

with pipenv:

```
$ pip3 install pipenv
$ pipenv --three
$ pipenv sync
```

with vitualenv:

```
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate

$ pip3 install -r requirements.txt
```

# .env file

```
$ touch .env
```

Variables to define

```
export SECRET_KEY=dev
export SQLALCHEMY_DATABASE_URI= connection_string_here
export SQLALCHEMY_TRACK_MODIFICATIONS=False
```

# Initiate Aplication

Database initialization

```
$ flask db init
```

Do migrations

```
$ flask migrate
```

Run application

```
$ flask run
```
