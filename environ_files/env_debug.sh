#!/usr/bin/env bash
# Debuging, i.e. turn off debug,  but use sqlite and debug toolbar

# Django
export DEBUG=off
export FORCE_SQLITE=yes

# Openshift
export SOURCE_REPOSITORY_URL='git@github.com:your-repository.git' # used for build
export CONTEXT_DIR='Set this to the relative path to your project if it is not in the root of your repository' # used for build
export APPLICATION_DOMAIN='vanity url fqdn' # Optional # used by route config

# S2I
export PIP_PROXY='ip:port' # used for build, if needed

# Optional - used by application
export GIT_PROJECT_URL='https://github.com/johnedstone/django-ex-external-db'
export DOCKERFILE_URL='https://github.com/johnedstone/django-ex-external-db/blob/master/Dockerfile'
