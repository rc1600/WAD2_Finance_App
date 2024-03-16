from django import HttpResponse
import pydot

def create_graph(request):
    sample_data = {'A': {'size': 30, 'color': 'red'},
        'B': {'size': 40, 'color': 'blue'},
        'C': {'size': 20, 'color': 'green'},
        'D': {'size': 10, 'color': 'yellow'}}

    graph = pydot.Dot(graph_type='graph')

    for label, node_data in sample_data.items():
        node = pydot.Node(label, shape='circle', width=str(node_data[10]), style='filled', fillcolor=node_data['color'])
        node.add_node(node)

    image_data = graph.create_png(prog='circo')

    return HttpResponse(image_data, content_type='image/png')
