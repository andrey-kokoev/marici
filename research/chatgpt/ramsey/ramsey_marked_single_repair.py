"""Delete one selected orbit, optimize over all triangle-free supersets of retained orbits. Each skipped addition stays skipped on that branch. Bounds count even sevens impossible to cover by the union of all still-legal additions. No catalogue input."""
from itertools import combinations,permutations
from pathlib import Path
import json
D=Path(__file__).parent;V=range(4);X=[('c',i) for i in V]+[('p',*t) for t in permutations(V,2)]+[('e',*t) for t in combinations(V,2)]
def flip(x):
    a=[(0,1,3,2)[i] for i in x[1:]];return (x[0],*(sorted(a) if x[0]=='e' else a))
r=[X.index(flip(x)) for x in X];O=sorted({tuple(sorted({(i,j),tuple(sorted((r[i],r[j])))})) for i,j in combinations(range(22),2)});assert len(O)==127

def add(N,a):
    L=N.copy()
    for i,j in O[a]:
        if L[i]&L[j]:return None
        L[i]|=1<<j;L[j]|=1<<i
    return L

def sevens(N):
    def gen(w,h,m):
        if not h:yield m;return
        while w.bit_count()>=h:
            b=w&-w;w^=b;yield from gen(w&~N[b.bit_length()-1],h-1,m|b)
    return list(gen((1<<22)-1,7,0))

def solve(S,d):
    N=[0]*22
    for a in sorted(S-{d}):N=add(N,a);assert N is not None
    F=sevens(N);gain={};candidates=[]
    for a in range(127):
        if a in S-{d} or add(N,a) is None:continue
        g=sum(1<<k for k,t in enumerate(F) if any(t>>i&t>>j&1 for i,j in O[a]));gain[a]=g
        if g:candidates.append(a)
    best=len(F);witness=[]
    def dfs(N,live,C,path):
        nonlocal best,witness
        if live.bit_count()<best:best=live.bit_count();witness=path
        opts=[];union=0
        for a in C:
            g=gain[a]&live
            if g and (L:=add(N,a)) is not None:opts.append((g.bit_count(),a,g,L));union|=g
        if (live&~union).bit_count()>=best:return
        opts.sort(reverse=True);_,a,g,L=opts[0];rest=[t[1] for t in opts[1:]];dfs(L,live&~g,rest,path+[a]);dfs(N,live,rest,path)
    dfs(N,(1<<len(F))-1,candidates,[])
    for a in witness:N=add(N,a);assert N is not None
    assert len(sevens(N))==best;return dict(deleted=d,best=best,added=witness)

out=[]
for row in json.loads((D/'ramsey_marked_live_sevens.json').read_text()):
    if row['remaining']!=10:continue
    S={a for a,g in row['trace']};res=[solve(S,d) for d in sorted(S)];out.append(dict(flat=row['flat'],repairs=res));print(row['flat'],len(S),min(z['best'] for z in res),[(z['deleted'],z['best'],z['added']) for z in res if z['best']<10]);assert all(z['best']<=10 for z in res)
(D/'ramsey_marked_single_repair.json').write_text(json.dumps(out,indent=2)+'\n')
