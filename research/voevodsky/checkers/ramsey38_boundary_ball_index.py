"""Retrieve all shellable fillers of an exact boundary, not just one witness."""
from collections import defaultdict,Counter
from functools import lru_cache
from itertools import combinations
from unittest.mock import patch
from statistics import median
from time import perf_counter_ns as now
from ramsey38_shell_lookup_trial import build,encoder,cells,p

triangles=list(combinations(range(7),3))
def index(atlas):
    face=[sum(1<<triangles.index(f) for f in combinations(t,3)) for t in cells]+[0]*5
    tables=[]
    for k in range(0,35,8):
        v=[0]
        for f in face[k:k+8]:v += [x^f for x in v]
        tables.append(v)
    a,b,c,d,e=tables;idx=defaultdict(list)
    for m in atlas:idx[a[m&255]^b[m>>8&255]^c[m>>16&255]^d[m>>24&255]^e[m>>32]].append(m)
    return idx

@lru_cache(maxsize=64)
def coords(L):
    ts=[frozenset(L[i] for i in t) for t in cells];bd={frozenset(L[i] for i in f):1<<j for j,f in enumerate(triangles)};carrier={frozenset(s):sum(1<<i for i,t in enumerate(ts) if set(s)<=t) for k in range(5) for s in combinations(L,k)};return ts,bd,carrier

def candidates(idx,L,req,boundary):
    ts,bd,car=coords(tuple(L));rr=[car[s] for s in req];bucket=idx.get(sum(bd[f] for f in boundary),())
    for m in bucket:
        if all(m&h for h in rr):yield [t for j,t in enumerate(ts) if m>>j&1]

@lru_cache(maxsize=1)
def shared_index():
    """Retain boundary buckets across batches; the intermediate atlas is disposable."""
    return index(build())


def construct_marked_routes(inputs,*,reference=False):
    """Graph6 word/root pairs, seven-column catalogue edge-release protocol only."""
    if reference:return p.construct(inputs,p.extend)
    idx=shared_index()
    return p.construct(inputs,p.greedy,certified_fillers=lambda L,r,b:candidates(idx,L,r,b))


def run(sample=p.P,result='ramsey38_boundary_ball_index.json'):
    t=now();atlas=build();build_ms=(now()-t)/1e6;t=now();idx=index(atlas);idx_ms=(now()-t)/1e6;enc=encoder();ref=p.parallel_chains;entries=p.json.loads(sample.read_text())['entries'];ids={e['record'] for e in entries};words={}
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in ids:words[i]=line.strip()
            if i>=max(ids):break
    inputs=[(words[e['record']],e['root']) for e in entries];p.base.templates();counts=Counter()
    def get(L,r,b):return candidates(idx,L,r,b)
    def checked(L,r,b):
        hits=list(get(L,r,b));gold=[ts for ts in ref(L,r,b) if enc(ts) in atlas];assert Counter(map(frozenset,hits))==Counter(map(frozenset,gold));counts['queries']+=1;counts['hits']+=len(hits);counts['empty_queries']+=not hits;return hits
    with patch.object(p,'Peeler',lambda _:lambda ts:True),patch.object(p,'parallel_chains',checked):gold=p.construct(inputs,p.greedy)
    rounds=[]
    for i in range(6):
        r={}
        for k in ['index','atlas'][::1 if i%2==0 else -1]:
            encode=encoder();coords.cache_clear()
            with patch.object(p,'Peeler',lambda _: (lambda ts:True) if k=='index' else (lambda ts:encode(ts) in atlas)),patch.object(p,'parallel_chains',get if k=='index' else ref):
                p.gc.collect();t=now();out=p.construct(inputs,p.greedy);r[k]=(now()-t)/1e6
            assert out==gold
        rounds.append(r)
    med={k:median(r[k] for r in rounds) for k in rounds[0]};out=dict(source_sha=p.prev.sha(sample.read_bytes()),roots=len(inputs),roots_with_routes=sum(map(bool,gold[0])),atlas_build_ms=build_ms,index_additional_build_ms=idx_ms,boundaries=len(idx),max_bucket=max(map(len,idx.values())),counts=dict(counts),pairs=sum(map(len,gold[0])),median_ms=med,rounds_ms=rounds);print(out);p.prev.save(p.prev.out/result,out)
if __name__=='__main__':run()
