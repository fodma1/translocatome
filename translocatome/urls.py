from django.conf.urls import patterns

urlpatterns = patterns('translocatome.views',
                       (r'query-nodes/$', 'query_nodes'),
                       )
