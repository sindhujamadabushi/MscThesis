import networkit as nk

reader = nk.graphio.EdgeListReader(',',1,continuous=False)
G = reader.read('../data/person_knows_person_0_0.csv')
nk.graphio.writeGraph(G, 'connections.graph', nk.Format.METIS)
person_knows_person = nk.graphio.readGraph('connections.graph', nk.Format.METIS)
G.indexEdges()
G.numberOfNodes(), G.numberOfEdges()

targetRatio = 0.2

# Initialize
tes = nk.sparsification.TriangleEdgeScore(G)

# Run
tes.run()

# Get edge scores
TriangleEdgeScores = tes.scores()
    
# Initialize the algorithm
triangleSparsifier = nk.sparsification.TriangleSparsifier()

# # Get sparsified graph
# randomGraph = randomEdgeSparsifier.getSparsifiedGraphOfSize(G, targetRatio)
