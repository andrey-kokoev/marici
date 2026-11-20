"""Do paired prefix mark words determine a step-eight reservation chain up to swap-preserving relabeling? Canonicalize the oriented prefix AND its ordered chain, with and without distinguished exit. Check earliest distinguishing prefix and minimum queried mark bits."""
from itertools import combinations
from collections import defaultdict
from ramsey_strip_turn_bridge_transport import G
from ramsey_strip_turn_reservation_chain import reservation
from ramsey_strip_anchor_geometry import anchors,rows,r
R=[]
for z in rows:
 for alt in (0,1):
    norm=lambda x:r[x] if alt else x;p=tuple(map(norm,z['path'][:8]));pair,leaf,n,y=anchors(p);chain,_=reservation(p);data=p+tuple(sorted(pair))+tuple(x for e in chain for x in e);can=lambda fixed:min(tuple(g[x] for x in p)+tuple(sorted(g[x] for x in pair))+tuple(g[x] for e in chain for x in e)+((g[z['path'][-1]],) if fixed else ()) for g in G);bits=tuple(i in m for i in range(1,8) for m in z['selected']);R.append((bits,can(False),can(True),n,tuple(sorted(pair))))
def buckets(ids,col):
 d=defaultdict(set)
 for line in R:d[tuple(line[0][i] for i in ids)].add(line[col])
 return d
for i in range(1,8):
 d=buckets(range(2*i),1);print('visits',i,'word count',len(d),'max candidates',max(map(len,d.values())))
for k in range(15):
 hits=[I for I in combinations(range(14),k) if all(len(V)==1 for V in buckets(I,1).values())];
 if hits:break
print('minimum binary tests',hits);groups=buckets(range(14),1);print('prefix classes',len(set(row[1] for row in R)));print('words -> (lengths, distinct literal anchor sets, exit-decorated orbits)');
for w in groups:print(''.join('1' if v else '0' for v in w[::2]),''.join('1' if v else '0' for v in w[1::2]),{line[3] for line in R if line[0]==w},len(buckets(range(14),4)[w]),len(buckets(range(14),2)[w]))
