#!/bin/sh

WHEEL_DIR="/tmp/wheels"

if [ -z "$(ls $WHEEL_DIR)" ]; then
    echo "Installing packages from network"
    pip3 install --extra-index-url https://int.repositories.cloud.sap/artifactory/api/pypi/naatpypi/simple -r /tmp/requirements.txt
else
    echo "Installing wheels from local files"
    pip3 install --no-index --find-links="${WHEEL_DIR}/" -r /tmp/requirements.txt
fi
