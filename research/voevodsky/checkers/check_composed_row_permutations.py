"""Two row transports compose mathematically but remain two synthetic witnesses."""
from hashlib import sha256
from pathlib import Path
import json
rows=('left','right','bottom','top');weights=(0,1,0,0)
p=(2,0,3,1);q=(1,3,0,2)
def act(seq,perm):
 assert sorted(perm)==list(range(len(seq)))
 return tuple(seq[i] for i in perm)
intermediate=act(rows,p);final=act(intermediate,q)
wp=act(weights,p);wfinal=act(wp,q)
composed=tuple(p[i] for i in q)
assert final==act(rows,composed) and wfinal==act(weights,composed)
H=lambda x:sha256(repr(x).encode()).hexdigest()
chain=(('source','middle',p),('middle','target',q))
direct=(('source','target',composed),)
assert H(chain)!=H(direct) and len(chain)==2 and len(direct)==1
report={'passed':True,'sequential_vs_direct_math':'identical ordered rows and transported weights','composed_permutation':composed,'synthetic_history':'two intermediate witness edges distinct from hypothetical direct edge','scope':'Local slot maps only, no actual transport events, source issuer or analytic correspondence.'}
out=Path(__file__).resolve().parents[1]/'results/composed-row-permutations.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
