#!/bin/bash

abs_path="$( cd "$(dirname "$0")" ; pwd -P )/commands.py"

python3=/home/ryanbaig/.pyenv/versions/3.12.2/envs/.venv/bin/python3
$python3 $abs_path $@