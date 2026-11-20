"""Keep the three stars and seven fixed as sets. Mark one apex-red leaf in each star, breaking the middle tie by adjacency to a named pole. Verify reflection transports the two marked partitions; it fixes neither individually."""
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';read=lambda f:json.loads((D/(f+'.json')).read_text());g=read('ramsey_37_dual_stars');N={v:set() for v in range(22)}
for a,b in g['red_edges']:N[a].add(b);N[b].add(a)
s=g['reflection'];r=list(range(22))
for row in g['rows']:
    for i,v in enumerate(row):r[v]=row[(i+1)%5]
out=[]
for rec in read('ramsey_37_three_stars_apex'):
    for c in rec['choices']:
        B=[set(rec['left']),{c['center'],*c['leaves']},set(rec['right'])];centers=[next(v for v in S if len(N[v]&S)==4) for S in B];remaining=set(N)-set.union(*B);ap=c['apex'];contacts=[(S-{v})&N[ap] for S,v in zip(B,centers)];assert list(map(len,contacts))==[1,2,1];l,=contacts[0];u,=contacts[2];triples=[]
        for pole in [0,6]:
            m,=contacts[1]&N[pole];marks=[l,m,u];assert all(len((S-{w})&N[v])==3 for S,v,w in zip(B,centers,marks));assert len(remaining)==7 and not remaining&set(marks);triples.append(marks)
        assert {s[v] for v in triples[0]}==set(triples[1])!=set(triples[0]);assert {s[v] for v in remaining}==remaining;out.append(dict(center=c['center'],apex=ap,pole0_triple=triples[0],pole6_triple=triples[1],seven=sorted(remaining)))
    s=[r[s[r.index(v)]] for v in range(22)]
print(out[:2]);(D/'ramsey_37_oriented_three_plus_seven.json').write_text(json.dumps(out,indent=2)+'\n')
