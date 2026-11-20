"""Catalogue-free forward search on eleven reflected pairs.
Run: uv run --with python-sat -- python research/chatgpt/ramsey/ramsey_forward_marks.py
"""
from itertools import combinations
from pysat.solvers import Solver
from pauli_realization_audit import triangle_free, independent_witness, encode_graph6


def search(marks, single=True):
    keys=sorted({(u//2,v//2,(u^v)%2) for u,v in combinations(range(22),2)})
    ids={k:i for i,k in enumerate(keys,1)}
    def edge(u,v):return ids[(u//2,v//2,(u^v)%2)]  # u<v
    clauses=[[-edge(u,v) for u,v in combinations(t,2)] for t in combinations(range(22),3)]
    parents=list(range(11))
    def root(a):
        while parents[a]!=a:a=parents[a]
        return a
    for r in range(3):
        for c,m in enumerate(marks,3):
            p,x=(ids[r,c,h] for h in (0,1))
            if not m>>r&1: clauses.extend([[-p],[-x]]);continue
            clauses.append([p,x]);
            if single:clauses.append([-p,-x])
            # By swapping the labels inside pairs along a forest, each
            # of these nonempty connections can be made parallel.
            if root(r)!=root(c): parents[root(r)]=root(c); clauses.append([p])
    # Generate one representative of every reflected seven-set clause.
    seven=set()
    for t in combinations(range(22),7):
        if tuple(sorted(v^1 for v in t))<t:continue
        seven.add(tuple(sorted({edge(u,v) for u,v in combinations(t,2)})))
    with Solver(name='cadical195',bootstrap_with=clauses+sorted(seven)) as solver:
        solver.conf_budget(200000); answer=solver.solve_limited()
        if not answer:return ('UNSAT' if answer is False else 'UNKNOWN'),None
        pos={v for v in solver.get_model() if v>0};rows=[0]*22
        for u,v in combinations(range(22),2):
            if edge(u,v) in pos:rows[u]|=1<<v;rows[v]|=1<<u
        assert triangle_free(rows) and independent_witness(rows,7) is None
        return 'SAT',rows

if __name__=='__main__':
    for marks,single in [(list(range(1,8)),False),([1,2,7,4,5,6,7],True)]:
        status,rows=search(marks,single)
        print('column masks',marks,'single =',single,status,flush=True)
        if rows:
            print('graph6:',encode_graph6(rows))
            print('signed frame:')
            for i in range(11): print(''.join('.PXB'[(rows[2*i]>>(2*j))&3] for j in range(11)))
            assert all(bool((rows[2*r]>>(2*c))&3)==bool(m>>(r)&1)
                       for r in range(3) for c,m in enumerate(marks,3))
            assert not any(all(not(rows[i]>>j&1) for i,j in combinations(t,2))
                           for t in combinations(range(22),7))
