from django.conf.urls import patterns

urlpatterns = patterns('translocatome.views',
                       (r'^api/translocatome/api/query-nodes/$', 'query_nodes'),
                       )
