#!/bin/bash

#install uv
pip install uv

#set up python environment
echo "Setting up python environment"
uv venv
source .venv/bin/activate
uv pip install -r backend/requirements.txt

#install and set up gcloud
echo "Setting up gcloud"
./gcloud_installer.sh

echo "Setup complete"