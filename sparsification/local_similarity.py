import networkit as nk

G = nk.readGraph("../input/jazz.graph", nk.Format.METIS)
G.indexEdges()
G.numberOfNodes(), G.numberOfEdges()

targetRatio = 0.2

# Compute triangles in G
e_triangles = nk.sparsification.TriangleEdgeScore(G)
e_triangles.run()
triangles = e_triangles.scores()

# Initialize the algorithm
lss = nk.sparsification.LocalSimilarityScore(G, triangles)

# Run
lss.run()

# Get edge scores
scores = lss.scores()
for score in scores[:5]:
    print("{:.3f}".format(score))
    
# Initialize the algorithm
similaritySparsifier = nk.sparsification.LocalSimilaritySparsifier()

# Get sparsified graph
similarityGraph = similaritySparsifier.getSparsifiedGraphOfSize(G, targetRatio)
G.numberOfEdges(), similarityGraph.numberOfEdges()


