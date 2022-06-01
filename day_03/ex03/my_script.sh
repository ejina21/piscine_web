#!/bin/sh
"/usr/local/bin/python3" -m venv local_lib
source local_lib/bin/activate

python3 -m pip --version

python3 -m pip install --force-reinstall -r requirement.txt
