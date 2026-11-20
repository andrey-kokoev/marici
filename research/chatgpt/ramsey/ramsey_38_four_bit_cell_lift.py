"""Three vs four bit XOR core with arbitrary three-vertex completion; no catalogue.
Run: uv run --with python-sat python ramsey_38_four_bit_cell_lift.py
"""
from itertools import combinations,islice
from time import monotonic
from pysat.solvers import Solver
from ramsey_311_two_qubit_trial import clique

def run(bits,n,seconds):
    names={};pair={};full=(1<<n)-1
    def label(j):
        if bits==5:
            # Maximize distinct unordered pair XORs with the low three profile bits fixed.
            return (8,9,10,11,12,5,30,23)[j]
        if bits==6:
            a,b,c=[j>>i&1 for i in range(3)]
            return j|((1^(a*b))<<3)|((a*c)<<4)|((b*c)<<5)
        assert bits in (3,4)
        return j|((j==0 and bits==4)<<3)
    for i,j in combinations(range(n),2):
        key=('core',*sorted((i//8,j//8)),label(i%8)^label(j%8)) if j<24 else ('border',i,j)
        pair[i,j]=names.setdefault(key,len(names)+1)
    def cut(vs,sgn):return tuple(sorted({sgn*pair[e] for e in combinations(vs,2)}))
    clauses={cut(vs,-1) for vs in combinations(range(n),3)}
    # Seed all within-row blue prohibitions and two-row four-plus-four patterns
    # using identical sets of four columns. Others are separated exactly below.
    for r in range(3):clauses.add(cut(range(8*r,8*r+8),1))
    for a,b in combinations(range(3),2):
        for q in combinations(range(8),4):clauses.add(cut([8*r+p for r in (a,b) for p in q],1))
    with Solver(name='cadical195',bootstrap_with=sorted(clauses)) as sol:
        seen=set();tested=0;end=monotonic()+seconds
        while monotonic()<end:
            sol.conf_budget(1500);ok=sol.solve_limited()
            if ok is None:continue
            if not ok:print(bits,n,'UNSAT',tested,len(seen),flush=True);return
            m=set(sol.get_model());A=[0]*n
            for (i,j),v in pair.items():
                if v in m:A[i]|=1<<j;A[j]|=1<<i
            B=[full^r^(1<<i) for i,r in enumerate(A)];assert next(clique(A,3,full),None) is None
            bad=list(islice(clique(B,8,full),400));tested+=1
            if not bad:
                from pathlib import Path
                import json
                Path(__file__).with_name(f'ramsey_38_cell_{bits}bit_{n}.json').write_text(json.dumps({'labels':[label(i) for i in range(8)],'rows':A}));print(bits,n,'WITNESS',tested,len(seen),flush=True);return
            for s in bad:
                c=cut([i for i in range(n) if s>>i&1],1)
                if c not in seen:seen.add(c);sol.add_clause(c)
        print(bits,n,'timeout',tested,len(seen),flush=True)
if __name__=='__main__':
    for n in (24,27):
        for bits in (3,4):run(bits,n,20)
