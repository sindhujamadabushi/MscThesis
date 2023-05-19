import numpy as np
from karateclub import Node2Vec
import networkx as nx
import pandas as pd

# Relationships matrix as a pandas DataFrame
relationships_matrix = pd.read_csv('../data/person_knows_person_0_0.csv')
relationships_matrix.columns = ['source', 'target']

# Create a graph from the dataframe edge list
graph = nx.from_pandas_edgelist(relationships_matrix, 'source', 'target')
node2vec = Node2Vec(dimensions=50, walk_length=10, walk_number=5, workers=4)
mapping = {node: index for index, node in enumerate(graph.nodes())}
G = nx.relabel_nodes(graph, mapping)

node2vec.fit(G)

# Get the node embeddings
node_embeddings = node2vec.get_embedding()

print(node_embeddings)
