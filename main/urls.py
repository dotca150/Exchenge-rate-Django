from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from exchange_rate_django.settings import MEDIA_URL, MEDIA_ROOT
from main.views import *

urlpatterns = [
    path('', main, name='main'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
