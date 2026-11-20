"""Test whether taking a half-step of the row exchange names the bit-flip columns. Enumerate every square root on the six tetrahedral edges, independent of strip routes, marks and closure. Compare to explicit within-row / across-row edge transport."""
from itertools import permutations
from ramsey_strip_prism_proof import X,P,T,rep,labels,e,ext
rows=('BRNN','BNRN');index=lambda i,j:X.index(tuple(sorted((i,j))));edgeBR=lambda s:index(s.index('B'),s.index('R'));edgeNN=lambda s:index(*(i for i,c in enumerate(s) if c=='N'));b=list(map(edgeBR,rows));n=list(map(edgeNN,rows));cycle=(b[0],n[0],b[1],n[1]);h=list(range(6))
for i,j in zip(cycle,cycle[1:]+cycle[:1]):h[i]=j
assert [h[h[i]] for i in range(6)]==e

def action(q):
 d=lambda x:tuple(sorted(q[i] for i in x));return [P.index(d(x)) for x in P]+[15+T.index(tuple(sorted(map(d,t)))) for t in T]
roots=[]
for q in permutations(range(6)):
 if [q[q[i]] for i in range(6)]!=e:continue
 m=action(q);cols={name:labels[rep(m[i])] for i,name in labels.items()};flip={'A':'C','C':'A','B':'D','D':'B'};assert all(cols[v][0].upper()==flip[v[0].upper()] for v in cols);roots.append(q)
assert len(roots)==4 and tuple(h) in roots;print('seed root cycle (tetrahedral edges)',[tuple(i+1 for i in X[j]) for j in cycle]);print('all',len(roots),'roots exchange AD and CB columnwise');print('literal root folded action',{v:labels[rep(action(h)[i])] for i,v in labels.items()})
