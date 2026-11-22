"""Whole-wiring lower bounds on rooted Exoo charts. Retain all links incident to the root or its neighbours; every exterior ID and its signature is fixed. Permutations inside equal-signature cells give distinct labelled legal completions by rigidity. Prove nonseparation even by an entire reference star. Also record single-flip mandatory probes. No enumeration of all completions claimed."""
from exoo39_symbolic_relations import edges
from itertools import combinations
from math import factorial,prod
from pathlib import Path
import json

def run():
    E=edges();V=range(39);H=[sum(1<<j for j in V if tuple(sorted((i,j))) in E) for i in V];I=[0]
    for i,h in enumerate(H):I += [s|(1<<i) for s in I if not s&h]
    assert max(s.bit_count() for s in I)==9 and all(not H[i]&H[j] for i,j in E);T=[s for s in I if s.bit_count()==8];c=[0]*39
    while len(set(c))<39:
        sig=[(c[i],tuple(sorted(c[j] for j in V if H[i]>>j&1))) for i in V];mp={k:i for i,k in enumerate(sorted(set(sig)))};nc=[mp[k] for k in sig];assert len(set(nc))>len(set(c));c=nc
    F=[(i,j) for i,j in combinations(V,2) if (not any(not s&(H[i]|H[j]) for s in T) if (i,j) in E else not H[i]&H[j])];rs=[]
    for r in V:
        W=[i for i in V if i!=r and not H[r]>>i&1];cells={s:[i for i in W if H[i]&H[r]==s] for s in {H[i]&H[r] for i in W}};order=prod(factorial(len(g)) for g in cells.values());swaps=sum((list(combinations(g,2)) for g in cells.values()),[]);examples={}
        for p in V:
            witness=next(((u,v) for u,v in swaps if p not in (u,v) and ((H[p]>>u)^(H[p]>>v))&1==0),None)
            if witness:examples[p]=witness
        rs.append(dict(root=r,degree=H[r].bit_count(),cells=list(cells.values()),orbit_size=order,min_bits=(order-1).bit_length(),mandatory=[(i,j) for i,j in F if i in W and j in W],blind_star_swaps=examples))
    return rs
if __name__=='__main__':
    rs=run();print([(r['root'],r['degree'],r['orbit_size'],r['min_bits'],len(r['blind_star_swaps'])) for r in rs]);Path(__file__).with_suffix('.json').write_text(json.dumps(rs)+'\n')
