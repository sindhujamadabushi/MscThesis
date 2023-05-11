import numpy as np
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPRegressor

def convert_to_adjacency_matrix(df):
    # Create an empty graph
    G = nx.Graph()

    # Add edges from the DataFrame
    edges = df.values.tolist()
    G.add_edges_from(edges)

    # Convert the graph to an adjacency matrix
    adjacency_matrix = nx.adjacency_matrix(G)

    return adjacency_matrix

def perform_sdne(adjacency_matrix, embedding_dim, epochs):
    # Calculate Laplacian matrix
    degree_matrix = np.diag(np.sum(adjacency_matrix, axis=1))
    laplacian_matrix = degree_matrix - adjacency_matrix

    # Define the SDNE model using MLPRegressor
    model = MLPRegressor(hidden_layer_sizes=(embedding_dim,), activation='relu', max_iter=epochs, random_state=0)

    # Create a pipeline with PCA and SDNE model
    pipeline = Pipeline([
        ('pca', PCA(n_components=embedding_dim)),
        ('sdne', model)
    ])

    # Fit the pipeline to the Laplacian matrix
    pipeline.fit(laplacian_matrix, laplacian_matrix)

    # Get the node embeddings
    node_embeddings = pipeline['sdne'].coefs_[0]

    return node_embeddings
  
  # Relationships matrix as a pandas DataFrame
relationships_matrix = pd.read_csv('../data/person_knows_person_0_0.csv')
relationships_matrix.head()

adjacency_matrix = convert_to_adjacency_matrix(relationships_matrix)

# Compute the graph Laplacian
degree_matrix = np.diag(np.sum(adjacency_matrix, axis=1))
laplacian_matrix = degree_matrix - adjacency_matrix

embedding_dim = 128  # Dimensionality of node embeddings
epochs = 50  # Number of training epochs

# Perform SDNE
node_embeddings = perform_sdne(adjacency_matrix, embedding_dim, epochs)

# Print node embeddings
print("Node embeddings:")
print(node_embeddings)
