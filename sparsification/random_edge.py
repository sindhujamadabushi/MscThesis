import networkit as nk

reader = nk.graphio.EdgeListReader(',',1,continuous=False)
G = reader.read('../data/person_knows_person_0_0.csv')
nk.graphio.writeGraph(G, 'connections.graph', nk.Format.METIS)
person_knows_person = nk.graphio.readGraph('connections.graph', nk.Format.METIS)
G.indexEdges()
G.numberOfNodes(), G.numberOfEdges()

targetRatio = 0.2

# Initialize
res = nk.sparsification.RandomEdgeScore(G)

# Run
res.run()

# Get edge scores
randomEdgeScores = res.scores()
    
# Initialize the algorithm
randomEdgeSparsifier = nk.sparsification.RandomEdgeSparsifier()

# Get sparsified graph
randomGraph = randomEdgeSparsifier.getSparsifiedGraphOfSize(G, targetRatio)
G.numberOfEdges(), randomGraph.numberOfEdges()
