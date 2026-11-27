"""Shrink local-veto explanations; verify each against actual shellable proper submeshes."""
from ramsey38_vertex_veto_holdout import P,p,shared_index,candidates,permutations,lru_cache,Counter,reject
from ramsey38_shell_lookup_trial import encoder,build
from ramsey38_compare_support_fillings import boundary

def predicates(B,atoms):
    return reject(B,*({s for k,s in atoms if k==t} for t in ('bury','expose','carry')),True)

@lru_cache(maxsize=4096)
def shrink(B,atoms):
    left=list(atoms)
    for a in atoms:
        trial=[b for b in left if b!=a]
        if predicates(B,trial):left=trial
    return tuple(left)

def run(repair=False):
    from itertools import combinations
    repaired=[];final_sizes=Counter()
    es=p.json.loads(P.read_text())['entries'];ids={e['record'] for e in es};words={};idx=shared_index();atlas=set(m for bucket in idx.values() for m in bucket);encode=encoder();sizes=Counter();exact=Counter();examples={}
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in ids:words[i]=line.strip()
            if i>=max(ids):break
    @lru_cache(maxsize=256)
    def subballs(B):
        ts=sorted(B,key=sorted);out=[]
        for m in range(1,(1<<len(ts))-1):
            A=frozenset(t for i,t in enumerate(ts) if m>>i&1)
            if encode(A) in atlas:out.append((A,boundary(A)))
        return out
    @lru_cache(maxsize=4096)
    def verify(B,core):
        witnesses={};n=len(core)
        for A,bd in subballs(B):
            fails=[]
            for i,(k,s) in enumerate(core):
                on=any(s<=f for f in bd);inside=any(s<=t for t in A)
                if not(on if k=='expose' else inside and not on if k=='bury' else inside):fails.append(i)
            if not fails:return None  # the entire proposed subset has a witness
            if len(fails)==1:witnesses.setdefault(fails[0],p.faces(A))
        return witnesses
    for e in es:
        g=p.graph(words[e['record']]);u=e['root'];L,rows,_,dec,stage,_=p.prepare(g,u);_,rs,ms=p.setup(g,u)
        @lru_cache(None)
        def pool(r,bs):return {frozenset(ts) for bd in bs for ts in candidates(idx,L,r,set(map(dec,bd)))}
        for a in ms:
            r,S=stage((a,));x,v=a;rr={**rs,x:rs[x]|1<<L.index(v)}
            for b in p.setup(p.add(g,a),u)[2]:
                q,T=stage(tuple(sorted((a,b))))
                for j,k in permutations(rows,2):
                    if not pool(r,tuple(S.get(frozenset([j]),()))):continue
                    atoms=tuple(sorted({('bury',dec(rs[x]))}|{('bury' if h==j else 'carry' if s.bit_count()==4 else 'expose',dec(s)) for h,s in rr.items()},key=lambda a:(a[0],sorted(a[1]))))
                    for B in pool(q,tuple(T.get(frozenset([j,k]),()))):
                        if not predicates(B,atoms):continue
                        c=shrink(B,atoms);w=verify(B,c);n=len(c);sizes[n]+=1;exact[len(w)==n]+=1;key=f'{n}_{len(w)}'
                        if repair:
                            short=c
                            if len(w)<n:
                                for length in range(1,n):
                                    short=next((s for s in combinations(c,length) if verify(B,s) is not None),None)
                                    if short is not None:break
                                assert short is not None and len(short)<n
                                ws=verify(B,short);assert set(ws)==set(range(len(short)))
                                repaired.append(dict(record=e['record'],root=u,goal=[j,k],moves=[a,b],end=p.faces(B),original=[(t,sorted(s)) for t,s in c],core=[(t,sorted(s)) for t,s in short],drop_one_witnesses=ws))
                            final_sizes[len(short)]+=1
                        if key not in examples:examples[key]=dict(record=e['record'],root=u,goal=[j,k],moves=[a,b],end=p.faces(B),core=[(kind,sorted(s)) for kind,s in c],drop_one_witnesses=w)
    assert sum(sizes.values())==411
    if repair:
        assert len(repaired)==19 and exact[True]==392
        changes=Counter((len(z['original']),len(z['core'])) for z in repaired);print(final_sizes,changes)
        p.prev.save(p.prev.out/'ramsey38_exact_conflict_repairs.json',dict(source_sha=p.prev.sha(P.read_bytes()),sizes=dict(final_sizes),repairs=repaired));return
    print(sizes,exact);p.prev.save(p.prev.out/'ramsey38_local_conflict_certificates.json',dict(source_sha=p.prev.sha(P.read_bytes()),sizes=dict(sizes),exactly_irreducible=exact[True],redundant=exact[False],examples=examples))
if __name__=='__main__':
    import sys
    run('--repair' in sys.argv)
