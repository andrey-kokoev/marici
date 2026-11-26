"""Classify separated-block path corners by all one/two-port tests. Also exhibit a true depth-three split for unrestricted independent first supports."""
from itertools import combinations,product
from collections import defaultdict
import numpy as np,json
from pathlib import Path

def path(n):
    h=(1<<n)-1;a=np.zeros(h+1,dtype=np.int8)
    for p in range(1,h+1):
        b=p&-p;a[p]=max(a[p^b],1+a[(p^b)&~(b<<1)])
    return h,a,np.array([s for s in range(h+1) if not s&(s<<1)])

def corners(n):
    h,a,d=path(n);m=n//2;cs={sum(1<<(i+z) for i,z in zip(t,ds)) for t in combinations(range(n-1),3) if min(t[1]-t[0],t[2]-t[1])>=3 for ds in product(range(2),repeat=3)};groups=defaultdict(list)
    for s in cs:groups[(a[h^(d|s)]<m).tobytes()].append(s)
    refined=[]
    for key,ss in groups.items():
        legal=d[np.frombuffer(key,dtype=bool)];possible=np.zeros(h+1,bool)
        for t in legal:possible[t|legal]=True
        unions=np.flatnonzero(possible & (a[::-1]<m));g=defaultdict(list)
        for s in ss:g[(a[h^(s|unions)]<m-1).tobytes()].append(s)
        refined.extend(g.values())
    return dict(width=n,corners=len(cs),one=len(groups),two=len(refined),multiple=[l for l in refined if len(l)>1])

def witness():
    n=12;h,a,d=path(n);ss=[int(s) for s in d if a[h^s]<=4];
    for I in d:
        if int(I).bit_count()!=4:continue
        yes=next((s for s in ss if s&I),None);no=next((s for s in ss if not s&I),None)
        if yes is None or no is None:continue
        # Split complement of I into three independent neighborhoods. Each pair must hit all six-sets, and the triple must hit all five-sets.
        free=[i for i in range(n) if not I>>i&1];
        for colors in product(range(3),repeat=len(free)):
            t=[sum(1<<i for i,c in zip(free,colors) if c==k) for k in range(3)]
            if any(x&(x<<1) for x in t) or any(a[h^(x|y)]>=6 for x,y in combinations(t,2)):continue
            def valid(s):return all(a[h^int(np.bitwise_or.reduce(u))]+len(u)<8 for r in range(1,5) for u in combinations([s,*t],r))
            if valid(yes) and not valid(no):return dict(width=n,first=[yes,no],later=t,blue_core=int(I),residual_alpha=[int(a[h^s]) for s in (yes,no)])
    raise AssertionError
if __name__=='__main__':
    r=dict(corners=[corners(n) for n in (8,10,12,14,16)],unrestricted=witness());print(r);(Path(__file__).resolve().parents[1]/'results'/'ramsey_cube_third_depth.json').write_text(json.dumps(r,indent=1)+'\n')
