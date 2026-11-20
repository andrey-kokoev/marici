"""Blind red-neighbor decoding of oriented triples and intrinsic rooted invariant distinguishing the fixed vertices. No use of preselected apex in the decoder."""
from pathlib import Path
from itertools import combinations
import json
D=Path(__file__).resolve().parents[1]/'results';load=lambda f:json.loads((D/(f+'.json')).read_text());g=load('ramsey_37_dual_stars');N={u:set() for u in range(22)}
for u,v in g['red_edges']:N[u].add(v);N[v].add(u)
def invariant(v):
    w=[u for u in N if len(N[u]&N[v])==1];return dict(vertices=w,edges=sum(y in N[x] for x,y in combinations(w,2)))
def decode(t):return set.intersection(*(N[u] for u in t))
out=[]
for row in load('ramsey_37_oriented_three_plus_seven'):
    c,a=row['center'],row['apex'];da,db=[decode(row[k]) for k in ('pole0_triple','pole6_triple')];assert da&db=={a};ic,ia=invariant(c),invariant(a);assert {ic['edges'],ia['edges']}=={3,4} and len(da)==len(db)==(2 if ic['edges']==3 else 1);out.append(dict(center=c,apex=a,center_invariant=ic,apex_invariant=ia,decodings=[sorted(da),sorted(db)]))
print(out[:2]);(D/'ramsey_37_apex_decode.json').write_text(json.dumps(out,indent=2)+'\n')
