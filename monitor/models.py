from django.db import models
import datetime
# Create your models here.

class Failure(models.Model):
    PageName = models.TextField(default="This webpage")
    StatusCode = models.TextField(default="This webpage")
    FailureTimeBegin = models.DateTimeField(default=datetime.datetime.now)
    FailureTimeFixed = models.DateTimeField(blank=True,null=True)
    ResponseDataOnFailure = models.TextField(blank=True)
    ResponseDataAfterFix = models.TextField(blank=True)
    LogErrorMessage = models.TextField(blank=True)
    
class WebPage(models.Model):
    description = models.TextField(blank=True)
    link = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    WebPageName = models.TextField(default="Web Page")
    Failures = models.ManyToManyField(Failure, blank=True, related_name='Failures')
    IsWorking = models.BooleanField(default=True)
    FrequencyOfChecking=models.TextField(default="1min")


