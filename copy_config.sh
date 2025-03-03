#!/bin/bash

CONFIG_PATH="/usr/share/nbfc/configs/"

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <config_file>"
  exit 1
fi

CONFIG_FILE=$1

if [ ! -f "settings/$CONFIG_FILE" ]; then
  echo "Error: File '$CONFIG_FILE' not found!"
  exit 1
fi

echo "Copying 'settings/$CONFIG_FILE' to '$CONFIG_PATH'..."
sudo cp "settings/$CONFIG_FILE" "$CONFIG_PATH"

if [ $? -eq 0 ]; then
  echo "File successfully copied!"
else
  echo "Failed to copy file."
fi