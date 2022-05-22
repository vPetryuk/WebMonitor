from django.urls import path

from .views import AddWebPageView, WebPageDeleteView, WebPageDetailView, WebPageUpdateView, broken_webpages_view, monitor_view

app_name = 'monitor'

urlpatterns = [
    path('', monitor_view, name='main'),
    path('broken-webpages/', broken_webpages_view, name='BrokenWebpages'),
    path('<pk>/delete/', WebPageDeleteView.as_view(), name='webpage-delete'),
    path('<pk>/update/', WebPageUpdateView.as_view(), name='webpage-update'),
    path('<pk>/detail/', WebPageDetailView.as_view(), name='webpage-details'),
    path('add-webpage/', AddWebPageView, name='AddWebPage'),
]
