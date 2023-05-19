import numpy as np
import pandas as pd
from karateclub.node_embedding.neighbourhood.deepwalk import DeepWalk

# Relationships matrix as a pandas DataFrame
relationships_matrix = pd.read_csv('../data/person_knows_person_0_0.csv')

deepwalk = DeepWalk(dimensions=50, walk_length=10, walk_number=5, workers=4)
mapping = {node: index for index, node in enumerate(graph.nodes())}
G = nx.relabel_nodes(graph, mapping)

node2vec.fit(G)

node_embeddings = node2vec.get_embedding()
