"""Filter arbitrary proper cell selections by exposure, connected edge links and spherical boundary."""
from ramsey38_endpoint_parity_veto import P,p,shared_index,candidates,permutations,combinations,lru_cache,Counter,veto

@lru_cache(maxsize=256)
def table(B,L):
    cells=tuple(B);n=len(cells);full=(1<<(1<<n))-1;on=[full//((1<<(1<<i))+1)<<(1<<i) for i in range(n)];occ={};bd={};link={};edges=list(map(frozenset,combinations(L,2)));tri=list(map(frozenset,combinations(L,3)));tri_on={}
    for f in cells:occ[f]=on[cells.index(f)]
    for f in tri:
        v=0
        for t,z in zip(cells,on):
            if f<=t:v^=z
        tri_on[f]=v
    for s in [frozenset()]+[frozenset([v]) for v in L]+edges+tri:
        a=b=0
        for t,z in zip(cells,on):
            if s<=t:a|=z
        for f,z in tri_on.items():
            if s<=f:b|=z
        occ[s]=a;bd[s]=b
    for s in edges:
        inds=[i for i,t in enumerate(cells) if s<=t];bad=0
        for mask in range(1,1<<len(inds)):
            chosen=[cells[i] for j,i in enumerate(inds) if mask>>j&1];seen={chosen[0]}
            for _ in chosen:seen.update(t for t in chosen if any(len(t&u)>=3 for u in tuple(seen)))
            if len(seen)==len(chosen):continue
            bits=full
            for j,i in enumerate(inds):bits&=on[i] if mask>>j&1 else ~on[i]
            bad|=bits
        link[s]=full^bad
    return full,occ,bd,link,cells,tri_on

def run(local=False,vertices=False):
    from ramsey38_local_edge_domains import reject
    es=p.json.loads(P.read_text())['entries'];ids={e['record'] for e in es};words={};cnt=Counter();idx=shared_index();examples={}
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in ids:words[i]=line.strip()
            if i>=max(ids):break
    spheres={frozenset(bd) for bd,_ in p.base.templates()}
    for e in es:
        g=p.graph(words[e['record']]);u=e['root'];L,rows,_,dec,stage,_=p.prepare(g,u);_,rs,ms=p.setup(g,u)
        @lru_cache(None)
        def pool(req,bds):return {frozenset(ts) for bd in bds for ts in candidates(idx,L,req,set(map(dec,bd)))}
        for a in ms:
            r,S=stage((a,));x,v=a;rr={**rs,x:rs[x]|1<<L.index(v)}
            for b in p.setup(p.add(g,a),u)[2]:
                q,T=stage(tuple(sorted((a,b))))
                for j,k in permutations(rows,2):
                    A=pool(r,tuple(S.get(frozenset([j]),())))
                    if not A:continue
                    for B in pool(q,tuple(T.get(frozenset([j,k]),()))):
                        yes=any(M<B for M in A);buried={dec(rs[x]),dec(rr[j])};exposed={dec(s) for h,s in rr.items() if h!=j and s.bit_count()<4};required={dec(s) for s in rr.values() if s.bit_count()==4};reason=reject(B,buried,exposed,required) if local else veto(B,buried,exposed,required,True)
                        if vertices and not reason and reject(B,buried,exposed,required,True):reason='incompatible vertex links'
                        if not local and not reason:
                            full,occ,bd,link,cells,tri=table(B,tuple(L));live=(full>>1)&~1
                            for s in buried:live&=occ[s]&~bd[s]
                            for s in exposed:live&=bd[s]
                            for s in required:live&=occ.get(s,0)
                            if not live:reason='proper selection and all row tests'
                            for allowed in link.values():live&=allowed
                            if not live:reason=reason or 'disconnected edge link unavoidable'
                            ok=False
                            while live and not ok:
                                h=live&-live;live^=h;surface=frozenset(sum(1<<L.index(v) for v in f) for f,t in tri.items() if t&h);ok=surface in spheres
                            if not ok:reason=reason or 'no spherical boundary'
                        assert not(reason and yes);key=reason or ('feasible' if yes else 'missed negative');cnt[key]+=1;examples.setdefault(key,dict(record=e['record'],root=u,moves=[a,b],goal=[j,k],end=p.faces(B)))
    print(cnt);p.prev.save(p.prev.out/('ramsey38_endpoint_vertex_veto.json' if vertices else 'ramsey38_endpoint_interval_veto.json' if local else 'ramsey38_endpoint_link_diagnosis.json'),dict(source_sha=p.prev.sha(P.read_bytes()),counts=dict(cnt),examples=examples))
if __name__=='__main__':
    import sys
    run('--local' in sys.argv or '--vertices' in sys.argv,'--vertices' in sys.argv)
