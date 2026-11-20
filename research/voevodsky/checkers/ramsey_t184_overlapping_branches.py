"""T184 one-face patch: overlapping two-branch flips, then all overlapping whole-branch flips. No fitted base attachment."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
HOME=Path(__file__).resolve().parents[1];D=json.loads((HOME/'results/esd7_explicit_analytical_census.json').read_text());T=next(t for t in D['tetrahedra'] if t['id']=='T184');V=T['vertices'];O=[]
for v in V:
    a=[set(q['vertices'])-set(V) for q in D['tetrahedra'] if q!=T and set(V)-{v}<=set(q['vertices'])];assert len(a)==1 and len(a[0])==1;O.append(a[0].pop())
P=V+O;assert len(set(P))==8
labels={frozenset(e['vertices']):e['transfer_mask'] for e in D['edges']};pairs=[(1<<i|1<<j,labels.get(frozenset((P[i],P[j])),'absent')) for i,j in combinations(range(8),2)];types=sorted({z for _,z in pairs});out=Counter();hist=Counter();witness=None
# Include every incident choice (unlabelled family) of subsets with a common branch
# and a private branch on either side. First screen the canonical two-against-two splits.
moves=[(a,b) for a,b in combinations(range(1,16),2) if a&b and a&~b and b&~a];double=[(a,b) for a,b in moves if a.bit_count()==b.bit_count()==2];assert len(double)==12
def expand(a):return a|(a<<4)
for mask in range(1<<len(types)):
    red=[p for p,z in pairs if mask>>types.index(z)&1];blue=[p for p,z in pairs if not(mask>>types.index(z)&1)]
    rc=[s for s in range(256) if any(s&p==p for p in red)];tri=any(all((s^i) in red for i in [1<<j for j in range(8) if s>>j&1]) for s in range(256) if s.bit_count()==3);ind=[s for s in range(256) if s not in rc];
    if tri or any(s.bit_count()>=7 for s in ind):continue
    out['admissible']+=1;B6=[s for s in ind if s.bit_count()==6];v=[(int(s not in rc),int(not any(s&t==0 for t in B6))) for s in range(256)];bad=[s for s in range(256) if v[s]==(0,0)];hist[len(bad)]+=1
    assert set(bad)=={p for p in red if all(p&q for q in red)}
    if not bad:continue
    for a,b in moves:
        x,y=expand(a),expand(b)
        for s in bad:
            if {v[s^x],v[s^y]}=={(1,0),(0,1)} and v[s^x^y]==(1,1):
                out['all_squares']+=1;out['two_branch_squares']+=int((a,b) in double)
                if witness is None:witness=dict(red_types=[z for i,z in enumerate(types) if mask>>i&1],base=s,flips=[x,y])
r=dict(roles=P,decoder_count=2**len(types),admissible=out['admissible'],overlapping_two_branch_pairs=len(double),overlapping_nonnested_pairs=len(moves),starting_masks=256,double_failure_counts=dict(hist),two_branch_squares=out['two_branch_squares'],all_squares=out['all_squares'],example=witness);print(json.dumps(r));(HOME/'results/ramsey_t184_overlapping_branches.json').write_text(json.dumps(r,indent=2)+'\n')
