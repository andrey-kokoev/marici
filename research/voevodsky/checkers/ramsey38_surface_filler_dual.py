"""Three independent traversals up to two attachments. Never identify starting meshes by boundary."""
from ramsey38_middle_choice_holdout import P,R,prev,json,graph,setup,add,boundary
from ramsey38_three_releases import templates
from itertools import combinations,permutations
from collections import Counter,defaultdict
from functools import lru_cache
from statistics import median
from time import perf_counter_ns

@lru_cache(None)
def geometry():
    tri=sorted(sum(1<<x for x in f) for f in combinations(range(7),3));cells=sorted(sum(1<<x for x in f) for f in combinations(range(7),4));facebits={f:1<<i for i,f in enumerate(tri)};delta=[sum(b for f,b in facebits.items() if t&f==f) for t in cells];enc=lambda fs:sum(facebits[f] for f in fs);spheres={enc(fs):cl for fs,cl in templates()};
    # For each possible attached cell and subset of its triangles that are
    # on the starting surface, forbid old cells with a stray edge/point contact.
    blockers=[]
    for t in cells:
        fs=[f for f in tri if f&t==f];tab={}
        for k in (1,2,3):
            for hits in combinations(fs,k):tab[enc(hits)]=sum(1<<i for i,u in enumerate(cells) if not any((u&t)&h==(u&t) for h in hits))
        blockers.append(tab)
    return cells,enc,delta,spheres,blockers

def run():
    cells,enc,delta,spheres,blockers=geometry();cases=[];ref=json.loads(R.read_text());it=iter(ref['results']);assert ref['prediction_sha']==prev.sha(P.read_bytes())
    for e in json.loads(P.read_text())['cases']:
        g=graph(e['word']);L=sorted(g[e['u']]);mask=lambda f:sum(1<<L.index(w) for w in f)
        for d in e['requests']:
            z=next(it);assert z['record']==e['record'] and z['goal']==d['goal'] and z['moves']==d['moves'];h=g;buried=[]
            for x,v in d['moves']:
                _,rs,_=setup(h,e['u']);buried.append(rs[x]);h=add(h,(x,v))
            _,rs,_=setup(h,e['u']);goal=set(d['goal']);ends={b for b,cl in spheres.items() if not set(buried)&cl and {j for j,s in rs.items() if s.bit_count()<4 and s not in cl}==goal};car=[sum(1<<i for i,t in enumerate(cells) if s&t==s) for s in set(rs.values())];starts=[]
            for pool in d['pool']:
                ts=set(map(frozenset,pool));starts.append((sum(1<<cells.index(mask(t)) for t in ts),enc(map(mask,boundary(ts)))))
            cases.append((starts,ends,car,z['ok']))
    benchmark(cases,make_search(delta,spheres,blockers))

def make_search(delta,spheres,blockers):
    def search(case,mode):
        starts,ends,car,_=case;out=set();nodes=Counter();by=defaultdict(list)
        for j,(m,b) in enumerate(starts):by[b].append((j,m))
        def step(m,b,i):
            ban=blockers[i].get(b&delta[i]);return ban is not None and not m&(ban|1<<i)
        def accept(j,m,b,path):
            if b in ends and all(m&c for c in car):out.add((j,m,b,path))
        if mode=='back':
            def rev(b,tail):
                nodes['surface']+=1
                if tail:
                    for j,m in by.get(b,()):
                        cur=b
                        for i in tail:
                            nodes['replay']+=1
                            if not step(m,cur,i):break
                            m|=1<<i;cur^=delta[i]
                        else:accept(j,m,cur,tail)
                if len(tail)<2:
                    for i,v in enumerate(delta):
                        other=b^v
                        if other in spheres and i not in tail:rev(other,(i,)+tail)
            for b in ends:rev(b,())
        else:
            if mode=='join':
                reach=set(ends)
                for b in ends:
                    nodes['surface']+=1;reach.update(b^v for v in delta if b^v in spheres)
            def forward(j,m,b,path):
                nodes['filler']+=1
                if path:accept(j,m,b,path)
                if len(path)==2:return
                for i,v in enumerate(delta):
                    nb=b^v
                    if mode=='join' and nb not in (ends if path else reach):continue
                    if step(m,b,i):forward(j,m|1<<i,nb,path+(i,))
            for j,(m,b) in enumerate(starts):forward(j,m,b,())
        return out,nodes
    return search

def benchmark(cases,search):
    modes=('forward','back','join');gold=[];summary={};traces=[]
    for mode in modes:
        allr=[];nodes=Counter()
        for idx,c in enumerate(cases):
            r,n=search(c,mode);nodes.update(n);allr.append(r)
            if mode=='forward':assert {v[0] for v in r}==set(c[3]);traces.append(sorted(r))
        if mode=='forward':gold=allr
        else:assert allr==gold
        summary[mode]=dict(nodes)
    times=[]
    for order in permutations(modes):
        rnd={}
        for k in order:
            start=perf_counter_ns();ans=[search(c,k)[0] for c in cases];rnd[k]=(perf_counter_ns()-start)/1e6;assert ans==gold
        times.append(rnd)
    med={k:median(z[k] for z in times) for k in modes};counts=dict(requests=len(cases),middle_occurrences=sum(len(c[0]) for c in cases),orders=sum(map(len,gold)),pairs=sum(len({r[:3] for r in rs}) for rs in gold),goals=sum(bool(rs) for rs in gold));print(counts,summary,med);prev.save(prev.out/'ramsey38_surface_filler_dual.json',dict(counts=counts,visits=summary,median_ms=med,batch_ms=times,solutions=traces,scope='Cell and triangle bit indices in increasing numerical 7-bit mask order. Timers exclude common geometry, pool and target-compatible sphere preparation, include traversal-specific reachability. Paths of length 1 or 2 only.'))
if __name__=='__main__':run()
