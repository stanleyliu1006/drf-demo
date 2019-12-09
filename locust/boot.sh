#!/bin/bash
#pytest --cov-report term --cov=apps &&

MODE="$1"

case $MODE in

  server)
    set -x
    echo Running Load Test...
    sleep 10
    locust -f /src/locust/*locust* --no-web -c 300 -r 20 -t 30s
    ;;

esac
