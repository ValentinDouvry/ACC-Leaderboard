#!/bin/bash
dir=~/server/results
while inotifywait -e create $dir
do
python3 checkChanges.py
done