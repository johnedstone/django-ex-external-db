#!/usr/bin/env bash
# Production: using external db like oracle

# Openshift build
export SOURCE_REPOSITORY_URL='git@github.com:your-repository.git' # used for build
export CONTEXT_DIR='Set this to the relative path to your project if it is not in the root of your repository' # used for build

# S2I/Openshift build
export PIP_PROXY='ip:port' # used for build
# export APPLICATION_DOMAIN='vanity url fqdn' # Optional # used by route config

# Django
export DEBUG=off
export DATABASE_USER='someuser'
export DATABASE_PASSWORD='yourpasswd'
export DATABASE_NAME='ip:port/instance'
export DJANGO_SECRET_KEY='put-your-django-secret-key-here'
export DB_TABLE_NAME='oracle-table-name' # For production, DB team will supply value
export DISABLE_MIGRATE=yes

# Optional - used by application
export GIT_PROJECT_URL='https://github.com/johnedstone/django-ex-external-db'
export DOCKERFILE_URL='https://github.com/johnedstone/django-ex-external-db/blob/master/Dockerfile'
