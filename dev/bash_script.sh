#!/bin/bash

echo "Starting test.py for data_pipeline.py."
python3 test.py

echo "Test Ended"

while true
do
echo "Do you want to execute data_pipeline.py?[y/n]"
read answer
case "$answer" in 
  y|Y ) 
  echo "Starting data_pipeline.py."
  python3 data_pipeline.py
  echo "Ended data_pipeline.py."
  break;;
  n|N ) 
  break;;
  * ) 
  echo "Invalid Input";;
esac
done
echo "Exited Script. Goodbye"
exit