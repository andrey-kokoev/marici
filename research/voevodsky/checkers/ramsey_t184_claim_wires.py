"""Six unordered contacts on four claim sites; every active wire carries one shared R+ or B- token. The global exclusions already rule out the other two tokens. Compare per-site existence against per-wire witnessing. Count active wire records, not Ramsey vertices."""
from itertools import combinations,product
from pathlib import Path
from collections import Counter
import json
D=Path(__file__).resolve().parents[1]/'results';edges=list(combinations(range(4),2));sites=['no R-','no B+','some R+','some B-'];modes=['site','wire'];counts={m:Counter() for m in modes};ex={m:{} for m in modes};missing=set()
for x in product(('-', 'R+', 'B-'),repeat=6):
    if not all(any(v==wanted and i in e for e,v in zip(edges,x)) for i,wanted in [(2,'R+'),(3,'B-')]):continue
    k=sum(v!='-' for v in x);strict=all(v=='-' or ((2 not in e or v=='R+') and (3 not in e or v=='B-')) for e,v in zip(edges,x))
    for mode in (modes if strict else ['site']):
        counts[mode][k]+=1;ex[mode].setdefault(k,x)
    if strict and k==5:missing.add(edges[x.index('-')])
assert counts['site'][6]>0 and max(counts['wire'])==5 and missing=={(2,3)}
out=dict(sites=sites,edges=edges,counts=counts,max_examples={m:ex[m][max(counts[m])] for m in modes},strict_missing=list(missing));print(out);(D/'ramsey_t184_claim_wires.json').write_text(json.dumps(out,indent=2)+'\n')
