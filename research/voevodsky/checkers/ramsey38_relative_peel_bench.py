"""Matched prefix benchmark: freeze route-derived pairs without testing extension outcomes."""
from ramsey38_middle_choice_holdout import prev,json,sys,graph,setup,gzip,add,key,prepare,face_assignments,shelling,extend,faces,boundary,attaches,Counter
from ramsey38_shared_peel_trial import Peeler
from itertools import permutations
from functools import lru_cache
from time import perf_counter_ns
from statistics import median
import gc
P=prev.out/'ramsey38_relative_peel_cases.json';R=prev.out/'ramsey38_relative_peel_bench.json'
protocol='First 5 distinct canonical roots after 257216 with a legal two-edit promotion, sole edge release then two including first, and at least one nested candidate pair. First root per record. All distinct contained pairs of certified first balls and face-count-valid final candidates on eligible shells. No final shellability or relative extension tested in sampling. Compare original forward extension and reverse peeling, two-level cache ablations. Search-only full batches incl mask table construction/encoding and fresh caches.'
def freeze():
    es=[];seen=set()
    with gzip.open(prev.catalogue,'rt') as fp:
        for i,line in enumerate(fp,1):
            if i<=257216:continue
            if i>277216:break
            w=line.strip();g=graph(w)
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,rs,ms=setup(g,u)
                if len(ms)<2 or max(map(int.bit_count,rs.values()))>4 or sum(s.bit_count()==2 for s in rs.values())<2:continue
                scripts=[(a,b) for a in ms for b in setup(add(g,a),u)[2]];k=key(L,rs,ms)
                if not scripts or k in seen:continue
                seen.add(k);L,rows,cells,dec,stage,_=prepare(g,u);pairs=set()
                @lru_cache(None)
                def cand(req,b):return [frozenset(z) for z in face_assignments(L,req,set(map(dec,b)))]
                for a,b in scripts:
                    r,S=stage((a,));q,T=stage(tuple(sorted((a,b))))
                    for H,bds in T.items():
                        ends=[t for bd in bds for t in cand(q,bd)]
                        for j in H:
                            for bd in S.get(frozenset([j]),[]):
                                for m in cand(r,bd):
                                    if shelling(m):pairs.update((m,t) for t in ends if m<t)
                if pairs:
                    es.append(dict(record=i,u=u,cases=sorted([[faces(s),faces(t)] for s,t in pairs])));print(i,len(pairs),flush=True);break
            if len(es)==5:break
    assert len(es)==5;prev.save(P,dict(protocol=protocol,cases=es))

def work(raw,mode):
    stats=Counter();out=[]
    if mode!='forward':engine=Peeler(True)
    @lru_cache(None)
    def moves(m):
        ans=[];rem=m
        while rem:
            b=rem&-rem;rem^=b;i=b.bit_length()-1;rest=m^b;adj,rules=engine.tab[i];k=0
            for j,a in enumerate(adj):
                h=a&rest
                if h&(h-1):break
                if h:k|=1<<j
            else:
                if not rules[k]&rest:ans.append(b)
        return ans
    @lru_cache(None)
    def rev(m,p):
        if m==p:return ()
        for b in moves(m):
            if p&b:continue
            if mode=='checked' and not engine.peel(m^b,m):continue
            s=rev(m^b,p)
            if s is not None:return s+(b,)
        return None
    for s,t in raw:
        if mode=='forward':out.append(extend(s,t));continue
        if mode=='local':moves.cache_clear();rev.cache_clear()
        L=sorted(set().union(*t));pos={v:j for j,v in enumerate(L)};by={1<<engine.idx[tuple(sorted(pos[v] for v in f))]:f for f in t};m=sum(by);p=sum(b for b,f in by.items() if f in s);o=rev(m,p);out.append(tuple(by[b] for b in o) if o is not None else None)
    if mode!='forward':stats.update(move_hits=moves.cache_info().hits,relative_hits=rev.cache_info().hits,relative_states=rev.cache_info().currsize,ordinary_states=len(engine.memo))
    return out,dict(stats)
def bench():
    raw=[tuple(frozenset(map(frozenset,h)) for h in p) for e in json.loads(P.read_text())['cases'] for p in e['cases']];modes=['forward','local','shared','checked'];gold=None;times=[];stats={}
    for i in range(8):
        order=(modes if i<4 else modes[::-1]);order=order[i%4:]+order[:i%4];rnd={}
        for mode in order:
            gc.collect();start=perf_counter_ns();res,stats[mode]=work(raw,mode);rnd[mode]=(perf_counter_ns()-start)/1e6;yes=[o is not None for o in res];gold=yes if gold is None else gold;assert gold==yes
            for (s,t),o in zip(raw,res):
                if o is not None:assert set(o)==t-s and all(attaches(s|set(o[:j]),x) for j,x in enumerate(o))
        times.append(rnd)
    med={k:median(r[k] for r in times) for k in modes};print(len(raw),sum(gold),med,stats);prev.save(R,dict(sample_sha=prev.sha(P.read_bytes()),queries=len(raw),feasible=sum(gold),timings_ms=times,median_ms=med,cache_stats=stats))
if __name__=='__main__':{'freeze':freeze,'bench':bench}[sys.argv[1]]()
