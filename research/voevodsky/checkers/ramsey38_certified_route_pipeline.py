"""Time graph-to-marked-pair construction, not just the route on supplied endpoints."""
from ramsey38_nested_ball_obstruction_trial import P,prev,json,gzip,graph,prepare,setup,add,parallel_chains,Peeler,extend,faces
from ramsey38_marked_greedy_bench import greedy
from ramsey38_surface_fiber_profile import parity_basis,base
from functools import lru_cache
from statistics import median
from time import perf_counter_ns
import gc


def construct(inputs,method,*,certified_fillers=None):
    """Shared traversal. A supplied provider must return all shellable fillers."""
    if certified_fillers is None:
        solver=Peeler(True);parity_basis.cache_clear()
        def certified_fillers(labels,req,bd):
            return (ts for ts in parallel_chains(labels,req,bd) if solver(ts))
    out=[];tested=nested=0
    for word,u in inputs:
        g=graph(word);L,_,_,dec,stage,_=prepare(g,u);routes={}
        @lru_cache(None)
        def balls(req,bd):return [frozenset(ts) for ts in certified_fillers(L,req,set(map(dec,bd)))]
        for a in setup(g,u)[2]:
            for b in setup(add(g,a),u)[2]:
                r,S=stage((a,));q,T=stage(tuple(sorted((a,b))))
                for H,bds in T.items():
                    ends=[B for bd in bds for B in balls(q,bd)]
                    for j in H:
                        for bd in S.get(frozenset([j]),[]):
                            for A in balls(r,bd):
                                for B in ends:
                                    tested+=1
                                    if not A<B:continue
                                    nested+=1;order=method(A,B);assert order is not None;routes[A,B]=order
        out.append(routes)
    return out,tested,nested


def run():
    entries=json.loads(P.read_text())['entries'];want={e['record'] for e in entries};words={}
    with gzip.open(prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in want:words[i]=line.strip()
            if i==max(want):break
    inputs=[(words[e['record']],e['root']) for e in entries];expected=[]
    for e in entries:
        pairs=set()
        for z in e['ends']:
            cells=list(map(frozenset,z['cells']));pairs.update((frozenset(t for i,t in enumerate(cells) if m>>i&1),frozenset(cells)) for m in z['marked'])
        expected.append(pairs)
    from ramsey38_append_holdout import attaches
    base.templates();rounds=[];ref=None
    for i in range(6):
        times={}
        for k,method in ([('reference',extend),('greedy',greedy)][::1 if i%2==0 else -1]):
            gc.collect();start=perf_counter_ns();out,tested,nested=construct(inputs,method);times[k]=(perf_counter_ns()-start)/1e6
            assert list(map(set,out))==expected
            if ref is None:ref=out
            assert ref==out
            for d in out:
                for (A,B),order in d.items():
                    for t in order:assert t in B-A and attaches(A,t);A=A|{t}
                    assert A==B
        rounds.append(times);print(times,flush=True)
    res=dict(sample_sha=prev.sha(P.read_bytes()),roots=len(inputs),pairs=sum(map(len,expected)),comparisons=tested,nested_occurrences=nested,median_ms={k:median(r[k] for r in rounds) for k in rounds[0]},rounds_ms=rounds);print(res);prev.save(prev.out/'ramsey38_certified_route_pipeline.json',res)
if __name__=='__main__':run()
