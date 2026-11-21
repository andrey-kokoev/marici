"""Synthesize equivariant 11-row rules from cube incidence, NOT from saved outputs. Work at 000 modulo its stabilizer. Compare strictly local Hall, neighborhood and triangle obligations. MUS-style optional certificate compression."""
from ramsey_cube_pair_rules import F,V,G,edges,D,json,combinations,verify_rules
from pysat.solvers import Solver
from collections import Counter

def run():
    K=[g for g in G if g('000',state=True)=='000'];orb=lambda e:min(tuple(sorted(map(g,e))) for g in K);reps=sorted({orb(e) for e in edges});X={e:reps.index(orb(e))+1 for e in edges};n=len(reps);sig=[sum(1<<i for i,v in enumerate(V) if all(x=='*' or x==y for x,y in zip(f,v))) for f in F];ix={(F.index(a),F.index(b)):v for (a,b),v in X.items()};rows={};
    def add(lits,tag):
        c=tuple(sorted(set(lits)));rows.setdefault(c,tag)
    for i,j,k in combinations(range(26),3):
        q=[ix.get(e) for e in ((i,j),(j,k),(i,k))];
        if all(q):add([-v for v in q],('triangle',i,j,k))
    for radius in range(2,7):
        for U in combinations(range(8),radius):
            mask=sum(1<<i for i in U)
            for J in combinations([i for i,m in enumerate(sig) if m&~mask==0],radius+1):add([ix[e] for e in combinations(J,2) if e in ix],('hall',*J))
    for j in range(8):
        star=[i for i,m in enumerate(sig) if m>>j&1];assert len(star)==7
        for i in range(26):
            if i not in star:add([ix[e] for v in star for e in [tuple(sorted((i,v)))] if e in ix],('star',i,j))
    # Throw out clauses containing a smaller one (literal signs retained).
    kept=[];bylit={};
    for c in sorted(rows,key=lambda t:(len(t),t)):
        C=set(c)
        if any(k<=C for v in c for k in bylit.get(v,())):continue
        kept.append(c);bylit.setdefault(c[0],[]).append(C)
    def models(cs,limit=10):
        with Solver(name='cadical195',bootstrap_with=cs) as s:
            ans=[]
            while len(ans)<limit and s.solve():
                m=set(s.get_model());w=sum(1<<(i-1) for i in range(1,n+1) if i in m);ans.append(w);s.add_clause([(-i if i in m else i) for i in range(1,n+1)])
            return sorted(ans)
    solutions=models(kept);print('vars',n,'counts',len(rows),len(kept),'models',len(solutions),flush=True);assert len(solutions)==2
    def table(w):
        red={e for e,i in X.items() if w>>(i-1)&1};ret={}
        for e in edges:
            o=[tuple(sorted(map(g,e))) for g in G];r=min(o)
            if e in red:ret.setdefault(r,set()).update(g('000',state=True) for g,u in zip(G,o) if u==r)
        return {' '.join(e):sorted(ret.get(e,())) for e in sorted({min(tuple(sorted(map(g,e))) for g in G) for e in edges})}
    tables=[table(w) for w in solutions];assert all({''.join(str(1-int(v)) for v in c) for c in Vv}==set(tables[1][p]) for p,Vv in tables[0].items());[verify_rules(t) for t in tables]
    # Delete unnecessary clauses using one permanent exclusion clause per known solution.
    cs={i:c for i,c in enumerate(kept,1)};guards=[-n-i for i in cs];keep=list(cs)
    with Solver(name='cadical195') as s:
        for w in solutions:s.add_clause([(-i if w>>(i-1)&1 else i) for i in range(1,n+1)])
        for i,c in cs.items():s.add_clause([*c,-(n+i)])
        assert not s.solve(assumptions=[n+i for i in keep]);keep=sorted(v-n for v in s.get_core());
        for i in keep[:]:
            t=[j for j in keep if j!=i]
            if not s.solve(assumptions=[n+j for j in t]):keep=t
    assert models([cs[i] for i in keep])==solutions;hist=Counter(rows[cs[i]][0] for i in keep);print('irredundant',len(keep),hist,flush=True);return dict(reps=reps,tables=tables,solutions=solutions,unique_clauses=len(rows),subsumption_minimal=len(kept),certificate=[dict(literals=cs[i],source=rows[cs[i]]) for i in keep])
if __name__=='__main__':(D/'ramsey_cube_rule_necessity.json').write_text(json.dumps(run())+'\n')
