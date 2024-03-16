from django import HttpResponse
import pydot
import io

def create_graph(request):
    sample_data = {'A' : 10, 'B' : 20, 'C' : 30, 'D' : 40}

    graph = pydot.Dot(graph_type='graph')

    for label, sizes in sample_data.items():
        node = pydot.Node(label, shape='circle', width=str(10))
        node.add_node(node)

    image_data = graph.create_png(prog='spendings')

    return HttpResponse(image_data, content_type='image/png')
