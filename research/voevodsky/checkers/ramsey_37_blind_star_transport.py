"""Blind incidence search in the 191 labelled catalogue records. Recover a full permutation from both star families: each middle site is determined by its two containing stars. Test red adjacency on all pairs and both composite routes on every vertex."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
H=Path(__file__).resolve().parents[1];D=H/'results';cat=H.parent/'chatgpt/ramsey/pauli-realization-catalogues/r37_22.g6';U=set(range(22))

def test(E):
 N=[{y for y in U if tuple(sorted((x,y))) in E} for x in range(22)];counts=Counter();cert=None
 for p,q in sorted(E):
    X=N[p]-{q};Y=N[q]-{p};M=U-{p,q}-X-Y
    if len(X)!=5 or len(Y)!=5 or len(M)!=10:continue
    F={x:N[x]&M for x in X|Y}
    def stars(X):return all(len(F[x])==4 for x in X) and all(len(F[x]&F[y])==1 for x,y in combinations(X,2)) and all(sum(v in F[x] for x in X)==2 for v in M)
    if not(stars(X) and stars(Y)):continue
    counts['paired']+=1
    def mate(k):
        C={x:[y for y in Y if len(F[x]&F[y])==k] for x in X};return {x:l[0] for x,l in C.items()} if all(len(l)==1 for l in C.values()) and len({l[0] for l in C.values()})==5 else None
    m=mate(0);one=mate(1)
    if not m or not one:continue
    inv={y:x for x,y in m.items()};L=[min(X)]
    for _ in range(4):L.append(inv[one[L[-1]]]);
    if len(set(L))!=5 or inv[one[L[-1]]]!=L[0]:continue
    counts['opposite_clocks']+=1
    def lift(f):
        for x,y in combinations(X,2):
            v,=F[x]&F[y];z,=F[f[x]]&F[f[y]];f[v]=z
        return f if len(set(f.values()))==22 and all(tuple(sorted((f[u],f[v]))) in E for u,v in E) else None
    r=lift({p:p,q:q,**{z:w for i,x in enumerate(L) for z,w in [(x,L[(i+1)%5]),(m[x],m[L[(i+1)%5]])]}})
    if not r:continue
    counts['rotations']+=1
    for h in range(5):
        s=lift({p:q,q:p,**{z:w for i,x in enumerate(L) for z,w in [(x,m[L[(h-i)%5]]),(m[x],L[(h-i)%5]) ]}})
        if s and all(s[s[v]]==v and s[r[s[r[v]]]]==v for v in U):
            counts['coherent']+=1
            if cert is None:cert=dict(poles=[p,q],first_clock=L,second_matched=[m[x] for x in L],rotation=[r[i] for i in range(22)],reflection=[s[i] for i in range(22)])
            break
 return dict(counts),cert
out=[]
for i,g in enumerate(cat.read_text().splitlines(),1):
 assert ord(g[0])-63==22;bits=''.join(f'{ord(ch)-63:06b}' for ch in g[1:]);E={(a,b) for b in U for a in range(b) if bits[b*(b-1)//2+a]=='1'};cnt,cert=test(E);out.append(dict(record=i,counts=cnt,certificate=cert))
w=json.loads((D/'ramsey_37_dual_stars.json').read_text());assert test(set(map(tuple,w['red_edges'])))[1];print([(k,sum(k in x['counts'] for x in out),sum(x['counts'].get(k,0) for x in out)) for k in ('paired','opposite_clocks','rotations','coherent')]);print([(x['record'],x['counts']) for x in out if x['certificate']]);(D/'ramsey_37_blind_star_transport.json').write_text(json.dumps(out,indent=2)+'\n')
