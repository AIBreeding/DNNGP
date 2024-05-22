#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate DNNGP3
if [ "$1" == "L" ]; then
    chmod 777 -R * && ./Scripts/DNNGP-Linux
elif [ "$1" == "I" ]; then
    if xattr -d com.apple.quarantine ./Scripts/DNNGP-intel.app; then
        :
    else
        :
    fi
    chmod -R 777 *
    open ./Scripts/DNNGP-intel.app
elif [ "$1" == "M" ]; then
    if xattr -d com.apple.quarantine ./Scripts/M1/DNNGP-M1.app; then
        :
    else
        :
    fi
    chmod -R 777 *
    open ./Scripts/M1/DNNGP-M1.app
else
    echo "Invalid parameter: $1"
    echo "Three parameters are available: L, I, and M"
    echo "L:For Linux   I:For Mac-Intel   M:For Mac-M1"
fi
