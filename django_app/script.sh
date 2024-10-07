#!/bin/bash

./manage.py migrate
./manage.py loaddata fixtures/db_20240918_new_address_region.json
./manage.py collectstatic --noinput

