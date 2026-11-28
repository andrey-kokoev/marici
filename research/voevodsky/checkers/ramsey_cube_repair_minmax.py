"""Exact minimum hitting sets versus maximum disjoint demands. A demand is the set of individual repair links inside one blocking blue clique. Mutual triangle constraints are deliberately absent."""
from ramsey_cube_retention_floor import G,induced,D,json,combinations,Counter
from functools import lru_cache,reduce
from operator import or_

def bits(m):
    while m:
        b=m&-m;m-=b;yield b.bit_length()-1

def opt(ds):
    small=[]
    for d in sorted(ds,key=lambda d:(d.bit_count(),d)):
        if not any((e&d)==e for e in small):small.append(d)
    # Dominated supersets are unnecessary for cover; replace a packed superset with its subset without conflicts.
    touch={i:sum(1<<j for j,d in enumerate(small) if d>>i&1) for i in bits(reduce(or_,small))};allrows=(1<<len(small))-1
    @lru_cache(None)
    def cover(m):
        if not m:return ()
        d=small[(m&-m).bit_length()-1];return min(((i,)+cover(m&~touch[i]) for i in bits(d)),key=len)
    clash=[reduce(or_,(touch[i] for i in bits(d))) for d in small]
    @lru_cache(None)
    def pack(m):
        if not m:return ()
        j=(m&-m).bit_length()-1;yes=(j,)+pack(m&~clash[j]);return yes if not m&(clash[j]^(1<<j)) else max(yes,pack(m^(1<<j)),key=len)
    c=cover(allrows);pk=[small[j] for j in pack(allrows)];assert all(any(d>>i&1 for i in c) for d in ds) and all(not x&y for x,y in combinations(pk,2));return c,pk,small

def audit():
    old=json.loads((D.parent/'ramsey_cube_reverse_mixed.json').read_text());V=old['core_labels'];a=induced(G,V);out=[];hist=Counter()
    for trial in old['per_cut']:
        if not trial['counts'].get('each_breakable'):continue
        u,v=trial['removed'];b=a[:];b[u]^=1<<v;b[v]^=1<<u;I=[0]
        for i,n in enumerate(b):I.extend([s|1<<i for s in I if not n&s]);
        Q=[q for q in I if q.bit_count()==7];O=[q for q in I if q.bit_count()==8];E=[(i,j) for i,j in combinations(range(26),2) if not b[i]&((1<<j)|b[j]) and (i,j)!=(u,v)];ends=[1<<i|1<<j for i,j in E];dem={q:sum(1<<j for j,e in enumerate(ends) if q&e==e) for q in O+Q};ncase=0
        for s in Q:
            allowed=sum(1<<j for j,e in enumerate(ends) if s&e!=e);Dq={dem[q]&allowed:q for q in O+[q for q in Q if not q&s]}
            if 0 in Dq:continue
            ncase+=1;c,pk,small=opt(Dq);hist[len(pk),len(c)]+=1;out.append(dict(remove=[u,v],row=list(bits(s)),packing=len(pk),cover=len(c),cover_links=[E[i] for i in c],packed_cliques=[list(bits(Dq[d])) for d in pk],minimal_demands=[[E[i] for i in bits(d)] for d in small]))
        assert ncase==trial['counts']['each_breakable']
    assert len(out)==90;print(sorted(hist.items()));(D.parent/'ramsey_cube_repair_minmax.json').write_text(json.dumps(dict(core_labels=V,distribution=[dict(packing=p,cover=c,cases=n) for (p,c),n in sorted(hist.items())],cases=out),indent=2)+'\n')
if __name__=='__main__':audit()
