#!/bin/sh

# Create a folder
mkdir actions-runner && cd actions-runner
# Download the latest runner package
curl -o actions-runner-linux-x64-2.278.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.278.0/actions-runner-linux-x64-2.278.0.tar.gz
# Extract the installer
tar xzf ./actions-runner-linux-x64-2.278.0.tar.gz

# EDIT - Create the runner and start the configuration experience
./config.sh --url <my-repo-url> --token <my-runner-token>
# Last step, run it!
./run.sh
