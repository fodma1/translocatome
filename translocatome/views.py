from django.views.decorators.http import require_GET

from utils.http_response import HttpResponseJSON

from models import Node

@require_GET
def query_nodes(request):
    uni_prot_ac = request.GET.get('uni_prot_ac', '')
    gene_name = request.GET.get('gene_name', '')

    query_params = {}
    if uni_prot_ac and len(uni_prot_ac) > 2:
        query_params['uni_prot_ac__startswith'] = uni_prot_ac

    if gene_name and len(gene_name) > 2:
        query_params['gene_name__startswith'] = gene_name

    data = {'nodes': []}
    if query_params:
        data['nodes'] = Node.objects.filter(**query_params).values()

    return HttpResponseJSON(data)
