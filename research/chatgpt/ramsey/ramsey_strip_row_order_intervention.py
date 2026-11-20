"""Reverse the literal row order only. Use no closure labels to pick the entry partition: pair the stationary axis BQ with the first row's RQ edge. Compare outcomes in the exceptional family and all shortest substitutions. Check the swap transports paths, incidence matchability and the last-partner choice equivariantly."""
from collections import Counter
from itertools import combinations
from ramsey_strip_seed_shortest_moves import families,full,s,t,paths,matches,target
from ramsey_strip_first_generator import r,N,X,D,M
rows=('BRNN','BNRN');edge=lambda i,j:X.index(tuple(sorted((i,j))));pair=lambda i,j:tuple(sorted((i,j)))
def entry(rows):
 B,=[i for i,ab in enumerate(zip(*rows)) if ab==('B','B')];Q,=[i for i,ab in enumerate(zip(*rows)) if ab==('N','N')];U=rows[0].index('R');selected=pair(edge(B,Q),edge(U,Q));j,=[j for j in N[s] if selected in M[j-15]];return j
f,rev_entry=entry(rows),entry(rows[::-1]);assert f!=rev_entry and r[f]==rev_entry
sw=lambda p:tuple(r[i] for i in p)
def swap(z):
 h,a,b=z;return (sw(h),*sorted((sw(a),sw(b))))
for name,S in [('all',families['seed']),('exceptional',target)]:
 assert {swap(z) for z in S}==S;hist=Counter();concrete={}
 for z in S:
    h,a,b=z;label=lambda p:matches(frozenset(full-set(h)-set(p)));u,v=label(a),label(b);zh=swap(z)[0];assert all(label(p)==matches(frozenset(full-set(zh)-set(sw(p)))) for p in (a,b));hist[h[0],int(u)+int(v)]+=1
    if h[0]==f and u!=v:concrete.setdefault(name,(h,a if u else b,b if u else a))
 print(name,'entry / number of closing alternatives',dict(sorted(hist.items())))
print('row entries',f,rev_entry)
