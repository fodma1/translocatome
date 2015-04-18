#!/bin/bash -ex

root="`dirname \"$0\"`"

export VIRTUAL_ENV="${root}/virtualenv"
[ -d "${VIRTUAL_ENV}/" ] || virtualenv --setuptools --no-site-packages -p python2.7 "${VIRTUAL_ENV}"
. "${VIRTUAL_ENV}/bin/activate"

pip install -r "${root}/requirements.txt"
