"""Find a smallest joint blue-eight veto for every locally forced but jointly illegal move. Count arity by two exact methods."""
from ramsey_double_cross_blind_veto import audit as generate,CAT,D,decode,combinations,islice,gzip,json,Counter
from ramsey_retention_slice import has

def audit():
    idx=448077
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:a=decode(next(islice(f,idx,None)).strip())
    cases=[];hist=Counter()
    def record(z,pair,cuts,g):
        active=((1<<27)-1)^(1<<z);I=[0]
        for i,v in enumerate(g):
            if i!=z:I.extend([s|1<<i for s in I if not s&v and s.bit_count()<8])
        before=a[:];before[z]=0
        for i in range(27):before[i]&=active
        for u,v in pair:before[u]|=1<<v;before[v]|=1<<u
        assert all(not g[i]&g[j] for i,j in combinations(range(27),2) if g[i]>>j&1)
        options=[]
        for q in I:
            if q.bit_count()!=8:continue
            old=tuple((i,j) for i,j in combinations([i for i in range(27) if q>>i&1],2) if before[i]>>j&1);assert set(old)<=cuts;options.append((len(old),q,old))
        k,q,small=min(options);assert k>=2
        # Test all smaller cut subsets explicitly, and replay the indicated veto alone.
        def fails(sub):
            b=before[:]
            for i,j in sub:b[i]^=1<<j;b[j]^=1<<i
            return has([~n for n in b],active,8)
        assert all(not fails(sub) for n in range(k) for sub in combinations(sorted(cuts),n)) and fails(small);hist[k]+=1;cases.append(dict(z=z,add=pair,all_cuts=sorted(cuts),minimum=k,witness_cuts=small,blue_eight=[i for i in range(27) if q>>i&1],distinct_vetoes=len({s for _,_,s in options})))
    generate(record);prior=json.loads((D.parent/'ramsey_double_cross_blind_veto.json').read_text())['counts'];assert len(cases)==prior['locally_forced']-prior['jointly_legal']==158;print('minimum cut arities',hist,'largest example',max(cases,key=lambda r:r['minimum']));(D.parent/'ramsey_joint_veto_arity.json').write_text(json.dumps(dict(record=idx,histogram=hist,cases=cases),indent=1)+'\n')
if __name__=='__main__':audit()
