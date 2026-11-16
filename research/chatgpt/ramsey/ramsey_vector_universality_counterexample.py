"""Exact finite obstruction to the fixed-angle Ramsey carrier.

Requires networkx >= 3. Graph is the 50-vertex Hoffman–Singleton graph.
The proof itself uses integer spectral data, not floating point arithmetic.
"""
import networkx as nx

G = nx.hoffman_singleton_graph()
N = G.number_of_nodes()
E = G.number_of_edges()
deg = {v: G.degree(v) for v in G}
assert N == 50 and E == 175 and set(deg.values()) == {7}
assert sum(nx.triangles(G).values()) == 0

# Strong regularity (50, 7, 0, 1) implies A^2+A-6I=J.
# On vectors orthogonal to the all-ones vector, adjacency eigenvalues
# are roots of lambda^2+lambda-6 = 0, namely 2 and -3.
vs = list(G)
for index, u in enumerate(vs):
    Nu = set(G.neighbors(u))
    for v in vs[index + 1:]:
        common = len(Nu & set(G.neighbors(v)))
        assert common == (0 if G.has_edge(u, v) else 1)

# A-graph is triangle free; complement cliques are B-groups.
B = nx.complement(G)
independent_set, alpha = nx.algorithms.clique.max_weight_clique(B, weight=None)
assert alpha == 15
assert min(dict(B.degree()).values()) == 42  # >= 25 => Hamiltonian by Dirac.
assert any(len(c) == 5 for c in nx.cycle_basis(G))

# If every A-edge had inner product < -1/2 between unit vectors P_i,
# Gram matrix X would satisfy tr(Adj(G) X) < -|E|.
# However Adj(G) >= -3 I as a quadratic form (min eigenvalue -3),
# hence tr(Adj(G) X) >= -3 tr(X) = -3N = -150.
# Contradiction: tr(Adj(G) X) < -175 and >= -150.
assert -E < -3 * N
print(f"N={N}, A edges={E}, degree=7, triangles=0, alpha={alpha}")
print("B degree=42; A contains a 5-cycle and B has a Hamiltonian cycle")
print(f"Gram trace contradiction: tr(A X)<{-E} but tr(A X)>={-3*N}")
print("No -1/2 angular representation exists in any dimension.")
