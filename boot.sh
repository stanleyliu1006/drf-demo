#!/bin/bash
#pytest --cov-report term --cov=apps &&

MODE="$1"

case $MODE in

  server)
    set -x
    echo Running Pact Test ...
    #pytest --pact-broker-url=http://pact-broker.example/ tests/verify_pacts.py
    echo Running Unit Test...
    pytest --cov-report term --cov=apps && (
    echo Upgrading DB...
    until (
      python manage.py makemigrations
      python manage.py migrate
      python manage.py collectstatic --no-input --clear
      ); do echo Retry...; sleep 1; done


    if [ "$DB_INIT_DATA" = "true" ] ; then
        echo Injecting data ...
        ls apps/fixtures/*model*
        python manage.py loaddata apps/fixtures/*model*; fi

    echo Starting API...
    #exec python /src/manage.py runserver 0.0.0.0:8007
    exec gunicorn --workers=3 --bind 0.0.0.0:8007 main.wsgi
    )
    ;;

esac
