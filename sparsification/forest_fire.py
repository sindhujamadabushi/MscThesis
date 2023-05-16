import networkit as nk

G = nk.readGraph("../input/jazz.graph", nk.Format.METIS)
G.indexEdges()
G.numberOfNodes(), G.numberOfEdges()

targetRatio = 0.2

# Initialize the algorithm
ffs = nk.sparsification.ForestFireScore(G, 0.6, 5.0)

# Run
ffs.run()

# Get edge scores
attributes = ffs.scores()
for attribute in attributes[:5]:
    print("{:.3f}".format(attribute))
    
# Initialize the algorithm
fireSparsifier = nk.sparsification.ForestFireSparsifier(0.6, 5.0)

# Get sparsified graph
fireGraph = fireSparsifier.getSparsifiedGraphOfSize(G, targetRatio)
G.numberOfEdges(), fireGraph.numberOfEdges()
    
  
