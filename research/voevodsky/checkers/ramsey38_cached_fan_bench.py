"""Paired full-batch replay with exact leaf checks outside timed regions."""
from ramsey38_fan_lookahead_trial import F,R,prev,json,inputs,search
from ramsey38_cached_fan_search import search as cached
from time import perf_counter_ns
from statistics import median
import gc,sys,platform

def run():
    old=json.loads(R.read_text());assert old['sample_sha']==prev.sha(F.read_bytes());cases=[]
    for e in json.loads(F.read_text())['cases']:
        b,_,x,rs,v=inputs(e);S=rs[x];rs[x]|=v;labs=sorted(b[e['u']]);dec=lambda m:frozenset(w for i,w in enumerate(labs) if m>>i&1)
        for d in e['sample']:cases.append((labs,set(map(dec,d['bd'])),set(map(dec,rs.values()))|{dec(S)|{d['tip']}}))
    gold=[sorted(search(*c,None,True,True)['leaves']) for c in cases];modes=dict(online=lambda c:search(*c,None,True),cached=lambda c:cached(*c))
    def batch(k):
        fn=modes[k];gc.collect();t=perf_counter_ns();a=[fn(c) for c in cases];dt=(perf_counter_ns()-t)/1e6
        assert all(sorted(z['leaves'])==g and z['nodes']==d['online' if k=='online' else 'forward'] for z,g,d in zip(a,gold,old['results'],strict=True));return dt
    for k in modes:batch(k)
    rounds=[{k:batch(k) for k in (list(modes) if i%2==0 else list(reversed(modes)))} for i in range(12)];ratios=[r['cached']/r['online'] for r in rounds];out=dict(sample_sha=old['sample_sha'],python=sys.version,platform=platform.platform(),protocol='12 alternating paired batches after warmup. Fresh per-search cache. Setup and result construction timed; validation, input decoding and forced GC outside timer.',rounds_ms=rounds,median_ms={k:median(r[k] for r in rounds) for k in modes},median_ratio=median(ratios),range_ratio=[min(ratios),max(ratios)]);print(out['median_ms'],out['median_ratio'],out['range_ratio']);prev.save(prev.out/'ramsey38_cached_fan_benchmark.json',out)
if __name__=='__main__':run()
