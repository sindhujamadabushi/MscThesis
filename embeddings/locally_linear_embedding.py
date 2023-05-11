import numpy as np
from sklearn.manifold import LocallyLinearEmbedding
import networkx as nx

def convert_to_adjacency_matrix(df):
    # Create an empty graph
    G = nx.Graph()

    # Add edges from the DataFrame
    edges = df.values.tolist()
    G.add_edges_from(edges)

    # Convert the graph to an adjacency matrix
    adjacency_matrix = nx.adjacency_matrix(G)

    return adjacency_matrix
  
# Relationships matrix as a pandas DataFrame
relationships_matrix = pd.read_csv('/content/person_knows_person_0_0.csv')
relationships_matrix.head()

adjacency_matrix = convert_to_adjacency_matrix(relationships_matrix)

# Compute the graph Laplacian - Laplacian matrix captures properties of the graph such as the connectivity and the degree of each node
degree_matrix = np.diag(np.sum(adjacency_matrix, axis=1))
laplacian_matrix = degree_matrix - adjacency_matrix

# Initialize the LLE algorithm
lle = LocallyLinearEmbedding(n_neighbors=3, n_components=2)

# Fit and transform the data
embedding = lle.fit_transform(laplacian_matrix)

print("Embedded Points:")
for i, point in enumerate(embedding):
    print(f"Point {i+1}: {point}")
