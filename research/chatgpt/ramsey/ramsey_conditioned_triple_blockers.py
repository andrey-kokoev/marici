"""Predict feasibility of EVERY independent three-vertex commitment on the 12 hard fixed triples. Only graph, three old ports and commitment enter the predictor. Minimal repair list used afterwards as oracle."""
from itertools import combinations
from functools import lru_cache
from collections import Counter
from ramsey_fork_audit_uniform import D,json,grow,inds
from ramsey_final_miss_levels import bits

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=grow(p['stem_graphs'][-1],p['alternate']['to34']);I=inds(H);trip=[s for s in I if s.bit_count()==3];T=[s for s in I if 6<=s.bit_count()<=8];F=(1<<34)-1;prev=json.loads((D/'ramsey_repair_pair_gluing.json').read_text());ks={tuple(r['triple']):r['minima'] for r in json.loads((D/'ramsey_compulsory_kernel_test.json').read_text())['triples']};tot=Counter();hard=Counter();ex=None;remaining=[]
    for r in prev:
        if not r['spurious']:continue
        q=r['fixed'];rows=[s for s in T if s.bit_count()+sum(not s&t for t in q)==9];cols=[sum(1<<i for i,s in enumerate(rows) if s>>v&1) for v in range(34)];full=(1<<len(rows))-1
        @lru_cache(None)
        def uncovered(live):
            hit=0
            for v in bits(live):
                hit|=cols[v]
                if hit==full:break
            return full^hit
        mins=ks[tuple(q)];blocks={s:sum(1<<i for i,k in enumerate(mins) if H[s]&k) for s in range(34)};allk=(1<<len(mins))-1
        for t in trip:
            v=list(bits(t));live=F&~(H[v[0]]|H[v[1]]|H[v[2]]);init=live;depth=0
            while not uncovered(live):
                ban=sum(1<<x for x in bits(live) if uncovered(live&~H[x]));
                if not ban:break
                live^=ban;depth+=1
            ok=not uncovered(live);a,b,c=(blocks[x] for x in v);truth=(a|b|c)!=allk;assert ok or not truth;tot[truth,ok]+=1
            if not truth and all(x!=allk for x in (a|b,b|c,a|c)):
                hard['undetected' if ok else str(depth)]+=1
                if ok:remaining.append(dict(fixed=q,commit=v,live=list(bits(live))))
                if ex is None and not ok:
                    idx=next(bits(uncovered(live)));ex=dict(fixed=q,commit=v,depth=depth,row=list(bits(rows[idx])),initial_options=list(bits(rows[idx]&init)))
        uncovered.cache_clear()
    return dict(all={str(k):v for k,v in tot.items()},pairwise_feasible_but_impossible=hard,example=ex,remaining=remaining)
if __name__=='__main__':
    out=run();print(out['all'],out['pairwise_feasible_but_impossible'],out['example']);(D/'ramsey_conditioned_triple_blockers.json').write_text(json.dumps(out)+'\n')
