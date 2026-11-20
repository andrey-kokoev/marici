"""Construct directly from six labels and literal row swap. Enumerate only 36 cyclic groups, retain four normalized by the swap, and solve their 3x3 quotient matchings. No completed-matching census or stored paths."""
from itertools import combinations,permutations
P=list(combinations(range(6),2));T=[t for t in combinations(P,3) if len(set(sum(t,())))==6];I=tuple(range(6));r=(1,0,2,3,5,4);comp=lambda a,b:tuple(a[x] for x in b)
def action(p):
 tr=lambda d:tuple(sorted(p[x] for x in d));return [P.index(tr(d)) for d in P]+[15+T.index(tuple(sorted(map(tr,t)))) for t in T]
R=action(r);move=lambda m,H:frozenset(tuple(sorted((H[i],H[j]))) for i,j in m);groups=set()
for hub in range(6):
 v=sorted(set(I)-{hub})
 for tail in permutations(v[1:]):
  ring=(v[0],)+tail;p=list(I)
  for x,y in zip(ring,ring[1:]+ring[:1]):p[x]=y
  q=I;G=[]
  for _ in range(5):G.append(q);q=comp(p,q)
  groups.add(frozenset(G))
compatible=[G for G in groups if {comp(r,comp(g,r)) for g in G}==G];assert len(groups)==36 and len(compatible)==4
flags={(i,j) for i,d in enumerate(P) for j,t in enumerate(T,15) if d in t};final=[]
frame_records=[]
for G in sorted(compatible,key=lambda g:sorted(g)):
 H=action(min(g for g in G if g!=I));bundles=set()
 for flag in flags:
  orbit={flag};e=(H[flag[0]],H[flag[1]])
  while e!=flag:orbit.add(e);e=(H[e[0]],H[e[1]])
  bundles.add(frozenset(orbit))
 constructed=[]
 for triple in combinations(bundles,3):
  m=frozenset().union(*triple)
  if len({i for i,j in m})==len({j for i,j in m})==15:constructed.append(m)
 assert len(constructed)==8
 frame_records.append((G,H,constructed))
 family0=[m for m in constructed if len(m&move(m,R))==10];entry=[m for m in family0 if (0,16) in m];assert len(family0)==4 and len(entry)==1
 m,=entry;hub,=[x for x in I if all(g[x]==x for g in G)];exitmate,=[i for i,j in m if j==29];print('hub',hub,'entry selects one of four family-zero states; exit partner',exitmate)
 if (7,29) in m:final.append(m)
assert len(final)==1;print('direct quotient construction gives one prescribed-row completion')
