#!/bin/sh

# Download the latest runner package
curl -o /home/runner/actions-runner-linux-x64.tar.gz -L $ACTIONS_INSTALLER_URL

# Extract the installer
tar xzf /home/runner/actions-runner-linux-x64.tar.gz

# Create the runner and start the configuration experience
/home/runner/config.sh --url $GIT_REPO_URL --token $GIT_RUNNER_TOKEN --name runner-$APP_NAME

# Last step, run it!
/home/runner/run.sh
