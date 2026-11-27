"""Prospective three-way replay, counterbalanced by all six batch orders."""
from ramsey38_fan_lookahead_trial import F,freeze,inputs,json,prev,search
from ramsey38_cached_fan_search import search as cached
from pathlib import Path
from itertools import permutations
from statistics import median
from time import perf_counter_ns
import gc,sys,platform
H=prev.out/'ramsey38_cached_holdout_sample.json';R=prev.out/'ramsey38_cached_holdout_replay.json'
protocol='First three canonically novel marked promotions after record 237, all previous early sign survivors. Frozen code; compare identical assignments and nodes per case; time entire batches in all six mode orders twice, after one warmup each; no I/O, gc.collect or validation in timers.'
def hashes():return {n:prev.sha(Path(__file__).with_name(n).read_bytes()) for n in ['ramsey38_cached_holdout.py','ramsey38_partial_fan_prune.py','ramsey38_cached_fan_search.py']}
def run():
    data=json.loads(H.read_text());assert data['source_hashes']==hashes() and data['protocol']==protocol;cases=[];cases_meta=[]
    for e in data['cases']:
        b,_,x,rs,v=inputs(e);S=rs[x];rs[x]|=v;labs=sorted(b[e['u']]);dec=lambda m:frozenset(w for i,w in enumerate(labs) if m>>i&1)
        for d in e['sample']:
            cases.append((labs,set(map(dec,d['bd'])),set(map(dec,rs.values()))|{dec(S)|{d['tip']}}));cases_meta.append(dict(record=e['record'],root=e['u'],**d))
    modes=dict(online=lambda c:search(*c,None,True),full=lambda c:search(*c,None,True,True),cached=lambda c:cached(*c));gold=[]
    def batch(k):
        fn=modes[k];gc.collect();start=perf_counter_ns();ans=[fn(c) for c in cases];dt=(perf_counter_ns()-start)/1e6
        if not gold:gold.extend(sorted(a['leaves']) for a in ans)
        for d,a,g in zip(cases_meta,ans,gold,strict=True):
            assert sorted(a['leaves'])==g and d.setdefault(k,a['nodes'])==a['nodes'];d['survivors']=len(g)
            if 'cached' in d:assert d['cached']==d['full']
        return dt
    for k in modes:batch(k)
    rounds=[{k:batch(k) for k in order} for order in list(permutations(modes))*2];ms={k:median(r[k] for r in rounds) for k in modes};ratios=[r['cached']/r['online'] for r in rounds];nodes={k:sum(d[k] for d in cases_meta) for k in modes};total=sum(map(len,gold));print(len(cases),total,nodes,ms,min(ratios),median(ratios),max(ratios));prev.save(R,dict(sample_sha=prev.sha(H.read_bytes()),rounds_ms=rounds,median_ms=ms,nodes=nodes,survivors=total,cases=cases_meta,platform=platform.platform(),python=sys.version))
if __name__=='__main__':
    if sys.argv[1]=='freeze':freeze(237,(F,),H,protocol,dict(source_hashes=hashes()))
    elif sys.argv[1]=='run':run()
