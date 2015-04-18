from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'translocatome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^accounts/login/$',  'translocatome.views.login'),
    url(r'^accounts/auth/$',  'translocatome.views.auth_view'),
    url(r'^accounts/logout/$', 'translocatome.views.logout'),
    url(r'^accounts/loggedin/$', 'translocatome.views.loggedin'),
    url(r'^accounts/invalid/$', 'translocatome.views.invalid_login'),
    url(r'^accounts/register/$', 'translocatome.views.register_user'),
    url(r'^accounts/register_success/$', 'translocatome.views.register_success'),
]
