import networkit as nk

G = nk.readGraph("../input/jazz.graph", nk.Format.METIS)
G.indexEdges()
G.numberOfNodes(), G.numberOfEdges()

targetRatio = 0.2

# Initialize
res = nk.sparsification.RandomEdgeScore(G)

# Run
res.run()

# Get edge scores
randomEdgeScores = res.scores()
for score in randomEdgeScores[:5]:
    print("{:.3f}".format(score))
    
# Initialize the algorithm
randomEdgeSparsifier = nk.sparsification.RandomEdgeSparsifier()

# Get sparsified graph
randomGraph = randomEdgeSparsifier.getSparsifiedGraphOfSize(G, targetRatio)
G.numberOfEdges(), randomGraph.numberOfEdges()
