"""Classify four-root overlaps by affine orbits of the actual 35-circle. Test whether the full unoriented weighted pair graph determines core size away from 13 too."""
from itertools import combinations,permutations
from math import gcd
from pathlib import Path
from collections import defaultdict,Counter
import json
D=Path(__file__).resolve().parents[1]/'results'
def main():
    ds=set(json.loads((D/'ramsey_39_glue_vs_circle.json').read_text())['circle_distances']);S=ds|{35-d for d in ds};N=[{(x+s)%35 for s in S} for x in range(35)];V=set(range(35));mult=[a for a in range(35) if gcd(a,35)==1 and {a*s%35 for s in S}==S];covered=set();groups=defaultdict(list);hits=[];counts=Counter()
    for q in combinations(range(35),4):
        if q in covered or any(b in N[a] for a,b in combinations(q,2)):continue
        orbit={tuple(sorted((a*x+b)%35 for x in q)) for a in mult for b in V};assert not orbit&covered;covered.update(orbit)
        p=min(tuple(len(N[i]&N[j]) for i,j in combinations(z,2)) for z in permutations(q));t=[len(N[a]&N[b]&N[c]) for a,b,c in combinations(q,3)];f=len(set.intersection(*(N[i] for i in q)));core=len(V-set(q)-set.union(*(N[i] for i in q)));assert core==-1+sum(p)-sum(t)+f
        rec=dict(q=q,pairs=p,triples=t,four=f,core=core,orbit=len(orbit));groups[p].append(rec);counts[core]+=len(orbit)
        if core==13:hits.append(rec)
    ambiguous=[rs for rs in groups.values() if len({r['core'] for r in rs})>1];example=next(([rs[0],next(r for r in rs if r['core']!=rs[0]['core'])] for rs in ambiguous),None);assert len(covered)==10150 and sum(r['orbit'] for r in hits)==210
    out=dict(multipliers=mult,affine_order=35*len(mult),orbits=sum(map(len,groups.values())),pair_types=len(groups),ambiguous_types=len(ambiguous),ambiguous_example=example,core_hist=dict(sorted(counts.items())),successful_orbits=hits);print(out);(D/'ramsey_39_affine_overlap_orbits.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
