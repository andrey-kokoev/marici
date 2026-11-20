"""Use the row-preserving finish's leftover block {14,23} (tetrahedral edge labels) as Coxeter's distinguished two symbols. Classify each guard, its last partner, and both detours in that fixed cube."""
from ramsey_strip_local_stitch import flips,N,s,t
from itertools import combinations
X=list(combinations(range(1,5),2));D=list(combinations(range(6),2));M=[m for m in combinations(range(15),3) if len(set(sum((D[i] for i in m),())))==6];Z={X.index((1,4)),X.index((2,3))};hub=D.index(tuple(sorted(Z)));assert hub in M[t-15];corners={i for i,d in enumerate(D) if len(set(d)&Z)==1};edges={15+j for j,m in enumerate(M) if len(corners&set(m))==2};kind=lambda x:'corner' if x in corners else 'edge' if x in edges else 'hub' if x==hub else 'axis' if x>=15 else 'opposite-edge join';
for _,idx,good,bad,_,__,iso,p in flips:
 v,=iso;w,=N[v]-{s,t,*p};part=lambda a:[kind(a[i-1]) for i in idx];a,b=good[idx[1]-1],bad[idx[1]-1]; ep=lambda e:N[e]&corners; anti=lambda u:next(y for y in corners if set(D[u])-Z==set(D[y])-Z and y!=u); relation=('antipodal edges' if {anti(y) for y in ep(a)}==ep(b) else 'other edges') if a in edges else ('antipodal corners' if anti(a)==b else 'other corners');
 if idx[0]==2:
    u,z=({next(iter(set(D[i])-Z)) for i in ep(x)} for x in (a,b));assert (u==z or u.isdisjoint(z)) and not ep(a)&ep(b) and relation=='other edges';relation='parallel edges of one face'
 else:assert relation=='antipodal corners'
 print(idx,v,w,kind(v),kind(w),relation);path=(s,)+p+(t,);guard,=(N[path[2]]&N[path[10]] if idx[0]==2 else N[path[1]]&N[path[9]]);assert guard==v and w in bad and w not in good
