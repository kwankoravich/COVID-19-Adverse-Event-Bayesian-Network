import networkx as nx

def bayesian_model(bbn)
  n, d = bbn.to_nx_graph()
  nx.draw(n, with_labels=True, labels=d, node_color='r', alpha=1.0)
