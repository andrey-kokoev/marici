"""Prospective vertex-veto evaluation. Compare exact nested pairs, not just verdicts."""
from ramsey38_endpoint_parity_veto import P as calibration,old,key,p,shared_index,candidates,lru_cache,permutations,Counter,sys
from ramsey38_local_edge_domains import geometry,vertex_links,reject
from time import perf_counter_ns
from statistics import median
P=p.prev.out/'ramsey38_vertex_veto_holdout_cases.json'

def freeze():
    prior={e['record']:e['root'] for path in (calibration,old,p.P) for e in p.json.loads(path.read_text())['entries']};cut=max(prior);seen=set();es=[]
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in prior:seen.add(key(*p.setup(p.graph(line.strip()),prior[i])))
            if i<=cut:continue
            g=p.graph(line.strip())
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,r,m=p.setup(g,u)
                if max(map(int.bit_count,r.values()))>4 or sum(s.bit_count()==2 for s in r.values())<2 or not any(p.setup(p.add(g,a),u)[2] for a in m):continue
                k=key(L,r,m)
                if k in seen:continue
                seen.add(k);es.append(dict(record=i,root=u));break
            if len(es)==32:break
    assert len(es)==32;p.prev.save(P,dict(after=cut,protocol='Graph-only eligibility as parity calibration; exclude keys of all three preceding samples.',entries=es))

def check():
    es=p.json.loads(P.read_text())['entries'];ids={e['record'] for e in es};words={};idx=shared_index();p.base.templates()
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in ids:words[i]=line.strip()
            if i>=max(ids):break
    def batch(mode):
        geometry.cache_clear();vertex_links.cache_clear();counts=Counter();pairs=set()
        for e in es:
            g=p.graph(words[e['record']]);u=e['root'];L,rows,_,dec,stage,_=p.prepare(g,u);_,rs,ms=p.setup(g,u)
            @lru_cache(None)
            def pool(req,bds):return {frozenset(ts) for bd in bds for ts in candidates(idx,L,req,set(map(dec,bd)))}
            for a in ms:
                r,S=stage((a,));x,v=a;rr={**rs,x:rs[x]|1<<L.index(v)}
                for b in p.setup(p.add(g,a),u)[2]:
                    q,T=stage(tuple(sorted((a,b))))
                    for j,k in permutations(rows,2):
                        src=tuple(S.get(frozenset([j]),()));dst=tuple(T.get(frozenset([j,k]),()))
                        if not src or not dst:continue
                        for B in pool(q,dst):
                            bad=mode!='direct' and reject(B,{dec(rs[x]),dec(rr[j])},{dec(s) for h,s in rr.items() if h!=j and s.bit_count()<4},{dec(s) for s in rr.values() if s.bit_count()==4},True)
                            if mode=='guard' and bad:continue
                            starts=pool(r,src);matches=[A for A in starts if A<B];pairs.update((e['record'],a,b,j,k,A,B) for A in matches)
                            if mode=='audit' and starts:
                                assert not (bad and matches);counts['feasible' if matches else 'rejected' if bad else 'missed']+=1
        return pairs,counts
    gold,c=batch('audit');rounds=[]
    for i in range(4):
        rr={}
        for mode in ['guard','direct'][::1 if i%2==0 else -1]:
            p.gc.collect();t=perf_counter_ns();res,_=batch(mode);rr[mode]=(perf_counter_ns()-t)/1e6;assert res==gold
        rounds.append(rr)
    out=dict(sample_sha=p.prev.sha(P.read_bytes()),counts=dict(c),request_pair_occurrences=len(gold),median_ms={k:median(r[k] for r in rounds) for k in rounds[0]},rounds_ms=rounds);print(out);p.prev.save(p.prev.out/'ramsey38_vertex_veto_holdout.json',out)
if __name__=='__main__':{'freeze':freeze,'check':check}[sys.argv[1]]()
