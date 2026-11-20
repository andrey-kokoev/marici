"""Construct all C5-invariant Hall matchings from a 3-by-3 quotient multigraph, with no precomputed matchings or isomorphism data."""
from itertools import combinations
from collections import Counter
P=list(combinations(range(6),2));T=[t for t in combinations(P,3) if len(set(sum(t,())))==6];g=(1,2,3,4,0,5);tr=lambda d:tuple(sorted(g[i] for i in d));act=[P.index(tr(d)) for d in P]+[15+T.index(tuple(sorted(map(tr,t)))) for t in T]
def orbit(x):
 out={x};y=act[x]
 while y!=x:out.add(y);y=act[y]
 return frozenset(out)
L=sorted({orbit(i) for i in range(15)},key=lambda s:min(s));R=sorted({orbit(i) for i in range(15,30)},key=lambda s:min(s));assert len(L)==len(R)==3
flags={(i,j) for i,d in enumerate(P) for j,t in enumerate(T,15) if d in t};bundles=set()
for e in flags:
 o={e};x=(act[e[0]],act[e[1]])
 while x!=e:o.add(x);x=(act[x[0]],act[x[1]])
 assert len(o)==5 and len({i for i,j in o})==len({j for i,j in o})==5;bundles.add(frozenset(o))
B=sorted(bundles,key=lambda s:sorted(s));matrix=[[sum(any(i in u and j in v for i,j in b) for b in B) for v in R] for u in L];outputs=[]
for choices in combinations(B,3):
 m=frozenset().union(*choices)
 if len({i for i,j in m})==len({j for i,j in m})==15:outputs.append(m)
assert len(outputs)==8 and all({(act[i],act[j]) for i,j in m}==m for m in outputs)
hubrow,=[k for k,u in enumerate(L) if all(5 in P[i] for i in u)]
print('quotient edge multiplicities',matrix,'hub row',hubrow,'flag bundles',len(B),'constructed matchings',len(outputs));print('completion counts per hub-edge bundle',[sum(b<=m for m in outputs) for b in B if any(i in L[hubrow] for i,j in b)])
