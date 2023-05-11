import numpy as np
from scipy.sparse.linalg import svds

def convert_to_adjacency_matrix(df):
    # Create an empty graph
    G = nx.Graph()

    # Add edges from the DataFrame
    edges = df.values.tolist()
    G.add_edges_from(edges)

    # Convert the graph to an adjacency matrix
    adjacency_matrix = nx.adjacency_matrix(G)

    return adjacency_matrix
  
def graph_factorization(adjacency_matrix, num_factors):
    adjacency_matrix = adjacency_matrix.astype(float)  # Convert to floating-point

    # Perform singular value decomposition (SVD) on the adjacency matrix
    U, sigma, V = svds(adjacency_matrix, k=num_factors)

    # Keep only the top 'num_factors' singular values and vectors
    U = U[:, ::-1]
    sigma = np.diag(sigma[::-1])
    V = V[::-1, :]

    # Compute the factorized graph representation
    factorized_graph = np.dot(U, np.sqrt(sigma))

    return factorized_graph


# Relationships matrix as a pandas DataFrame
relationships_matrix = pd.read_csv('/content/person_knows_person_0_0.csv')
relationships_matrix.head()

adjacency_matrix = convert_to_adjacency_matrix(relationships_matrix)

# Compute the graph Laplacian
degree_matrix = np.diag(np.sum(adjacency_matrix, axis=1))
laplacian_matrix = degree_matrix - adjacency_matrix

num_factors = 2  # Number of factors for factorization
factorized_graph = graph_factorization(adjacency_matrix, num_factors)
print("Factorized graph representation:")
print(factorized_graph)


