"""One possible N stop per gap, controlled only by (lap, left group, right group). Classify all masks giving exactly two stops at (3,7) and all p,q>=2. Internal counts vary independently, so a universal mask must omit RR and BB. Boundary order below is RB+,BR+,RB-,BR-."""
from itertools import combinations
from collections import Counter
E=[(s,k) for s in '+-' for k in ('RR','RB','BB','BR')]
def count(rule,p,q):return sum({'RR':p-1,'BB':q-1,'RB':1,'BR':1}[k] for s,k in rule)
local=[];uniform=[]
for mask in range(256):
    S={v for i,v in enumerate(E) if mask>>i&1}
    if count(S,3,7)!=2:continue
    local.append(S)
    if all(k in ('RB','BR') for s,k in S):
        assert all(count(S,p,q)==2 for p,q in [(2,2),(3,7),(7,3),(4,12)]);uniform.append(S)
assert len(local)==8 and len(uniform)==6
for S in uniform:
    reverse={('+' if s=='-' else '-',k[::-1]) for s,k in S};print(sorted(S),'both reversals invariant:',reverse==S)
