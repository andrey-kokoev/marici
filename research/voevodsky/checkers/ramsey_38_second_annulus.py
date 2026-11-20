"""Extend the stored first certificate, not all possible first annuli. Exhaust simple second boundaries on unused non-pole/non-hub vertices, then test a flat monotone zipper. Both cyclic orientations are considered. A certificate requires manifold links, not just parity."""
from pathlib import Path
from itertools import combinations,permutations
from collections import Counter,defaultdict
import json
D=Path(__file__).resolve().parents[1]/'results';first=json.loads((D/'ramsey_38_annulus_glue.json').read_text());layers=json.loads((D/'ramsey_38_disk_routes_layer.json').read_text());E=set(map(tuple,json.loads((D/'ramsey_38_root_glue.json').read_text())['witness']['plus_edges']));red=lambda a,b:int(tuple(sorted((a,b))) in E)
def attach(I,O):
    m=len(I);n=len(O);bits=[0]
    for a,b in zip(O,O[1:]):bits.append(bits[-1]^red(a,b))
    if bits[-1]!=red(O[-1],O[0]):return None
    for flip in (0,1):
        ok=lambda i,j:red(I[i%m],O[j%n])==(bits[j%n]^flip)
        for k in range(m):
            if not ok(k,0):continue
            def walk(i,j,seen,faces):
                x=I[(k+i)%m];y=O[j%n]
                for a,b,z in [(i+1,j,I[(k+i+1)%m]),(i,j+1,O[(j+1)%n])]:
                    if a>m or b>n or not ok(k+a,b):continue
                    key=(a%m,b%n);done=a==m and b==n
                    if not done and key in seen:continue
                    F=faces+[[x,y,z]]
                    if done:return F
                    hit=walk(a,b,seen|{key},F)
                    if hit:return hit
            F=walk(0,0,{(0,0)},[])
            if F:return F

def verify(I,O,F):
    edges=Counter(tuple(sorted(e)) for f in F for e in combinations(f,2));boundary={tuple(sorted((u,v))) for L in (I,O) for u,v in zip(L,L[1:]+L[:1])};assert {e for e,n in edges.items() if n==1}==boundary and max(edges.values())==2 and len(I)+len(O)-len(edges)+len(F)==0
    for u in I+O:
        L=defaultdict(set)
        for f in F:
            if u in f:
                a,b=set(f)-{u};L[a].add(b);L[b].add(a)
        todo=[next(iter(L))];seen=set()
        while todo:
            a=todo.pop();seen.add(a);todo.extend(L[a]-seen)
        assert len(seen)==len(L) and sorted(map(len,L.values()))==[1,1]+[2]*(len(L)-2)
    assert all(sum(red(a,b) for a,b in combinations(f,2))%2==0 for f in F)
out=[]
for rec,layer in zip(first,layers):
    I=rec['outer'];unused=set(range(27))-set(I+rec['ring']+rec['poles']+[layer['hub']]);assert layer['ring']==rec['ring'] and all(not red(a,b) for a,b in zip(I,I[1:]+I[:1]));options={};sample=None
    for n in range(len(unused),2,-1):
        for subset in combinations(sorted(unused),n):
            for tail in permutations(subset[1:]):
                O=[subset[0],*tail];F=attach(I,O)
                if F:
                    verify(I,O,F);options.setdefault(n,set()).add(min(tuple(O),tuple([O[0]]+O[:0:-1])));
                    if sample is None:sample=dict(outer=O,faces=F)
    out.append(dict(poles=rec['poles'],ring=rec['ring'],inner=I,unused=sorted(unused),options_by_length={k:len(v) for k,v in options.items()},certificate=sample))
print(Counter((len(r['unused']),max(r['options_by_length'],default=0)) for r in out));print(out[0]);(D/'ramsey_38_second_annulus.json').write_text(json.dumps(out,indent=2)+'\n')
