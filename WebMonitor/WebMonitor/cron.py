import requests
import datetime
from monitor.models import WebPage , Failure
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError



def connection(url):
    try:
        r = requests.get(url)
        return [r.status_code, r.text]
    except requests.exceptions.RequestException as err:
        return [404,err]



def request_sender():
    now = datetime.datetime.now()
    webpages = WebPage.objects.all()
    for page in webpages:
        if page.FrequencyOfChecking == "1min":
            CheckWebPage(page)
        elif page.FrequencyOfChecking == "5min" and now.minute % 5 == 0:
            CheckWebPage(page)
        elif page.FrequencyOfChecking == "1hour" and now.minute == 1:
            CheckWebPage(page)
        elif page.FrequencyOfChecking == "1day" and now.minute == 1 and now.hour == 1:
            CheckWebPage(page)

            


def CheckWebPage(page):
    pagestatus = connection(page.link)
    if page.IsWorking and pagestatus[0] != 200:
        page.IsWorking = False
        f = Failure(PageName=page.WebPageName,StatusCode=str(pagestatus[0]),LogErrorMessage=pagestatus[1])
        f.save()
        page.Failures.add(f)
        page.save()
    elif not page.IsWorking and pagestatus[0] == 200:
        page.IsWorking = True
        f = Failure.objects.get(PageName =page.WebPageName,FailureTimeFixed = None)
        f.FailureTimeFixed = datetime.datetime.now()
        f.ResponseDataAfterFix = pagestatus[1]
        f.save()
        page.save()

    
        

