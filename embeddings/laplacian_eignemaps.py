import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import SpectralEmbedding
import matplotlib.pyplot as plt



# Perform eigen-decomposition of the Laplacian
eigenvalues, eigenvectors = np.linalg.eigh(laplacian_matrix)
