# Django_template

## Requirements
- python3.6
- PostgreSQL

## NPM

This will take care of downloading bower assets as well
```
npm install
```

## Heroku Config

```
heroku config:set SECRET_KEY=(openssl rand 12 -base64)
heroku config:set ALLOWED_HOSTS=$DOMAIN
heroku run --no-tty ./manage.py migrate
heroku run --no-tty ./manage.py createsuperuser
printf 'Site.objects.create(name="django_template", domain="$DOMAIN")\nquit\n' | heroku run ./manage.py shell_plus --ipython
```
