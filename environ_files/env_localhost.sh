#!/usr/bin/env bash
# For localhost, default debug is 'on', so using sqlite3, migration is on

# Openshift
export SOURCE_REPOSITORY_URL='git@github.com:your-repository.git'
export CONTEXT_DIR='Set this to the relative path to your project if it is not in the root of your repository'
export PIP_PROXY='ip:port' # used for build, if needed

# Optional - used by application
export GIT_PROJECT_URL='https://github.com/johnedstone/django-ex-external-db'
export DOCKERFILE_URL='https://github.com/johnedstone/django-ex-external-db/blob/master/Dockerfile'
