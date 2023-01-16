import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure

#
# df = pd.read_csv('edge_list.txt', delim_whitespace=True,
#                  header=None, names=['n1', 'n2', 'weight'])
#
# G = nx.from_pandas_dataframe(df, 'n1', 'n2', edge_attr='weight')
options = {
    'node_color': 'blue',
    'node_size': 100,
    'width': 1,
    # 'arrowstyle': 'fancy',
    'arrowsize': 12,
}


def draw_graph(nodes: list[tuple]):
    G = nx.DiGraph()

    edges = nodes
    G.add_weighted_edges_from(edges)

    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos=pos, with_labels=True, **options)

    plt.show()
