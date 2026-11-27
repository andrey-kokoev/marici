"""Three endpoint probes per root. Redirect after an observed conflict; never inspect unprobed starts."""
from ramsey38_vertex_veto_holdout import P as prior,calibration,old,key,p,shared_index,candidates,lru_cache,permutations,Counter,sys
from ramsey38_local_conflict_certificates import shrink,predicates
from ramsey38_append_holdout import attaches
P=p.prev.out/'ramsey38_conflict_choice_cases.json';R=p.prev.out/'ramsey38_conflict_choice_results.json'
protocol='First 64 new eligible roots after prior batch. Budget 3 distinct (script,goal,final ball) containment probes. Baseline lexical. After failed probe only, shrink a local rejection to a core. Guided ranks untried options by count of learned cores retained in their first-stage requirements, breaking ties lexically. No trial starts queried during listing/ranking. Same candidate list and first probe. Independent unlimited feasibility census.'
FRESH=p.prev.out/'ramsey38_confirmed_choice_cases.json'
def freeze(confirmed=False):
    seen=set();es=[];prev={e['record']:e['root'] for path in ((P,) if confirmed else ())+ (prior,calibration,old,p.P) for e in p.json.loads(path.read_text())['entries']};cut=max(prev)
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in prev:seen.add(key(*p.setup(p.graph(line.strip()),prev[i])))
            if i<=cut:continue
            g=p.graph(line.strip())
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,r,m=p.setup(g,u)
                if max(map(int.bit_count,r.values()))>4 or sum(s.bit_count()==2 for s in r.values())<2 or not any(p.setup(p.add(g,a),u)[2] for a in m):continue
                k=key(L,r,m)
                if k in seen:continue
                seen.add(k);es.append(dict(record=i,root=u));break
            if len(es)==64:break
    assert len(es)==64;p.prev.save(FRESH if confirmed else P,dict(after=cut,protocol=(protocol+' Confirmed variant: scan in lexical order, skipping only after a retained learned core rejects the NEW endpoint. At most 3 exact probes. Validate all skips post hoc.' if confirmed else protocol),entries=es))

def check(sample=P,confirmed=False,clock=False):
    es=p.json.loads(sample.read_text())['entries'];ids={e['record'] for e in es};words={};idx=shared_index();stats=Counter();report=[]
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in ids:words[i]=line.strip()
            if i>=max(ids):break
    for e in es:
        g=p.graph(words[e['record']]);u=e['root'];L,rows,_,dec,stage,_=p.prepare(g,u);_,rs,ms=p.setup(g,u);opts=[]
        @lru_cache(None)
        def pool(r,bds):return {frozenset(ts) for bd in bds for ts in candidates(idx,L,r,set(map(dec,bd)))}
        for a in sorted(ms):
            r,S=stage((a,));x,v=a;rr={**rs,x:rs[x]|1<<L.index(v)}
            for b in sorted(p.setup(p.add(g,a),u)[2]):
                q,T=stage(tuple(sorted((a,b))))
                for j,k in sorted(permutations(rows,2)):
                    src=tuple(S.get(frozenset([j]),()));dst=tuple(T.get(frozenset([j,k]),()))
                    if not src or not dst:continue
                    atoms=tuple(sorted({('bury',dec(rs[x]))}|{('bury' if h==j else 'carry' if s.bit_count()==4 else 'expose',dec(s)) for h,s in rr.items()},key=lambda a:(a[0],sorted(a[1]))))
                    for B in sorted(pool(q,dst),key=p.faces):opts.append((a,b,j,k,r,src,atoms,B))
        def probe(i):
            *_,r,src,atoms,B=opts[i];return min((A for A in pool(r,src) if A<B),key=p.faces,default=None)
        skipped=[];tests=0
        def arm(guided,budget=3):
            nonlocal tests
            tried=[];cores=[]
            while len(tried)<min(budget,len(opts)):
                if confirmed and guided:
                    for i in range(len(opts)):
                        if i in tried or i in skipped:continue
                        atoms,B=opts[i][-2:];blocked=False
                        for c in cores:
                            if c<=set(atoms):
                                tests+=1
                                if predicates(B,c):blocked=True;break
                        if not blocked:break
                        skipped.append(i)
                    else:break
                elif not guided:i=len(tried)
                else:i=min((i for i in range(len(opts)) if i not in tried),key=lambda i:sum(c<=set(opts[i][-2]) for c in cores))
                tried.append(i);A=probe(i);a,b,j,k,_,_,atoms,B=opts[i]
                if A is not None:
                    order=p.greedy(A,B);M=A
                    for t in order:assert t in B-M and attaches(M,t);M=M|{t}
                    assert M==B;return tried,dict(moves=[a,b],goal=[j,k],start=p.faces(A),append=[sorted(t) for t in order])
                if guided and len(tried)<3 and predicates(B,atoms):cores.append(set(shrink(B,atoms)))
            return tried,None
        if clock:
            from time import perf_counter_ns
            from ramsey38_local_edge_domains import geometry,vertex_links
            from ramsey38_boundary_ball_index import coords
            samples=[]
            for rep in range(6):
                timing={};wins={};attempts={}
                for mode in ['guided','direct'][::1 if rep%2==0 else -1]:
                    skipped.clear();tests=0;pool.cache_clear();coords.cache_clear();geometry.cache_clear();vertex_links.cache_clear();shrink.cache_clear()
                    start=perf_counter_ns();tr,w=arm(mode=='guided',3 if mode=='guided' else len(opts));timing[mode]=perf_counter_ns()-start
                    wins[mode]=bool(w);attempts[mode]=len(tr)
                samples.append(dict(ns=timing,success=wins,attempts=attempts,direct_on_time=wins['direct'] and timing['direct']<=timing['guided']))
            report.append(dict(**e,rounds=samples));continue
        t1,w1=arm(False);t2,w2=arm(True);yes=any(probe(i) is not None for i in range(len(opts)));stats.update(roots=1,eligible=bool(opts),feasible=yes,baseline=bool(w1),guided=bool(w2),gained=bool(w2 and not w1),lost=bool(w1 and not w2),changed=t1!=t2);report.append(dict(**e,options=len(opts),feasible=yes,baseline=t1,guided=t2,baseline_route=w1,guided_route=w2))
        if confirmed:
            assert not w1 or w2;assert all(probe(i) is None for i in skipped);report[-1].update(skipped=skipped,core_tests=tests);stats.update(skipped=len(skipped),core_tests=tests)
    if clock:
        from statistics import median
        ref=p.json.loads((p.prev.out/'ramsey38_confirmed_choice_fresh.json').read_text())['roots'];assert all(z['record']==y['record'] and all(r['success']=={'direct':y['feasible'],'guided':bool(y['guided_route'])} for r in z['rounds']) for z,y in zip(report,ref,strict=True))
        totals=[dict(on_time=sum(z['rounds'][i]['direct_on_time'] for z in report),**{k:sum(z['rounds'][i]['ns'][k] for z in report)/1e6 for k in ['direct','guided']}) for i in range(6)];print(totals);p.prev.save(p.prev.out/'ramsey38_confirmed_choice_clock.json',dict(sample_sha=p.prev.sha(sample.read_bytes()),protocol='Selection after common option listing; fresh start-pool, coordinates and local caches per root/arm. Direct first success counts only if finished within paired guided elapsed time on same root. Six alternating orders. Includes route replay.',totals=totals,roots=report));return
    dest=p.prev.out/('ramsey38_confirmed_choice_'+('fresh' if sample==FRESH else 'replay')+'.json') if confirmed else R
    print(stats);p.prev.save(dest,dict(source_sha=p.prev.sha(sample.read_bytes()),stats=dict(stats),roots=report))
if __name__=='__main__':{'freeze':freeze,'check':check,'freeze-confirmed':lambda:freeze(True),'replay-confirmed':lambda:check(P,True),'fresh-confirmed':lambda:check(FRESH,True),'clock':lambda:check(FRESH,True,True)}[sys.argv[1]]()
