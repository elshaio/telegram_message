#!/bin/bash
sudo echo Hi!
# Get information from your user
pythonpath="$pwdpath/venv/bin/python"
send_message_path="$pwdpath/send_message.py"
send_file_path="$pwdpath/send_file.py"
# Substitute the information in scripts
sed -i -e "s|{{pythonpath}}|$pythonpath|" send_message.py
sed -i -e "s|{{pythonpath}}|$pythonpath|" send_file.py
# Install the service on your system
sudo ln -s $send_message_path /bin/send_message
sudo ln -s $send_file_path /bin/send_file
