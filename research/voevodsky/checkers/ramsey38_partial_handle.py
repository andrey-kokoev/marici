"""Minimum triangle count for a nonplanar orientable sublink of each punctured torus.
Compare free disk embedding and embedding relative to the fixed boundary rim.
"""
from functools import lru_cache
from itertools import combinations
from collections import Counter
from ramsey38_root15_link_rotation import link_domains
from ramsey38_cached_holdout import H,prev,inputs,json
from ramsey38_early_sign_trial import neg
from ramsey38_shared_twist10 import faces

@lru_cache(None)
def planar(fs):return not fs or bool(link_domains(fs))
def shortest(base,opts):
    opts=sorted(opts,key=sorted)
    for k in range(len(opts)+1):
        hits=[q for q in combinations(opts,k) if not planar(frozenset(base|set(q)))];
        if hits:return k,hits
    raise AssertionError('embedded torus?')
def run():
    cases=json.loads((prev.out/'ramsey38_holdout_survivors.json').read_text());frozen=json.loads(H.read_text());out=[]
    for d in cases['cases']:
        for r in d['results']:
            if not any(p==[1,True,-1] for p in r['non_disk'].values()):continue
            w,=(int(v) for v,p in r['non_disk'].items() if p==[1,True,-1]);e=next(e for e in frozen['cases'] if (e['record'],e['u'])==(d['record'],d['root']));b,_,x,rs,v=inputs(e);S=rs[x];rs[x]|=v;labs=sorted(b[e['u']]);dec=lambda m:frozenset(a for i,a in enumerate(labs) if m>>i&1);req=set(map(dec,rs.values()))|{dec(S)|{d['tip']}};fixed={s-{w} for s in req if len(s)==4 and w in s};bd=set(map(dec,d['bd']));rim={(f-{w})|{0} for f in bd if w in f};fs={frozenset(t)-{w} for t in r['cells'] if w in t};assert fixed<=fs and not neg(fs|rim);z=dict(row=d['row'],tip=d['tip'],bd=d['bd'],vertex=w,triangles=faces(fs),fixed=faces(fixed),rim=faces(f-{0} for f in rim))
            for name,base,opts in [('free',set(),fs),('relative',fixed|rim,fs-fixed)]:
                k,qs=shortest(base,opts);z[name]=dict(k=k,minimum_witnesses=[faces(q) for q in qs]);assert k>0
            out.append(z);print(z['row'],w,len(fs),len(fixed),z['free']['k'],z['relative']['k'],z['relative']['minimum_witnesses'][0],flush=True)
    assert len(out)==8;prev.save(prev.out/'ramsey38_partial_handle.json',dict(cases=out))
if __name__=='__main__':run()
