"""Profile forward-to-join pipeline; bit-slice all chains with fixed boundary across queries."""
import ramsey38_dual_batch_holdout as base
from ramsey38_shared_twist10 import face_assignments as reference
from itertools import combinations
from collections import Counter
from functools import lru_cache
from statistics import median
from time import perf_counter_ns
import gc

@lru_cache(None)
def parity_basis(L):
    apex=min(L);ts=list(map(frozenset,combinations(L,4)));tri=list(map(frozenset,combinations(L,3)));idx={t:i for i,t in enumerate(ts)};axes=[t for t in ts if apex not in t];N=1<<len(axes);full=(1<<N)-1;cols=[0]*len(ts)
    for j,t in enumerate(axes):
        half=1<<j;pat=(full//((1<<(2*half))-1))*(((1<<half)-1)<<half)
        for q in combinations(t|{apex},4):cols[idx[frozenset(q)]]^=pat
    return ts,tri,idx,cols,full,{f:[i for i,t in enumerate(ts) if f<=t] for f in tri}

def parallel_chains(L,req,bd):
    ts,tri,idx,cols,full,car=parity_basis(tuple(L));cols=list(cols);v=min(L)
    for f in bd:
        if v not in f:cols[idx[f|{v}]]^=full
    live=full
    for s in req:
        opts=0
        for i,t in enumerate(ts):
            if s<=t:opts|=cols[i]
        live &= opts
    # Each chain has fixed face parity already. Odd boundary faces cannot have
    # three hits; even internal faces cannot have four. Four carriers on seven labels.
    for f in tri:
        a,b,c,d=(cols[i] for i in car[f]);bad=((a&b&(c|d))|(c&d&(a|b))) if f in bd else a&b&c&d;live &= ~bad
        if not live:return
    while live:
        bit=live&-live;live^=bit;yield [t for i,t in enumerate(ts) if cols[i]&bit]

def run():
    data=base.json.loads(base.P.read_text());base.templates();ref_cache={};report=[];gold=None;orig={n:getattr(base,n) for n in ['prepare','geometry','face_assignments','shelling','extend','make_search']}
    for seq in [(False,True),(True,False)]*2:
        for fast in seq:
            # New basis cache per timed batch; only universal sphere library warm.
            parity_basis.cache_clear();phase=Counter();calls=Counter();captured={}
            def timed(n,fn):
                def f(*a,**kw):
                    t=perf_counter_ns();r=fn(*a,**kw);phase[n]+=perf_counter_ns()-t;calls[n]+=1;return r
                return f
            def assigns(L,req,bd):
                x=list((parallel_chains if fast else reference)(L,req,bd));captured[tuple(L),frozenset(req),frozenset(bd)]=x;return x
            class Geometry:
                cache_clear=staticmethod(orig['geometry'].cache_clear)
                __call__=staticmethod(timed('geometry',orig['geometry']))
            def prepare(*args):
                L,rows,ts,dec,stage,ch=orig['prepare'](*args);return L,rows,ts,dec,timed('shell_lookup',stage),ch
            base.geometry=Geometry();base.prepare=timed('prepare',prepare);base.make_search=lambda *a:timed('traverse',orig['make_search'](*a));base.face_assignments=timed('face_assignment',assigns);base.shelling=timed('shelling',orig['shelling']);base.extend=timed('extension',orig['extend']);gc.collect();t=perf_counter_ns()
            try:r=base.run(data,'join')
            finally:
                for n,fn in orig.items():setattr(base,n,fn)
            total=perf_counter_ns()-t;phase['other']=total-sum(phase.values());phase['total']=total
            norm={k:{frozenset(z) for z in x} for k,x in captured.items()}
            if gold is None:gold=r;ref_cache=norm
            else:assert r==gold and norm==ref_cache
            report.append(dict(fast=fast,ms={k:v/1e6 for k,v in phase.items()},calls=dict(calls)));print(fast,round(total/1e6,1),flush=True)
    med={str(f):{k:round(median(z['ms'][k] for z in report if z['fast']==f),3) for k in report[0]['ms']} for f in [False,True]};print(med,len(ref_cache),sum(map(len,ref_cache.values())),report[0]['calls']);base.prev.save(base.prev.out/'ramsey38_surface_fiber_profile.json',dict(sample_sha=base.prev.sha(base.P.read_bytes()),phase_medians_ms=med,rounds=report,unique_queries=len(ref_cache),assignment_occurrences=sum(map(len,ref_cache.values()))))
if __name__=='__main__':run()
