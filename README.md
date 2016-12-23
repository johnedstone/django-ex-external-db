### Work in progress - not complete as of 23-Dec-2016 ###

### Demonstrating connecting to an external database with Openshift 3.3
- Based on OpenShift 3.x Django example (see GitHub reference below)
- Python 3.4
- Django 1.10.1
- Openshift 3.3
- Used custom image (see Dockerfile) to include the three oracle-instantclient12 rpms
- Dockerfile tested with both centos/python-34-centos7 and rhscl/python-34-rhel7

### Background

- https://github.com/openshift/django-ex - this is the primary Openshift 3.x Django example
- rpms added to image based on https://code.djangoproject.com/wiki/OracleTestSetup
- custom image contains:
 
    - oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64
    - oracle-instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64
    - oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64

- see also the v1-django-simple branch at https://github.com/johnedstone/django-ex

#### Helpful commands ####

```
# Docker build and push to your local docker registry
docker build -t python34-oracle12:1.0.0 .
docker tag <image id> localhost:5000/custom-images/python34-oracle12:1.0.0
docker tag <image id> localhost:5000/custom-images/python34-oracle12:latest
docker push localhost:5000/custom-images/python34-oracle12:latest
docker push localhost:5000/custom-images/python34-oracle12:1.0.0
docker images -qa | sort |uniq | xargs docker rmi -f

# Create imagestream
oc create -f python_oracle_is.json -n openshift

# New project and new app
oc new-project python34-oracle12

source <environ variables file>

# Sample: some of these environ var may not be used
# This example is for production
oc new-app -f openshift/templates/django.json \
  --param="\
PIP_PROXY=${PIP_PROXY},\
SOURCE_REPOSITORY_URL=${SOURCE_REPOSITORY_URL},\
CONTEXT_DIR=${CONTEXT_DIR},\
APPLICATION_DOMAIN=${APPLICATION_DOMAIN},\
DEBUG=${DEBUG},\
DATABASE_USER=${DATABASE_USER},\
DATABASE_PASSWORD=${DATABASE_PASSWORD},\
DATABASE_NAME=${DATABASE_NAME},\
DISABLE_MIGRATE=${DISABLE_MIGRATE},\
DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY},\
DB_TABLE_NAME=${DB_TABLE_NAME},\
GIT_PROJECT_URL=${GIT_PROJECT_URL},\
DOCKERFILE_URL=${DOCKERFILE_URL}"

# json checker, gives approx line and column
>>> fh = open('django.json')
>>> data = fh.read()
>>> fh.close()
>>> import json
>>> json.loads(data)

# START Docker examples
/opt/s2i build . python34-oracle12:1.0.0 new-app

# Same as runnning env_localhost.sh 
source ../environ_files/env_unset.sh # Nothing else to source as the default is for localhost
docker run --rm -p 8080:8080 -e INTERNAL_IPS=<request IP if not on localhost> --label new-app new-app 

# Not sure where to run this debug, as can not get toolbar to show in production, but here it is
# But this simulates prod w/o an external db
source ../environ_files/env_unset.sh
source ../environ_files/env_debug.sh
docker run --rm -p 8080:8080 -e INTERNAL_IPS=<request IP if not on localhost> -e DEBUG=$DEBUG -e FORCE_SQLITE=${FORCE_SQLITE} --label new-app new-app

# END Docker examples

```
