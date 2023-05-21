import networkit as nk

reader = nk.graphio.EdgeListReader(',',1,continuous=False)
G = reader.read('/content/person_knows_person_0_0.csv')
nk.graphio.writeGraph(G, 'connections.graph', nk.Format.METIS)
person_knows_person = nk.graphio.readGraph('connections.graph', nk.Format.METIS)
G.indexEdges()

G.numberOfNodes(), G.numberOfEdges()

targetRatio = 0.2

# Initialize the algorithm
lds = nk.sparsification.LocalDegreeScore(G)

# Run
lds.run()

# Get edge scores
ldsScores = lds.scores()
    
# Initialize the algorithm
localDegSparsifier = nk.sparsification.LocalDegreeSparsifier()

# Get sparsified graph
localDegGraph = localDegSparsifier.getSparsifiedGraphOfSize(G, targetRatio)
G.numberOfEdges(), localDegGraph.numberOfEdges()



