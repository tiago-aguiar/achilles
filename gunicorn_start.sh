#!/bin/bash

service xinetd stop
service nginx restart

NAME="achilles"
FLASK_DIR=/var/www/achilles/src            	# Flask project directory
SOCKFILE=/var/www/achilles/gunicorn.sock	# we will communicte using this unix socket
USER=root                               	# the user to run as
GROUP=root                                     	# the group to run as
NUM_WORKERS=1                                 	# how many worker processes should Gunicorn spawn
FLASK_WSGI_MODULE=achilles.wsgi              	# WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment

cd $FLASK_DIR
source /var/www/achilles/bin/activate
export PYTHONPATH=$FLASK_DIR:$PYTHONPATH

# Create the run directory if it doesn't exist
# RUNDIR=$(dirname $SOCKFILE)
# test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)

exec /var/www/achilles/bin/gunicorn ${FLASK_WSGI_MODULE}:myapp \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER \
  --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --access-logfile -
