"""Representation audit (not discovery). Use the reflection on catalogue record 5 to identify its fixed sites and transpositions with tetrahedral sites. Verify the resulting signature lookup and clique bounds directly."""
from pathlib import Path
from itertools import combinations
import json,random
import ramsey_marked_role_comparator as m
H=Path(__file__).parent
m.incidence=m.corner_incidence=m.endpoint_incidence=m.port_edge_incidence=m.edge_pair_incidence=True
G=[0,1,3,2];X=m.X
def refl(x):
    v=[G[i] for i in x[1:]];return (x[0],*(sorted(v) if x[0]=='e' else v))
r=[X.index(refl(x)) for x in X];row=json.loads((H/'ramsey_37_marked_port_involutions.json').read_text())[0];p=row['example'];rec=row['record'];line=(H/'pauli-realization-catalogues/r37_22.g6').read_text().splitlines()[rec-1];bits=''.join(f'{ord(c)-63:06b}' for c in line[1:]);red=lambda i,j:bits[max(i,j)*(max(i,j)-1)//2+min(i,j)]=='1'
def parts(p):return [i for i,j in enumerate(p) if i==j],[(i,j) for i,j in enumerate(p) if i<j]
a,b=parts(r);f,t=parts(p);out={};
for flat in (True,False):
    E=m.run(flat,'cpe',True);classes={v:[] for v in E.values()};orbits={}
    for e,v in E.items():
        i,j=e;rev=tuple(sorted((r[i],r[j])));assert E[rev]==v;orbits.setdefault(v,set()).add(min(e,rev));classes[v].append(e)
    print(flat,len(classes),sum(map(len,orbits.values())),flush=True);rng=random.Random(0)
    for attempt in range(1,100001):
        rng.shuffle(f);rng.shuffle(t);mapping=dict(zip(a,f));
        for (x,y),pair in zip(b,t):mapping[x],mapping[y]=pair[::rng.choice([1,-1])]
        if any(len({red(mapping[i],mapping[j]) for i,j in es})>1 for es in orbits.values() if len(es)>1):continue
        R={e for e in E if red(*(mapping[i] for i in e))};lookup={E[e] for e in R};assert {e for e in E if E[e] in lookup}==R
        assert not any(all(e in R for e in combinations(c,2)) for c in combinations(range(22),3));assert all(any(e in R for e in combinations(c,2)) for c in combinations(range(22),7));break
    else:raise RuntimeError('No fit within search budget')
    out[str(flat)]=dict(classes=len(classes),orbits=sum(map(len,orbits.values())),record=rec,mapping=[mapping[i] for i in range(22)],red_classes=sorted(v.bit_length()-1 for v in lookup),red_edges=len(R));print('fit',attempt,len(R))
(H/'ramsey_marked_root_profiles.json').write_text(json.dumps(out,indent=2)+'\n')
