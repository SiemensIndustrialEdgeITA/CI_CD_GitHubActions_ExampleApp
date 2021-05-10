#!/bin/sh

# Create a folder
mkdir actions-runner && cd actions-runner
# Download the latest runner package
curl -o actions-runner-linux-x64-2.278.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.278.0/actions-runner-linux-x64-2.278.0.tar.gz
# Extract the installer
tar xzf ./actions-runner-linux-x64-2.278.0.tar.gz

# Create the runner and start the configuration experience
./config.sh --url https://github.com/SiemensIndustrialEdgeITA/CI_CD_GitHubActions_ExampleApp --token AIGDZWR3E5B42ECG5ILE4RLATET3G
# Last step, run it!
./run.sh
