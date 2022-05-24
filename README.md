# openclassroom - projet 13 - Site web d'Orange County Lettings

| OC-Lettings |
|:----------:|

_Owner: [Amélie](https://github.com/ameliebnpp)_

## Developpement guide

### General informations

This project is developped with :
- Python(>=3.6, programming language),
- Django(web framework),
- Django REST(REST API framework),
- SQLite3(database)
- CircleCI for continuous integration
- Heroku for deployment
- Sentry for mo,itoring

### Installation

1. Check python/pip version/interpreteur

```bash
which python
python --version
which pip
```

2. Clone the project:

```bash
git clone --recursive git@github.com:amelieBNPP/OC-Lettings.git
```

3. Active the virtual environement:
```bash
python3 -m venv venv
source env/bin/activate
```
*The virtual environement is created only one time, however, it is activate each time we start to develop.*

### Dependencies

Install dependencies :

```bash
pip install -r requirements.txt
```

*Install dependancies each time we develop on this project.*

### Run server

Server can be run using the following commands:
- `cd /path/to/oc-lettings`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`

The API can be tested in local at the following adresse : http://127.0.0.1:8000/

### Admin

Django Administration will be used as a simple frontend : 
- launch server
- run : `http://localhost:8000/admin`
- connect with your supersUser identifiers (user:`admin`, password:`Abc1234!`)

#### DataBase

- `cd /path/to/oc-lettings`
- Open session `sqlite3`
- Connect to database `.open oc-lettings-site.sqlite3`
- Show tables in database `.tables`
- Show columns in profile table, `pragma table_info(oc_lettings_site_profile);`
- Lauch request on profile table, `select user_id, favorite_city from
  oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` for exit sql
### Test

Launch tests
To ensure new features do not add any regression in the code, run the tests with the following commands :

- `cd /path/to/oc-lettings`
- `source venv/bin/activate`
- `pytest`

#### Linting

- `cd /path/to/oc-lettings`
- `source venv/bin/activate`
- `flake8`

#### Docker

##### Run app locally

To run the app locally: 
- `docker build -t oc_lettings .` create image
- `docker run -it -d -p 127.0.0.1:8000:8000 oc_lettings` connect to our container and launch website
(`it` to be interactif, `-d` to be detach(backend), `-p`to define port to use)

The website is now available at the following adress : http://127.0.0.1:8000/
##### Use the main Docker command line

**local**
- `docker images` show image available
- `docker ps` show container available
- `docker stop **CONTAINER ID**` stop container
- `docker exec -ti **CONTAINER ID** sh` to "go into" the docker container
- `docker rmi **IMAGE ID**` remove image
- `docker system prune` clean container, web, images...

**docker hub**
- `docker login -u amefaure` connect to docker
- `docker build -t amefaure/oc_lettings:1.0.0 .` build format to share image
- `docker push amefaure/oc_lettings:1.0.0` share image
- `docker pull amefaure/oc_lettings:1.0.0` download image


### Sources

- tests : https://openclassrooms.com/fr/courses/7155841-testez-votre-projet-python/7414181-implementez-vos-tests-pour-framework-django-avec-pytest-django
- docker : https://www.youtube.com/watch?v=dU5112nqViY
https://www.youtube.com/watch?v=ZgRkGfoy2nE
- Starting with Heroku : https://devcenter.heroku.com/articles/getting-started-with-python
- Starting with CicleCI : https://circleci.com/docs/
- Starting with Sentry : https://sentry.io/for/python/