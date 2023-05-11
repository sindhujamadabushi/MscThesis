import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import SpectralEmbedding
import matplotlib.pyplot as plt

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
relationships_matrix = pd.read_csv('../data/person_knows_person_0_0.csv')
relationships_matrix.head()

adjacency_matrix = convert_to_adjacency_matrix(relationships_matrix)

# Compute the graph Laplacian
degree_matrix = np.diag(np.sum(adjacency_matrix, axis=1))
laplacian_matrix = degree_matrix - adjacency_matrix

# Perform eigen-decomposition of the Laplacian
eigenvalues, eigenvectors = np.linalg.eigh(laplacian_matrix)

# Sort eigenvalues and eigenvectors in ascending order
sorted_indices = np.argsort(eigenvalues)
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

# Select the k eigenvectors corresponding to the smallest eigenvalues
k = 2  # Number of dimensions for visualization
selected_eigenvectors = eigenvectors[:, :k]

# Perform PCA on the selected eigenvectors for dimensionality reduction
pca = PCA(n_components=k)
embedding = pca.fit_transform(selected_eigenvectors)

# Plot the Laplacian Eigenmaps embedding
plt.scatter(embedding[:, 0], embedding[:, 1])
plt.title("Laplacian Eigenmaps")
plt.show()
