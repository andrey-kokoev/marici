"""Retrospective within-goal test, stripping away first-candidate ranking."""
from ramsey38_precommit_holdout import P,R,blocker,select,prev,json
from ramsey38_large_pivot_holdout import P as lp,R as lr
from ramsey38_one_pin_holdout import P as op,R as ore
from ramsey38_matched_mesh_trial import P as mp,R as mr
from ramsey38_append_holdout import proposals,setup,graph,attaches,shelling,face_assignments,faces,boundary
from itertools import permutations
from collections import Counter

def run():
    out=[];counts=Counter()
    for p,r in [(mp,mr),(op,ore),(lp,lr),(P,R)]:
        ref=json.loads(r.read_text());assert ref['prediction_sha']==prev.sha(p.read_bytes());wanted={(x['record'],x['j'],x['l']) for x in ref['results'] if x['routes']>=2}
        for e in json.loads(p.read_text())['cases']:
            if not any(i==e['record'] for i,j,l in wanted):continue
            def collect(e,L,rs,cs):return dict(candidates=cs)
            ds=proposals(e,collect);L,rs,_=setup(graph(e['word']),e['u']);dec=lambda m:frozenset(v for i,v in enumerate(L) if m>>i&1);cache={}
            for d in ds:
                if (e['record'],d['j'],d['l']) not in wanted:continue
                opts=[]
                for rank,c in enumerate(d['candidates'],1):
                    _,a,bd,w,n,end,collar=c;base=select(e,L,rs,[c]);q=base['commit']
                    if not q:continue
                    veto=blocker(L,rs,q);x,v=a;y,t=n;r1={**rs,x:rs[x]|1<<L.index(v)};r2={**r1,y:rs[y]|1<<L.index(t)};need=set(map(dec,r2.values()));k=(a,bd,w)
                    if k not in cache:cache[k]=[set(ts) for ts in face_assignments(L,set(map(dec,r1.values()))|{dec(rs[x])|{w}},set(map(dec,bd))) if shelling(ts)]
                    E=set(map(frozenset,collar));F=set(map(dec,end));cert=None
                    for A in cache[k]:
                        if A&E or boundary(A|E)!=F or not all(any(h<=t for t in A|E) for h in need):continue
                        order=next((o for o in permutations(E) if all(attaches(A|set(o[:i]),t) for i,t in enumerate(o))),None)
                        if order:cert=dict(start=[sorted(t) for t in shelling(A)],append=[sorted(t) for t in order]);break
                    assert not (cert and veto is not None);counts['good' if cert else 'bad_veto' if veto is not None else 'bad_pass']+=1;opts.append(dict(rank=rank,commit=q,blocker=veto,certificate=cert))
                kinds={bool(z['certificate']) for z in opts};contrast=kinds=={True,False};rejected=any(z['blocker'] is not None for z in opts);counts['goals']+=1;counts['mixed']+=contrast;counts['discriminated']+=contrast and rejected;out.append(dict(record=e['record'],j=d['j'],l=d['l'],options=opts))
                if contrast:print('mixed',e['record'],d['j'],d['l'],[(z['rank'],z['blocker'],bool(z['certificate'])) for z in opts],flush=True)
    print(counts);prev.save(prev.out/'ramsey38_within_goal_filter.json',dict(scope='All requests with >=2 counted extension routes in four completed exhaustive holdouts, all ranked final-disk-pass candidates, collar length 1 or 2.',counts=dict(counts),goals=out))
if __name__=='__main__':run()
