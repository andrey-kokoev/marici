"""One incidence rule for every step-eight choice: remove partners reserved by a tight block of OTHER vertices. Search smallest certificate that rules out all spare neighbors at once. No completion enumeration needed for prediction. Compare with routes only afterwards."""
from itertools import combinations
from collections import Counter
from ramsey_strip_prefix_geometry import N,r,rows
H=Counter();seen={};example=None
for z in rows:
 p=z['path'][:8]
 for alt in (0,1):
    occ=set()
    for i,(a,b) in enumerate(zip(p,p[1:])):occ.update((a,b) if i%2==alt else (r[a],r[b]))
    rem=set(range(30))-occ;v=p[-1] if alt==1 else r[p[-1]];same={i for i in rem if (i<15)==(v<15)}-{v};options=rem&N[v];assert v in rem
    for k in range(8):
        cert=[]
        for U in combinations(sorted(same),k):
            partners=set().union(*(N[x]&rem for x in U));free=options-partners
            if len(partners)==len(U) and len(free)==1:cert.append((U,sorted(partners),next(iter(free))))
        if cert:break
    assert cert and len({w for _,__,w in cert})==1
    U,B,w=cert[0];pred=w if alt==1 else r[w];assert (pred==z['path'][8])==z['closes'];key=tuple(p),alt
    if key not in seen:H[len(options),k]+=1;seen[key]=pred
    if (p[0],z['path'][-1])==(0,29) and not z['closes'] and k>=1 and example is None:example=(p,alt,v,sorted(options),U,B,w,pred,z['path'][8])
print('options / smallest reservation:',H,'example',example);assert len(seen)==64
