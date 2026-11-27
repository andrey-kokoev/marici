"""Attribute wall time on the positive batch, excluding suspended generator time."""
from collections import Counter
from contextlib import ExitStack
from unittest.mock import patch
from statistics import median
from time import perf_counter_ns as now
import ramsey38_certified_route_pipeline as p


def profile(inputs):
    ns=Counter();counts=Counter();peeler=p.Peeler;prepare=p.prepare;chains=p.parallel_chains
    def timed(k,fn):
        def go(*args,**kw):
            t=now();v=fn(*args,**kw);ns[k]+=now()-t;counts[k]+=1;return v
        return go
    def solver(*args):return timed('shelling',timed('peel_setup',peeler)(*args))
    def prep(*args):
        L,r,c,dec,stage,z=timed('prepare',prepare)(*args);return L,r,c,dec,timed('stage',stage),z
    def gen(*args):
        counts['queries']+=1;it=chains(*args);sentinel=object()
        while True:
            t=now();v=next(it,sentinel);ns['fillers']+=now()-t
            if v is sentinel:return
            counts['candidates']+=1;yield v
    with ExitStack() as stack:
        for name,fn in [('prepare',prep),('Peeler',solver),('parallel_chains',gen)]:stack.enter_context(patch.object(p,name,fn))
        t=now();out=p.construct(inputs,timed('routes',p.greedy));total=now()-t
    ns['residual']=total-sum(ns.values());ns['total']=total;return out,dict(counts),{k:v/1e6 for k,v in ns.items()}


def run():
    entries=p.json.loads(p.P.read_text())['entries'];ids={e['record'] for e in entries};words={}
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in ids:words[i]=line.strip()
            if i>=max(ids):break
    inputs=[(words[e['record']],e['root']) for e in entries];p.base.templates();gold=p.construct(inputs,p.extend);times=[]
    for _ in range(5):
        p.gc.collect();out,c,r=profile(inputs);assert out==gold;times.append(r)
    med={k:median(r[k] for r in times) for k in times[0]};print(c,med);p.prev.save(p.prev.out/'ramsey38_positive_phase_profile.json',dict(sample_sha=p.prev.sha(p.P.read_bytes()),counts=c,median_ms=med,rounds_ms=times))
if __name__=='__main__':run()
