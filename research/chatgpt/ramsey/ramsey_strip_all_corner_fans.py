"""Apply exactly the same two-row nonbacktracking conversion at every corner. Test whether this local recipe can be the restriction of a pair/partition bijection."""
from itertools import combinations
from ramsey_strip_alternating_opposites import fs,ed,E,V
from ramsey_strip_prism_proof import P,T
X=sorted(E)
def convert(start):
    arms=[];fan=[]
    for i,f in enumerate(fs):
        u=f[start];end=fs[1-i][u];fan.append(ed(start,u));arms.append({ed(start,u),ed(u,end)})
    arms.append(E-set.union(*arms));idx=lambda edges:tuple(sorted(X.index(e) for e in edges));return P.index(idx(fan)),15+T.index(tuple(sorted(idx(a) for a in arms)))
images={x:convert(x) for x in V}
print(images);assert images[1]==(0,26) and images[4]==(14,26) and images[2][1]==images[3][1] and len({p for p,t in images.values()})==4 and len({t for p,t in images.values()})==2
