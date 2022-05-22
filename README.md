# WebMonitor

Webmonitor is docker image of a Webpage writen in Django for monitoring Webpages

## Functionality

-Define, edit, delete a monitored website,
-View the failure history for each monitored website
-The ability to use the django admin to manage the data that the application collects.

## Installation (windows)

(You need to have a docker-desktop)

In PowerShell

```bash
docker-compose build  
docker-compose up
```
 In CLI 

```bash
python manage.py crontab add 
python manage.py migrate
python manage.py createsuperuser
```


## Testing 
```bash
docker exec django-webmonitor-container cat /cron/django_cron.log   
```


## DockerHub
https://hub.docker.com/r/ganz7991/webmonitor
## License
[MIT](https://choosealicense.com/licenses/mit/)
 
