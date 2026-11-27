"""Build the labelled seven-column ball atlas from closure, then time Boolean certification."""
import sys
from itertools import permutations,combinations
from functools import lru_cache
from unittest.mock import patch
from statistics import median
from time import perf_counter_ns as now
import ramsey38_certified_route_pipeline as p
from ramsey38_interior_edge_trap_census import run as census

cells=list(combinations(range(7),4));bits={t:1<<i for i,t in enumerate(cells)}
def build():
    reps=[];census(35,representatives=reps);assert len(reps)==183
    rows=[[i for i in range(35) if m>>i&1] for m in reps];atlas=set()
    for perm in permutations(range(7)):
        image=[bits[tuple(sorted(perm[i] for i in t))] for t in cells];atlas.update(sum(image[i] for i in row) for row in rows)
    return atlas

def encoder():
    @lru_cache(None)
    def index(labels):return {frozenset(labels[i] for i in t):v for t,v in bits.items() if max(t)<len(labels)}
    def encode(ts):
        ix=index(tuple(sorted(set().union(*ts))));return sum(ix[t] for t in ts)
    return encode

def run():
    t=now();atlas=build();cold=(now()-t)/1e6;entries=p.json.loads(p.P.read_text())['entries'];ids={e['record'] for e in entries};words={}
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in ids:words[i]=line.strip()
            if i>=max(ids):break
    inputs=[(words[e['record']],e['root']) for e in entries];p.base.templates();peel=p.Peeler;ref=peel(True);enc=encoder();checks=[]
    def check(ts):
        ok=enc(ts) in atlas;assert ok==bool(ref(ts));checks.append(ok);return ok
    with patch.object(p,'Peeler',lambda _:check):gold=p.construct(inputs,p.greedy)
    del ref
    def lookup(_):
        encode=encoder();return lambda ts:encode(ts) in atlas
    rounds=[]
    for i in range(6):
        r={}
        for k,f in [('atlas',lookup),('peel',peel)][::1 if i%2==0 else -1]:
            with patch.object(p,'Peeler',f):
                p.gc.collect();t=now();out=p.construct(inputs,p.greedy);r[k]=(now()-t)/1e6
            assert out==gold
        rounds.append(r);print(r,flush=True)
    med={k:median(r[k] for r in rounds) for k in rounds[0]};z=dict(sample_sha=p.prev.sha(p.P.read_bytes()),atlas_masks=len(atlas),atlas_set_and_int_bytes=sys.getsizeof(atlas)+sum(map(sys.getsizeof,atlas)),build_ms=cold,candidate_checks=len(checks),accepted=sum(checks),pairs=sum(map(len,gold[0])),median_ms=med,rounds_ms=rounds);print(z);p.prev.save(p.prev.out/'ramsey38_shell_lookup_trial.json',z)
if __name__=='__main__':run()
