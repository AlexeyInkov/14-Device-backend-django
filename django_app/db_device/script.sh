#!/bin/bash
python manage.py migrate
python manage.py loaddata fixtures/db_20240918_new_address_region.json
python manage.py collectstatic

