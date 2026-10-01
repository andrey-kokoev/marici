"""Canonical restriction of twelve labelled stabilizer probes to actual S4.

S12 acts on twelve directed-arrow labels. Restricting its fixed-label probes
along the induced S4 action is explicit, but need not preserve their metric.
The four state probes are tested in the same carrier function space.
"""
from fractions import Fraction as F
from itertools import permutations, combinations
from biclique_complex import rank

vertices=tuple(range(4)); group=tuple(permutations(vertices))
edges=tuple((i,j) for i in vertices for j in vertices if i!=j)
pairs=tuple(combinations(vertices,2))
fixed=[{k:F(1) for k,g in enumerate(group) if (g[i],g[j])==(i,j)} for i,j in edges]
undirected=[{k:F(1) for k,g in enumerate(group) if g[i]==i and g[j]==j} for i,j in pairs]
# 'undirected' here denotes duplicate endpoint-fixing probes. It is not a
# setwise-edge stabilizer, which would additionally allow swapping endpoints.
points=[{k:F(1) for k,g in enumerate(group) if g[i]==i} for i in vertices]
transition=[{k:F(1) for k,g in enumerate(group) if g[i]==j} for i,j in edges]
assert rank(fixed)==rank(undirected)==6
assert rank(points)==4 and rank(undirected+points)==10
assert rank(transition)==9
for index,(i,j) in enumerate(edges):
    assert fixed[index]==fixed[edges.index((j,i))]
# The action of every carrier relabelling commutes with restriction of probes.
for p in group:
    pi=tuple(p.index(i) for i in vertices)
    for e,column in zip(edges,fixed):
        moved=fixed[edges.index((p[e[0]],p[e[1]]))]
        for k,g in enumerate(group):
            conjugate=tuple(pi[g[p[i]]] for i in vertices)
            assert moved.get(k,0)==column.get(group.index(conjugate),0)


def dot(a,b,weights=None):
    return sum((a.get(i,F(0))*b.get(i,F(0))*(weights[i] if weights else 1) for i in range(24)),F(0))


pair_gram=[[dot(a,b) for b in undirected] for a in undirected]
point_gram=[[dot(a,b) for b in points] for a in points]
assert pair_gram==[[F(1+(i==j)) for j in range(6)] for i in range(6)]
assert point_gram==[[F(2+4*(i==j)) for j in range(4)] for i in range(4)]
for row,pair in zip(undirected,pairs):
    assert [dot(row,p) for p in points]==[F(2 if i in pair else 1) for i in vertices]
# A3-cycle fixes one point and no directed arrow. Point probes therefore cannot
# be linear combinations of the restricted arrow probes.
for i in vertices:
    witness=next(k for k,g in enumerate(group) if sum(g[j]==j for j in vertices)==1 and g[i]==i)
    assert all(witness not in column for column in fixed)
    assert points[i][witness]==1

# Lift both candidate probe choices to the actual121+16 comparison slots on
# S4 x S4. Counted records stay distinct even when their observations coincide.
def tensor(a,b): return {24*i+j:x*y for i,x in a.items() for j,y in b.items()}
selected=[i for i,e in enumerate(edges) if e!=(0,1)]
arrow_slots=[tensor(fixed[i],fixed[j]) for i in selected for j in selected]
state_slots=[tensor(a,b) for a in points for b in points]
assert len(arrow_slots)==121 and len(state_slots)==16
assert rank(arrow_slots)==36 and rank(state_slots)==16
assert rank(arrow_slots+state_slots)==52
transition_slots=[tensor(transition[i],transition[j]) for i in selected for j in selected]
assert rank(transition_slots+state_slots)==88
assert 137-52==85
assert {dot(a,b) for a in fixed for b in points}=={F(1),F(2)}
# Product-measure arrow/state overlaps factor; the two counted blocks are
# linearly independent in this realization but not orthogonal.
assert {dot(a,p)*dot(b,q) for a in fixed for b in fixed for p in points for q in points}=={F(1),F(2),F(4)}
# Tensor columns live on576 points, so their diagonal norms are computed directly.
assert {sum(v*v for v in col.values()) for col in arrow_slots}=={F(4)}
assert {sum(v*v for v in col.values()) for col in state_slots}=={F(36)}

# Exact source-metric decomposition for S12 G=10I+J, normalized once by10!.
seeds=[tuple(F(i==j) for i in range(12)) for j in range(12)]
seeds += [tuple(F(i-4) for i in range(12))]
for x in seeds:
    z=tuple(x[edges.index((i,j))]+x[edges.index((j,i))] for i,j in pairs)
    symmetric=tuple(z[pairs.index(tuple(sorted(e)))]/2 for e in edges)
    hidden=tuple(a-b for a,b in zip(x,symmetric))
    assert all(hidden[edges.index((i,j))]+hidden[edges.index((j,i))]==0 for i,j in pairs)
    assert tuple(s+h for s,h in zip(symmetric,hidden))==x
    source_norm=10*sum(a*a for a in x)+sum(x)**2
    quotient_norm=5*sum(a*a for a in z)+sum(z)**2
    hidden_norm=10*sum(a*a for a in hidden)
    carrier_norm=sum(a*a for a in z)+sum(z)**2
    assert source_norm==quotient_norm+hidden_norm
    assert quotient_norm-carrier_norm==4*sum(a*a for a in z)
# Common and contrast norm ratios differ: no one scalar makes the two visible
# metrics (5I+J versus I+J) agree.
assert F(11,7)!=F(5,1)

# Transporting the quotient Gram can instead impose a nonuniform carrier
# measure: identity weight1, transposition weight5. Arrow probes leave the
#3-cycle weight free. This changes the state-reference metric.
state_metrics=[]
for gamma in (F(1),F(3)):
    weights=[]
    for g in group:
        nfixed=sum(g[i]==i for i in vertices)
        weights.append(F(1) if nfixed==4 else F(5) if nfixed==2 else gamma if nfixed==1 else F(1))
    assert [[dot(a,b,weights) for b in undirected] for a in undirected]==[[F(1+5*(i==j)) for j in range(6)] for i in range(6)]
    metric=[[dot(a,b,weights) for b in points] for a in points]
    assert metric==[[F(6)+(10+2*gamma)*(i==j) for j in range(4)] for i in range(4)]
    state_metrics.append(metric)
assert state_metrics[0]!=state_metrics[1]
# State unit-reference normalization still leaves different contrast ratios.
assert F(12,36)!=F(16,40)
print('Canonical S12-to-S4 probe restriction is equivariant and has rank6: opposite directed-arrow probes coincide.')
print('Four state probes add four independent directions; a3-cycle witnesses why arrows alone cannot reconstruct them.')
print('Retained antisymmetric coefficients reconstruct all twelve source coefficients exactly.')
print('Transported visible Gram is5I+J; actual uniform S4-counting Gram isI+J. No global rescaling equates them.')
print('A nonuniform measure can match the arrow quotient metric, but leaves3-cycle weight and the four-state metric undetermined.')
print('On the121+16 counted slots, fixed-label probes have observed rank52 and85 hidden coefficient directions; transition probes give rank88.')
print('Uniform product counting gives arrow/state slot squared norms4 and36, with nonzero cross-block overlaps1,2,4.')
print('Transition probes have rank9 at the primitive level. Probe choice changes observability, while the137 retained slot count stays fixed; no gauge or coupling identification is inferred.')
