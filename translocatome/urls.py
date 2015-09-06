from django.conf.urls import patterns

urlpatterns = patterns('translocatome.views',
                       (r'query-nodes/$', 'query_nodes'),
                       (r'query-interactions/$', 'query_interactions'),
                       )

urlpatterns += patterns('translocatome.rest_api',
                        (r'rest-api/query-nodes/$', 'query_nodes'),
                        (r'rest-api/node(?:/(?P<node_id>[0-9]+))?/$', 'node'),
                        )
