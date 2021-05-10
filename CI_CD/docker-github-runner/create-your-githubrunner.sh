#!/bin/sh
# Configure, deploy and run a GitHub Actions Runner for self-hosted CI/CD Pipelines
#############################################################

# Define a unique name for GitHub Runner
app_name="CICD_Example"

# Copy here properties from New GitHib Actions Runner
actions_installer_url="https://github.com/actions/runner/releases/download/v2.277.1/actions-runner-linux-x64-2.277.1.tar.gz"
git_repo_url="https://github.com/SiemensIndustrialEdgeITA/CI_CD_GitHubActions_ExampleApp"
git_runner_token="AIGDZWWUQYAVMQHZWJSM7W3ATEGXA"

#############################################################
# START
echo "Creating Docker Compose file..."
# CREATE COMPOSE FILE FROM TEMPLATE
cp docker-compose-template.yml docker-compose-$app_name.yml
sed -i 's|#APPNAME|'"$app_name"'|g' ./docker-compose-$app_name.yml
sed -i 's|#ACTIONSINSTALLERURL|'"$actions_installer_url"'|g' ./docker-compose-$app_name.yml
sed -i 's|#GITREPOURL|'"$git_repo_url"'|g' ./docker-compose-$app_name.yml
sed -i 's|#GITRUNNERTOKEN|'"$git_runner_token"'|g' ./docker-compose-$app_name.yml
echo "New Docker Compose file ${app_name} created"

# BUILD AND RUN RUNNER DOCKER INSTANCE
echo "Creating docker GitHub Runner image for app ${app_name}"
docker-compose -f "docker-compose-$app_name.yml" up -d --build

echo "Completed"
#############################################################