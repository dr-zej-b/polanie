from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import lendingapp.views

urlpatterns = [
    url(r'^$', lendingapp.views.index, name='index'),
    url(r'^status/', lendingapp.views.status, name='status'),
    url(r'^db', lendingapp.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
