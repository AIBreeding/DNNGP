#!/bin/bash
eval "$(conda shell.bash hook)"
chmod -R 777 *
if [ "$1" == "L" ]; then
    conda env create -f ./Scripts/environment-Linux.yaml
elif [ "$1" == "I" ]; then
    conda env create -f ./Scripts/environment-intel.yaml
elif [ "$1" == "M" ]; then
    conda env create -f ./Scripts/environment-M1.yaml
else
    echo "Invalid parameter: $1"
    echo "Three parameters are available: L, I, and M"
    echo "L:For Linux   I:For Mac-Intel   M:For Mac-M1"
fi
