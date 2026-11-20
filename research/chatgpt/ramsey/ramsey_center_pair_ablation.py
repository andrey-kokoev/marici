"""Branch on partner internal color, then ablate clique constraints from one/both center slots. Derive using only host and center; check full model's types against independent two-pair catalogue after prediction. For each relaxation verify any found size-three menu by individual support (>=2/3)."""
from itertools import combinations
from pathlib import Path
import json
H=Path(__file__).parent;load=lambda f:json.loads((H/f).read_text());swap=lambda m:((m&21845)<<1)|((m&43690)>>1)
def test(N,center):
    I=[0];a,b,c=center;assert c==0
    for i,n in enumerate(N):I += [m|1<<i for m in I if not m&n]
    by={k:[m for m in I if m.bit_count()==k] for k in (3,4,5)}
    def hits(m,k):return all(m&f for f in by[k])
    types={k:[] for k in ('internal','one','both','full')}
    for m in I:
        t=swap(m);u=m|t
        if t<m or not all(hits(x|m,5) for x in [a,b]) or not hits(a|b|m,4):continue
        for red in [0,1]:
            if (m&t if red else not hits(u,5)):continue
            one=red or all(hits(x|u,4) for x in [a,b]);both=red or hits(a|b|u,3)
            for k,accept in [('internal',True),('one',one),('both',both),('full',one and both)]:
                if accept:types[k].append((m,t,red))
    def menu(T):
        slots=sorted({x for x,_,_ in T});full=(1<<len(slots))-1;ds={}
        for f in by[5]:
            for r in range(16):
                p=sum(1<<j for j,m in enumerate(slots) if any(x>>r&1 and not x&f for x in (m,swap(m))))
                if p:ds[p]=(r,f)
        maximal=[p for p in ds if not any(p!=q and p&q==p for q in ds)];ans=None
        if full in ds:ans=[ds[full]]
        else:
            for p,q,r in combinations(maximal,3):
                if ((p&q)|(p&r)|(q&r))==full:ans=[ds[v] for v in (p,q,r)];break
        if ans:assert all(sum(any(x>>r&1 and not x&f for x in (m,swap(m))) for r,f in ans)>=min(2,len(ans)) for m in slots)
        return dict(types=len(T),menu=ans)
    return {k:menu(t) for k,t in types.items()},set(types['full'])
hosts={(h['record'],tuple(h['order'])):h['N'] for h in load('ramsey_strict_aligned_hosts.json')};out=[]
for r in load('ramsey_signature_core.json'):
    res,full=test(hosts[r['record'],tuple(r['order'])],r['center']);assert full==set(map(tuple,r['partners']));assert res['full']['menu'];print(r['record'],[(k,v['types'],bool(v['menu'])) for k,v in res.items()]);out.append(dict(record=r['record'],center=r['center'],tests=res))
(H/'ramsey_center_pair_ablation.json').write_text(json.dumps(out,indent=2)+'\n')
