#!/bin/bash

sudo apt-get update -y
sudo apt install python3-pip -y
sudo pip install python
sudo python3 -m pip install pip pandas twitter matplotlib -U
nohup sudo python3 news.py &
