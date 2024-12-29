#!/bin/bash 

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "This script must be sourced. Run it as: source setup.sh"
    exit 1
fi

if [ -d "venv" ]; then
    echo "Activating python env"
    source venv/bin/activate
else
    echo "Creting new python env"
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
fi

if [ -d "Matrices-master/target" ]; then
    echo "Java matrix checker already compiled" 
else
    echo "Compiling Java matrix checker" 
    cd Matrices-master
    mvn compile
    cd ..
fi