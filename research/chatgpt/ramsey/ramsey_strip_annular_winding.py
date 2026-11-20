"""Test the seed prism's side-annulus coordinate on the mixed pattern. Only collapse verified pendant excursions; do not invent coordinates for the entire fixed graph. Signed quarter turns lift the cyclic column coordinate to integers. Differences of endpoint-matched paths are winding numbers."""
from ramsey_strip_local_stitch import routes,flips
from ramsey_strip_prism_proof import labels,rep,ext
from collections import Counter
from itertools import groupby
def projection(p):
    walk=[]
    for i,x in enumerate(p):
        if rep(x) in labels:walk.append(labels[rep(x)]);continue
        assert 0<i<len(p)-1 and {labels[rep(p[i-1])],labels[rep(p[i+1])]}==ext[x] and len(ext[x])==1
    return [k for k,_ in groupby(walk)]
def lift(p):
    cols=['abcd'.index(x[0].lower()) for x in projection(p)];ds=[(b-a)%4 for a,b in zip(cols,cols[1:])];assert 2 not in ds;return sum(-1 if v==3 else v for v in ds)
full=Counter();moves=Counter();examples=[]
for (a,b),ok,_ in routes:
    w=lift(a)-lift(b);assert w%4==0;full[ok,w//4]+=1
for _,idx,good,bad,*_ in flips:
    lo,hi=idx[0]-2,idx[-1]+1;a,b=good[lo:hi],bad[lo:hi];assert a[0]==b[0] and a[-1]==b[-1];w=lift(a)-lift(b);assert w%4==0 and lift(good)-lift(bad)==w;moves[w//4]+=1;examples.append((projection(a),projection(b)))
print('relative winding by closure (half A minus half B)',full,'stitch winding good minus bad',moves,'detour types',set((tuple(a),tuple(b)) for a,b in examples));
