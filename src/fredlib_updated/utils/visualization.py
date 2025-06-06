import math
import matplotlib.pyplot as plt
from rdflib.graph import Graph as RDFGraph
import networkx as nx

# ----------------------------------------------------------------------------------------------------------------------
# Visualization Functions
# ----------------------------------------------------------------------------------------------------------------------
def clean_uri(uri):
    # ex: 'http://www.ontologydesignpatterns.org/ont/fred/domain.owl#Motion_directional_1'
    # ex: 'http://www.ontologydesignpatterns.org/ont/framenet/abox/fe/Patient.ingestion'
    split_uri = str(uri).split("/")
    entity_label = split_uri[-1]
    return entity_label.replace("#", ": ")


def get_simplified_nx_graph(g):
    simplified_g = [(clean_uri(triple[0]),
                     clean_uri(triple[2]),
                     clean_uri(triple[1]))
                    for triple in g]

    for triple in simplified_g:
        print(triple)

    G = nx.DiGraph()

    for source, target, relation in simplified_g:
        G.add_edge(source, target, labels=relation)

    return G


def load_rdf_as_nx(rdf:str, format='ttl', simplify=True):
    """
        Load an RDF graph from a string and convert it to a simplified NetworkX graph.
        :param rdf_str: RDF graph in string format
        :param format: Format of the RDF graph (default is 'ttl')
        :return: Simplified NetworkX graph
    """
    # Load RDF graph
    g = RDFGraph()
    g.parse(data=rdf, format='ttl')
    print("rdflib Graph loaded successfully with {} triples".format(len(g)))
    return get_simplified_nx_graph(g) if simplify else g


def plot_graph(G, scaling=50, edge_width=1, k=2):
    # Calculate figure size based on the number of nodes
    num_nodes = len(G.nodes)
    num_edges = len(G.edges)
    graph_size = (num_nodes) + (2 * num_edges)

    figsize = graph_size * scaling / 300
    font_size = 2 + int(math.sqrt(scaling) / 5)

    # Position nodes using the spring layout
    pos = nx.spring_layout(G, seed=42, k=k / num_nodes)
    plt.figure(figsize=(figsize, figsize), dpi=300)

    # Draw nodes with sizes proportional to the length of their text
    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=scaling
    )
    # Draw node labels
    nx.draw_networkx_labels(
        G,
        pos,
        font_size=font_size,
        font_family="sans-serif"
    )


    # Draw edges with widths based on edge weights
    nx.draw_networkx_edges(
        G,
        pos,
        width=edge_width,
        arrows=True,
        arrowstyle='-|>',
        connectionstyle="arc3,rad=0.2"
    )
    # # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, "labels")
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_size=font_size,
        label_pos=0.5,
        rotate=False
    )

    # Customize and show plot
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()

    plt.show()