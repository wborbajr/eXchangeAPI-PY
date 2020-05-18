#!/bin/sh
#

POETRY_VERSION="1.0.5" 

/usr/local/bin/python -m pip install --upgrade pip 
pip install poetry==${POETRY_VERSION}
make install 
make debug
