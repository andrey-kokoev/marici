"""Shrink five-label coverage constraints relative to the fixed four-label baseline."""
from itertools import product,combinations
from pathlib import Path
from pysat.solvers import Solver
from pysat.card import CardEnc
import json


def setup():
    cells=[''.join(x) for x in product('01*',repeat=3) if x!=('*',)*3];corners=[s for s in cells if '*' not in s];m={s:{b for b in corners if all(x=='*' or x==y for x,y in zip(s,b))} for s in cells};v={frozenset(p):i for i,p in enumerate((p for p in combinations(cells,2) if m[p[0]].isdisjoint(m[p[1]])),1)}
    def edges(q):return [v[e] for p in combinations(q,2) if (e:=frozenset(p)) in v]
    base=[[-e for e in es] for q in combinations(cells,3) if len(es:=edges(q))==3];top=len(v)
    for s in cells:
        d=CardEnc.equals([x for p,x in v.items() if s in p],8-len(m[s]),top_id=top);top=d.nv;base+=d.clauses
    groups={};names={};clauses=[]
    for n in range(2,6):
        for L in combinations(corners,n):
            qs=list(combinations([s for s in cells if m[s]<=set(L)],n+1))
            if n<5:base.extend(edges(q) for q in qs);continue
            top+=1;groups[top]=qs;names[top]=L;clauses.extend([-top,*edges(q)] for q in qs)
    return corners,v,base,top,groups,names,clauses


def audit():
    corners,v,base,top,groups,names,clauses=setup()
    out=[]
    for s,t,u in [('*00','**1','*1*'),('**0','*01','*11')]:
        fixed=[[-v[frozenset((s,p))]] for p in (t,u)];
        with Solver(name='cadical195',bootstrap_with=base+fixed+clauses) as sl:
            core=list(groups);assert not sl.solve(assumptions=core)
            for a in core[:]:
                tmp=[b for b in core if b!=a]
                if not sl.solve(assumptions=tmp):core=tmp
            assert all(sl.solve(assumptions=[b for b in core if b!=a]) for a in core)
        qs=[(a,q) for a in core for q in groups[a]];ids={top+1+i:(a,q) for i,(a,q) in enumerate(qs)}
        with Solver(name='cadical195',bootstrap_with=base+fixed+[[-i,*edges(q)] for i,(a,q) in ids.items()]) as sl:
            assert not sl.solve(assumptions=list(ids));used=sorted(sl.get_core());
            for i in used[:]:
                tmp=[j for j in used if j!=i]
                if not sl.solve(assumptions=tmp):used=tmp
            records=[]
            for i in used:
                assert sl.solve(assumptions=[j for j in used if j!=i]);a,q=ids[i];records.append(dict(labels=names[a],cells=q))
        with Solver(name='cadical195',bootstrap_with=base+fixed) as sl:
            for r in records:
                r['possible_red']=[sorted(p) for p,e in v.items() if p<=set(r['cells']) and sl.solve(assumptions=[e])];assert r['possible_red']
        out.append(dict(wedge=[s,t,u],regions=[names[a] for a in core],six_cell_clauses=records));print(s,len(core),len(records),[names[a] for a in core],flush=True)
    (Path(__file__).resolve().parents[1]/'results/ramsey_wedge_region_core.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
