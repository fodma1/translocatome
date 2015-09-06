from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from models import Node
from serializers.node_serializers import NodeSerializer

@api_view(['GET'])
def query_nodes(request):
    uni_prot_ac = request.GET.get('uni_prot_ac', '')
    gene_name = request.GET.get('gene_name', '')

    query_params = {}
    if uni_prot_ac and len(uni_prot_ac) > 2:
        query_params['uni_prot_ac__startswith'] = uni_prot_ac

    if gene_name and len(gene_name) > 2:
        query_params['gene_name__startswith'] = gene_name

    node_objects = Node.objects.filter(**query_params)
    nodes = NodeSerializer(node_objects, many=True)

    return Response(nodes)

@api_view(['POST', 'DELETE', 'GET', 'PUT'])
def node(request, node_id=None):
    if request.method == 'POST':
        serializer = NodeSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(str(serializer.errors), status=status.HTTP_400_BAD_REQUEST)

    try:
        node_object = Node.objects.get(id=node_id)
    except (Node.DoesNotExist, ValueError):
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        node_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        serializer = NodeSerializer(node_object)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = NodeSerializer(node_object, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(str(serializer.errors), status=status.HTTP_400_BAD_REQUEST)