from rest_framework import serializers
from monitor.models import WebPage , Failure

class WebPageSerializer(serializers.ModelSerializer):
    CHOICES = (('1min', 'Once per minute'),('5min', 'Every 5 minutes'),('1hour', 'Once per hour'),('1day', 'Once per day'),)
    FrequencyOfChecking = serializers.ChoiceField(choices=CHOICES)
    class Meta:
        model = WebPage
        fields = (
            'id',
            'link' ,
            'WebPageName',
            'description',
            'FrequencyOfChecking'
        )


class FailureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Failure
        fields = (
            'id',
            'PageName' ,
            'StatusCode',
            'FailureTimeBegin' ,
            'FailureTimeFixed',
        )