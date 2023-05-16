import networkit as nk

G = nk.readGraph("../input/jazz.graph", nk.Format.METIS)
G.indexEdges()
G.numberOfNodes(), G.numberOfEdges()

targetRatio = 0.2

# Initialize the algorithm
lds = nk.sparsification.LocalDegreeScore(G)

# Run
lds.run()

# Get edge scores
ldsScores = lds.scores()
for score in ldsScores[:5]:
    print("{:.3f}".format(score))
    
# Initialize the algorithm
localDegSparsifier = nk.sparsification.LocalDegreeSparsifier()

# Get sparsified graph
localDegGraph = localDegSparsifier.getSparsifiedGraphOfSize(G, targetRatio)
G.numberOfEdges(), localDegGraph.numberOfEdges()



