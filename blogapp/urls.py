from django.conf.urls import url, include
import blogapp.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # i have not use the mvc yet here
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',blogapp.views.index),
    # url(r'^admin/', include(admin.site.urls)),
]

