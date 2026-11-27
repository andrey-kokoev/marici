"""Paired wall-time benchmark of the two existing search modes; no file I/O in timer."""
from ramsey38_fan_lookahead_trial import F,R,prev,json,inputs,search
import gc,platform,sys
from time import perf_counter_ns
from statistics import median

def run():
    replay=json.loads(R.read_text());assert replay['sample_sha']==prev.sha(F.read_bytes());cases=[]
    for e in json.loads(F.read_text())['cases']:
        b,_,x,rs,v=inputs(e);S=rs[x];rs[x]|=v;labs=sorted(b[e['u']]);dec=lambda m:frozenset(w for i,w in enumerate(labs) if m>>i&1)
        for d in e['sample']:
            cases.append((labs,set(map(dec,d['bd'])),set(map(dec,rs.values()))|{dec(S)|{d['tip']}},None,True))
    def batch(mode):
        gc.collect();start=perf_counter_ns();ans=[search(*c,mode) for c in cases];elapsed=(perf_counter_ns()-start)/1e6
        assert all(z['nodes']==d['forward' if mode else 'online'] and len(z['leaves'])==d['leaves'] for z,d in zip(ans,replay['results'],strict=True));return elapsed
    for mode in (False,True):batch(mode)
    rounds=[]
    for i in range(12):
        order=(False,True) if i%2==0 else (True,False);r={('lookahead' if m else 'online'):batch(m) for m in order};rounds.append(r)
    ratios=[r['lookahead']/r['online'] for r in rounds];out=dict(sample_sha=replay['sample_sha'],python=sys.version,platform=platform.platform(),machine=platform.machine(),protocol='One warm-up per mode. 12 paired full-sample repetitions, alternating first mode. GC collect outside timer; normal GC inside. Wall ms include search setup and result construction; exclude decoding, validation and I/O.',rounds_ms=rounds,median_ms={k:median(r[k] for r in rounds) for k in rounds[0]},median_ratio=median(ratios),ratio_range=[min(ratios),max(ratios)]);print(out['median_ms'],out['median_ratio'],out['ratio_range']);prev.save(prev.out/'ramsey38_fan_lookahead_timing.json',out)
if __name__=='__main__':run()
