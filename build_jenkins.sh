#!/bin/bash
source /usr/local/bin/virtualenvwrapper.sh
dt="rpn-"$(date '+%d-%m-%Y-%H-%M-%S');
mkvirtualenv "$dt"
workon "$dt"

./build.sh

deactivate
rmvirtualenv "$dt"