# WebMonitor

Webmonitor is docker image of a Webpage writen in Django for monitoring Webpages

## Installation (windows)

(You need to have a docker-desktop)

In PowerShell

```bash
docker-compose build  
docker-compose up
```
 In CLI 

```bash
docker exec -ti django-webmonitor-container python manage.py crontab add     
```

## Testing 
```bash
docker exec django-webmonitor-container cat /cron/django_cron.log   
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
 
