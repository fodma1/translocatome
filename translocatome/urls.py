from django.conf.urls import patterns

urlpatterns = patterns('translocatome.views',
                       (r'^translocatome/api/query-nodes/$', 'query_nodes'),
                       )
