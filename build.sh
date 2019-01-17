#!/usr/bin/env bash

# Fail on error
set -e
VIRTUAL_ENV_PATH="venv"

function print_help() {
    echo ""
    echo "Utility script for building and publishing package"
    echo ""
    echo "Usage: build command1 [command2] [command3...]"
    echo ""
    echo "Positional arguments"
    echo "command           Command to run"
    echo ""
}

source "${VIRTUAL_ENV_PATH}/bin/activate"

if [[ $# -eq 0 ]]; then
    print_help
    exit 1
fi

while [[ $# -gt 0 ]]
do
    command="$1"
    case $command in
        clean)
            echo "Cleaning build output dirs"
            rm -rf ./build/*
            rm -rf ./dist/*
            rm -rf ./*.egg-info
            ;;
        build)
            echo "Building wheel package"
            python setup.py bdist_wheel
            echo "Building source distribution"
            python setup.py sdist
            ;;
        publish)
            echo "Uploading packages on PyPi"
            twine upload -u logicify dist/*
            ;;
    esac
    shift
done