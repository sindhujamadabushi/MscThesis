import networkit as nk

reader = nk.graphio.EdgeListReader(',',1,continuous=False)
G = reader.read('/content/person_knows_person_0_0.csv')
nk.graphio.writeGraph(G, 'connections.graph', nk.Format.METIS)
person_knows_person = nk.graphio.readGraph('connections.graph', nk.Format.METIS)
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


