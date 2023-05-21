import networkit as nk

reader = nk.graphio.EdgeListReader(',',1,continuous=False)
G = reader.read('../data/person_knows_person_0_0.csv')
nk.graphio.writeGraph(G, 'connections.graph', nk.Format.METIS)
person_knows_person = nk.graphio.readGraph('connections.graph', nk.Format.METIS)
G.indexEdges()
G.numberOfNodes(), G.numberOfEdges()

targetRatio = 0.2

# Initialize the algorithm
ffs = nk.sparsification.ForestFireScore(G, 0.6, 5.0)

# Run
ffs.run()

# Get edge scores
attributes = ffs.scores()
    
# Initialize the algorithm
fireSparsifier = nk.sparsification.ForestFireSparsifier(0.6, 5.0)

# Get sparsified graph
fireGraph = fireSparsifier.getSparsifiedGraphOfSize(G, targetRatio)
G.numberOfEdges(), fireGraph.numberOfEdges()
    
  
