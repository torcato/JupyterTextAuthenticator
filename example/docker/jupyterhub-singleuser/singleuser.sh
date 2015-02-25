#!/bin/bash

echo "Creating user $JPY_USER"
useradd -m $JPY_USER

export USER=$JPY_USER
export HOME=/home/$JPY_USER

#chown -R $JPY_USER /home/$JPY_USER
cd /home/$JPY_USER

sudo -E -u $JPY_USER jupyterhub-singleuser \
  --port=8888 \
  --ip=* \
  --user=$JPY_USER \
  --cookie-name=$JPY_COOKIE_NAME \
  --base-url=$JPY_BASE_URL \
  --hub-prefix=$JPY_HUB_PREFIX \
  --hub-api-url=$JPY_HUB_API_URL


