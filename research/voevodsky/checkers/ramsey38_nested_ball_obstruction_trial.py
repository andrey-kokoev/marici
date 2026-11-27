"""Select nested genuine balls before testing whether there is any relative shelling."""
from ramsey38_relative_peel_bench import P as prior,prev,json,sys,graph,setup,gzip,add,key,prepare,faces,shelling,extend,attaches,Peeler,Counter
from ramsey38_surface_fiber_profile import parallel_chains
from functools import lru_cache
P=prev.out/'ramsey38_nested_ball_obstruction_sample.json';R=prev.out/'ramsey38_nested_ball_obstruction_check.json'
protocol='After 257403 through 290000, first 8 distinct marked roots with a legal two-promotion sequence and a strict nested pair of endpoint-certified stage balls (one edge target hidden then two). Exclude previous relative benchmark roots by canonical key; first eligible root per record. Freeze all such pairs, then also every shellable nonempty proper submesh of each distinct retained final ball as a separate stress stratum. Neither extension direction used for selection. Seven original labels only.'
def freeze():
    prior_roots={e['record']:e['u'] for e in json.loads(prior.read_text())['cases']};seen=set();entries=[];screened=0
    with gzip.open(prev.catalogue,'rt') as fp:
        for i,line in enumerate(fp,1):
            if i in prior_roots:seen.add(key(*setup(graph(line.strip()),prior_roots[i])))
            if i<=257403:continue
            if i>290000:break
            w=line.strip();g=graph(w)
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,rs,ms=setup(g,u)
                if len(ms)<2 or max(map(int.bit_count,rs.values()))>4 or sum(s.bit_count()==2 for s in rs.values())<2:continue
                scripts=[(a,b) for a in ms for b in setup(add(g,a),u)[2]]
                if not scripts:continue
                k=key(L,rs,ms)
                if k in seen:continue
                seen.add(k);screened+=1;_,_,_,dec,stage,_=prepare(g,u);pairs=set();engine=Peeler(True)
                @lru_cache(None)
                def balls(req,bd):return [frozenset(ts) for ts in parallel_chains(L,req,set(map(dec,bd))) if engine(ts)]
                for a,b in scripts:
                    r,S=stage((a,));q,T=stage(tuple(sorted((a,b))))
                    for H,bds in T.items():
                        ends=[B for bd in bds for B in balls(q,bd)]
                        for j in H:
                            for bd in S.get(frozenset([j]),[]):
                                for A in balls(r,bd):pairs.update((A,B) for B in ends if A<B)
                if not pairs:continue
                ends=[]
                for B in sorted({b for _,b in pairs},key=faces):
                    order=sorted(B,key=sorted);prefixes=[];marked=[]
                    for mask in range(1,(1<<len(B))-1):
                        A=frozenset(t for j,t in enumerate(order) if mask>>j&1)
                        if engine(A):prefixes.append(mask)
                        if (A,B) in pairs:marked.append(mask)
                    assert set(marked)<=set(prefixes);ends.append(dict(cells=faces(order),prefixes=prefixes,marked=marked))
                entries.append(dict(record=i,root=u,ends=ends));print(i,len(pairs),len(ends),flush=True);break
            if len(entries)==8:break
    assert entries;prev.save(P,dict(protocol=protocol,screened=screened,entries=entries))
def check():
    cnt=Counter();hist=Counter();failed=[];results=[]
    for e in json.loads(P.read_text())['entries']:
        for z in e['ends']:
            cells=list(map(frozenset,z['cells']));full=(1<<len(cells))-1;aset=lambda mask:frozenset(t for j,t in enumerate(cells) if mask>>j&1);assert shelling(aset(full));
            # Backward closure from full ball: a reverse edge is allowed only when
            # deleting the cell leaves a shellable ball and its reattachment is legal.
            allowed=set(z['prefixes'])|{full};seen={full};stack=[full]
            while stack:
                m=stack.pop()
                for j,t in enumerate(cells):
                    n=m^(1<<j)
                    if m>>j&1 and n in allowed and n not in seen and attaches(aset(n),t):seen.add(n);stack.append(n)
            @lru_cache(None)
            def forward(m):
                if m==full:return ()
                A=aset(m)
                for j,t in enumerate(cells):
                    if not m>>j&1 and attaches(A,t):
                        o=forward(m|1<<j)
                        if o is not None:return (j,)+o
                return None
            for m in z['prefixes']:
                o=forward(m);assert (o is not None)==(m in seen);cnt['tested']+=1;cnt['marked']+=m in z['marked'];cnt['extendible']+=o is not None;hist[len(cells)-m.bit_count()]+=1
                if o is None:failed.append(dict(record=e['record'],cells=z['cells'],prefix=m,marked=m in z['marked']))
            results.append(dict(record=e['record'],size=len(cells),prefixes=len(z['prefixes']),reached=len(seen)-1,marked=len(z['marked'])))
    print(cnt,hist,'failures',len(failed));prev.save(R,dict(sample_sha=prev.sha(P.read_bytes()),counts=dict(cnt),gaps=dict(hist),failures=failed,results=results))
if __name__=='__main__':{'freeze':freeze,'check':check}[sys.argv[1]]()
