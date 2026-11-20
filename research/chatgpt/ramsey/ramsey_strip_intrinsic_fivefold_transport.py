"""Recover the cyclic groups from matching incidence, then construct anchored transports through group conjugacy. No output-graph isomorphism search."""
from itertools import permutations
from ramsey_strip_fivefold_phase_anchor import long,selected,allms,P,T,moved
I=tuple(range(6));comp=lambda p,q:tuple(p[x] for x in q)
def action(p):
 tr=lambda d:tuple(sorted(p[i] for i in d));return [P.index(tr(d)) for d in P]+[15+T.index(tuple(sorted(map(tr,t)))) for t in T]
groups=set()
for h in range(6):
 v=sorted(set(range(6))-{h})
 for tail in permutations(v[1:]):
  cyc=(v[0],)+tail;p=list(I)
  for x,y in zip(cyc,cyc[1:]+cyc[:1]):p[x]=y
  q=I;G=[]
  for _ in range(5):G.append(q);q=comp(p,q)
  groups.add(frozenset(G))
assert len(groups)==36
def symmetry(m):
 hits=[G for G in groups if all(moved(m,action(p))==m for p in G)];assert len(hits)==1;G,=hits;h,=[x for x in I if all(p[x]==x for p in G)];return G,h
D,dh=symmetry(long)
records=[]
for n,pair in enumerate(selected,1):
 if n==3:continue
 for o,j in enumerate(pair):
  m=allms[j];S,sh=symmetry(m);coherent=[];correct=[]
  for p in permutations(I):
   if p[sh]!=dh or p[3]!=3:continue
   inv=tuple(p.index(x) for x in I)
   if {comp(p,comp(g,inv)) for g in S}!=D:continue
   coherent.append(p)
   if moved(m,action(p))==long:correct.append(p)
  records.append((n,o,m,S,coherent,correct[0]))
  assert len(coherent)==4 and len(correct)==1;print('source',n,o,'cyclic group fixed labels',sh,dh,'group-coherent anchored maps',len(coherent),'matching-compatible',len(correct),'map',correct[0])
