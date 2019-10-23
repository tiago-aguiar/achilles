ps aux |grep gunicorn |grep achilles | awk '{ print $2 }' |xargs kill -HUP
