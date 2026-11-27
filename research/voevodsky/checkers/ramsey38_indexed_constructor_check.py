"""Regression for the callable indexed constructor, without patching any dependencies."""
from ramsey38_boundary_ball_index import construct_marked_routes,shared_index,p,now
from ramsey38_boundary_index_holdout import P as holdout
from ramsey38_append_holdout import attaches


def run():
    sets=[p.json.loads(path.read_text())['entries'] for path in (p.P,holdout)];ids={e['record'] for es in sets for e in es};words={}
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in ids:words[i]=line.strip()
            if i>=max(ids):break
    p.base.templates();shared_index.cache_clear();res=[]
    for es in sets:
        inputs=[(words[e['record']],e['root']) for e in es];start=now();got=construct_marked_routes(inputs);ms=(now()-start)/1e6
        assert got==construct_marked_routes(inputs,reference=True)
        for routes in got[0]:
            for (a,b),order in routes.items():
                for t in order:assert t in b-a and attaches(a,t);a=a|{t}
                assert a==b
        res.append(dict(roots=len(es),pairs=sum(map(len,got[0])),comparisons=got[1],nested=got[2],indexed_ms=ms))
    assert shared_index.cache_info().misses==1;print(res);p.prev.save(p.prev.out/'ramsey38_indexed_constructor_check.json',dict(batches=res,sample_sha=[p.prev.sha(path.read_bytes()) for path in (p.P,holdout)]))
if __name__=='__main__':run()
