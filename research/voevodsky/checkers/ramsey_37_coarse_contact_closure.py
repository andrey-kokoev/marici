"""Coarse contact = endpoint port pair, not exclusive four-port signature. Fine lifts are red squares r-a-m-b-r, m != r. Greatest closed family in which every pair has a lift ending at another surviving frame containing a,b. This does not impose agreement of composite routes."""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
import json
H=Path(__file__).resolve().parents[1];C=H.parent/'chatgpt/ramsey/pauli-realization-catalogues/r37_22.g6';out=[]
for idx,g in enumerate(C.read_text().splitlines(),1):
 b=''.join(f'{ord(c)-63:06b}' for c in g[1:]);N=[set() for _ in range(22)]
 for j in range(22):
    for i in range(j):
        if b[j*(j-1)//2+i]=='1':N[i].add(j);N[j].add(i)
 F={(r,P):list(combinations(P,2)) for r in range(22) for P in combinations(sorted(N[r]),4)};hist=[len(F)]
 while F:
    support=defaultdict(set)
    for (r,P),pairs in F.items():
        for p in pairs:support[p].add(r)
    new={k:ps for k,ps in F.items() if all(support[p]-{k[0]} for p in ps)}
    hist.append(len(new))
    if len(new)==len(F):break
    F=new
 out.append(dict(record=idx,counts=hist,stable=len(F)))
print('any local',sum(x['counts'][1]>0 for x in out),'any stable',sum(x['stable']>0 for x in out),'record 190',out[189]);(H/'results/ramsey_37_coarse_contact_closure.json').write_text(json.dumps(out,indent=2)+'\n')
