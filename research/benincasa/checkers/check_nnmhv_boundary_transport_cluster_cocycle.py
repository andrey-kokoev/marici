#!/usr/bin/env python3
"""Bounded A3 sign-cocycle audit for Nima's boundary-transport request."""
import itertools,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]
# Hexagon diagonals and noncrossing triangulations.
n=6
def canon(a,b): return tuple(sorted((a,b)))
def boundary(d): a,b=d; return (b-a)%n in (1,n-1)
diags=[canon(a,b) for a in range(n) for b in range(a+1,n) if not boundary((a,b))]
def cross(x,y):
 a,b=x;c,d=y
 return len({a,b,c,d})==4 and ((a<c<b<d) or (c<a<d<b))
tris=[frozenset(S) for S in itertools.combinations(diags,n-3) if all(not cross(x,y) for x,y in itertools.combinations(S,2))]
assert len(tris)==14
edges=[]
for i,j in itertools.combinations(range(len(tris)),2):
 if len(tris[i]^tris[j])==2: edges.append((i,j))
assert len(edges)==21
# Every fixed diagonal gives one rank-two face (3 squares, 6 pentagons).
faces=[]
for d in diags:
 V={i for i,T in enumerate(tris) if d in T}; E=[e for e in edges if e[0] in V and e[1] in V]
 assert len(E)==len(V) and len(V) in (4,5)
 faces.append({'diagonal':d,'vertices':V,'edges':E,'size':len(V)})
assert [f['size'] for f in faces].count(4)==3 and [f['size'] for f in faces].count(5)==6
# The source packet fixes one negative exchange witness, but no mutation-edge transport.
e0=edges[0]
# Completion A is a vertex-gauge coboundary with g(e0[0])=-1 and all others +1.
g=[1]*len(tris);g[e0[0]]=-1
A={e:g[e[0]]*g[e[1]] for e in edges}
assert A[e0]==-1
# Completion B puts -1 only on that edge.
B={e:(-1 if e==e0 else 1) for e in edges}
def residuals(C): return [__import__('math').prod(C[e] for e in f['edges']) for f in faces]
rA=residuals(A);rB=residuals(B)
assert set(rA)=={1} and -1 in rB
src=json.loads((R/'nima/results/nnmhv-cluster-exchange-weight-gate.json').read_text())
out={'schema':'marici.benincasa.nnmhv-boundary-transport-cluster-cocycle.v1','coefficient_object':'candidate Z2 sign line on oriented mutation edges; reversal has the same sign','coboundary_operator':'for each square or pentagon face F, delta(s)(F)=product of edge signs around boundary(F)','complex':{'type':'A3 associahedron','vertices':14,'mutation_edges':21,'square_faces':3,'pentagon_faces':6},'source_constraints':{'known_negative_exchange_residual':src['with_boundary_update']['R'],'known_local_sign':-1,'global_edge_transport_maps_materialized':False},'exact_completions':[{'name':'closed_vertex_gauge_completion','designated_sign':A[e0],'square_pentagon_residuals':rA,'path_independent':True,'class':'trivial coboundary'},{'name':'single_edge_completion','designated_sign':B[e0],'square_pentagon_residuals':rB,'path_independent':False,'class':'obstructed cocycle'}],'topological_note':'The associahedron is a ball, hence any closed Z2 rank-one local system is cohomologically trivial; a nontrivial H1 class cannot be inferred on the full complex.','positroid_boundary':'Cluster/positroid incidence supplies the square-pentagon carrier only. The physical kernel weights are not positive cluster coordinates, so incidence does not supply their transport coefficients.','disposition':'missing source map','reason':'The one negative Ptolemy/minor witness is compatible with both a closed trivial sign cocycle and an obstructed assignment. No source packet gives mutation-edge coefficient transport, so exact face holonomies of the physical weights are underdetermined.','required_reopening':'materialize the coefficient ratio or signed linear map for every physical boundary replacement edge, then evaluate the displayed face coboundary','passed':True}
P=R/'benincasa/results/nnmhv_boundary_transport_cluster_cocycle.json';P.write_text(json.dumps(out,indent=2,default=lambda x:sorted(x) if isinstance(x,set) else x)+'\n');print(json.dumps(out,indent=2))
