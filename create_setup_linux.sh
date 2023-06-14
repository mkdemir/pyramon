#!/bin/bash

# Check if python3-venv package is installed
if ! dpkg -s python3-venv >/dev/null 2>&1; then
    echo "Installing python3-venv package..."
    sudo apt install python3-venv
fi

# Check if virtual environment directory exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created."
fi

# Activate virtual environment
source venv/bin/activate

# Ensure virtual environment is activated
if [[ $VIRTUAL_ENV != $PWD'/venv' ]]; then
    echo "
    ---------------------------------------------------------------------------------
        Please activate the virtual environment of this directory to install requirements!
        Current directory: $PWD
    ---------------------------------------------------------------------------------
    "
    exit 1
fi

# Upgrade pip in the virtual environment
python3 -m pip install --upgrade pip

# Install requirements from requirements.txt
python3 -m pip install -r requirements.txt

echo "Requirements installed successfully."

pip freeze
