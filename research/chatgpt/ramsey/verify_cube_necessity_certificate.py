"""Standard-library recheck: derive every supplied clause from its indicated cube incidence and exhaust its satisfying assignments by binary split/unit propagation."""
from ramsey_cube_pair_rules import F,V,G,edges,D,json,combinations

def run():
    d=json.loads((D/'ramsey_cube_rule_necessity.json').read_text());K=[g for g in G if g('000',state=True)=='000'];rep=lambda e:min(tuple(sorted(map(g,e))) for g in K);reps=sorted({rep(e) for e in edges});assert list(map(tuple,d['reps']))==reps;num={e:1+reps.index(rep(e)) for e in edges};C=[];sig=[{i for i,v in enumerate(V) if all(a=='*' or a==b for a,b in zip(f,v))} for f in F]
    for item in d['certificate']:
        kind,*J=item['source'];e=[num[k] for i,j in combinations(J,2) if (k:=tuple(sorted((F[i],F[j])))) in num]
        if kind=='triangle':assert len(e)==3;c={-v for v in e}
        elif kind=='hall':assert len(set.union(*(sig[i] for i in J)))<len(J);c=set(e)
        else:
            assert kind=='star';i,j=J;star=[p for p in range(26) if j in sig[p]];assert len(star)==7 and i not in star;c={num[k] for p in star if (k:=tuple(sorted((F[i],F[p])))) in num}
        assert sorted(c)==item['literals'];C.append(c)
    nodes=0;sol=[]
    def dfs(A):
        nonlocal nodes;nodes+=1
        while True:
            live=[c-{-i for i in A} for c in C if not c&A];
            if any(not c for c in live):return
            force={next(iter(c)) for c in live if len(c)==1}
            if any(-i in force for i in force):return
            if not force:break
            A=A|force
        if len(A)==len(reps):sol.append(sum(1<<(v-1) for v in A if v>0));return
        i=abs(min(min(live,key=len),key=abs)) if live else next(x for x in range(1,len(reps)+1) if not {x,-x}&A);dfs(A|{i});dfs(A|{-i})
    dfs(set());assert sorted(sol)==d['solutions'];print(len(C),'necessary clauses;',nodes,'search nodes;',len(sol),'solutions')
if __name__=='__main__':run()
