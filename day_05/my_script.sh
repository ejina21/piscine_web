#!/bin/sh
python3 -m venv django_venv

source django_venv/bin/activate

python3 -m pip install --force-reinstall -r requirement.txt

name_bd=djangotraining
user=djangouser
pass=secret

psql postgres <<-EOSQL
    CREATE USER $user WITH PASSWORD '$pass';
    CREATE DATABASE $name_bd;
    GRANT ALL PRIVILEGES ON DATABASE $name_bd TO $user;
EOSQL