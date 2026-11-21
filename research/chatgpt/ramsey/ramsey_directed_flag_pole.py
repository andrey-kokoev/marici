"""Color-blind bridge hypothesis. A selected incident-face duad at entry gives an edge tangent; an opposite-face duad at exit gives a normal axis. Orient both rays from B into the cube. Entry cross exit is an axial vector; project it onto the B body diagonal. No Ramsey graph colors used."""
from itertools import combinations, permutations
from collections import Counter
from pathlib import Path
import json
D=Path(__file__).parent;E=list(combinations(range(4),2));P=list(combinations(range(6),2));T=[t for t in combinations(P,3) if len(set(sum(t,())))==6];flip=lambda c:tuple(1-x for x in c);dot=lambda a,b:sum(x*y for x,y in zip(a,b));cross=lambda a,b:tuple(a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3] for i in range(3));sub=lambda x,y:tuple(a-b for a,b in zip(x,y));V=[(i>>2,i>>1&1,i&1) for i in range(8)]

def pole(v,entry,exit):
    # Hall IDs: duad -> partition at entry; duad -> partition at exit.
    F=[tuple(x if x==y else None for x,y in zip(v[a],v[b])) for a,b in E];d,t=entry;h,u=exit;assert P[d] in T[t-15] and P[h] in T[u-15];a,b=(F[i] for i in P[d]);c,e=(F[i] for i in P[h]);ea,=[i for i in range(3) if a[i] is b[i] is None];xa,=[i for i in range(3) if c[i]!=e[i] and None not in (c[i],e[i])];assert ea!=xa and all(x in (None,y) for face in (a,b) for x,y in zip(face,v[0]));diag=sub(v[0],flip(v[0]));ray=lambda ax:tuple(-diag[i] if i==ax else 0 for i in range(3));value=dot(cross(ray(ea),ray(xa)),diag);assert abs(value)==1;return (v[0] if value>0 else flip(v[0])),(ea,xa),value

def run():
    flags=[((0,16),(7,29)),((0,17),(4,29))];counts=Counter();canonical=None
    for parity in (0,1):
        for v in permutations([x for x in V if sum(x)%2==parity]):
            b=v[0];p,q=[pole(v,*f) for f in flags];assert p[0]==flip(q[0]);det=dot(sub(v[1],b),cross(sub(v[2],b),sub(v[3],b)));counts[det,p[0]==b]+=1
            if v==((0,0,0),(0,1,1),(1,0,1),(1,1,0)):canonical=dict(poles=[p[0],q[0]],axes=[p[1],q[1]],projections=[p[2],q[2]])
    out=dict(canonical=canonical,counts=[[list(k),n] for k,n in counts.items()]);print(out);return out
if __name__=='__main__':(D/'ramsey_directed_flag_pole.json').write_text(json.dumps(run())+'\n')
