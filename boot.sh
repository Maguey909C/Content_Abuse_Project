#!/bin/bash

sudo apt-get update -y
sudo apt install python3-pip python3-tk -y
sudo python3 -m pip install pip pandas scipy matplotlib numpy sklearn Flask -U
nohup sudo python3 r_static.py &
