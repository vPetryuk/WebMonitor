from django import forms
from .models import WebPage

class WebPageModelForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    link = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    WebPageName = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    CHOICES = (('1min', 'Once per minute'),('5min', 'Every 5 minutes'),('1hour', 'Once per hour'),('1day', 'Once per day'),)
    FrequencyOfChecking = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = WebPage
        fields = ('link' ,'WebPageName','description','FrequencyOfChecking' )

