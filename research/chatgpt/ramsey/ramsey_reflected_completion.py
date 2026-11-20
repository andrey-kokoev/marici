"""Complete the best three-row frame from ramsey_signed_overlap_test.py.
Run with uv run --with python-sat --with networkx -- python <this file>.
All labels are zero-based except the one-based graph6 catalogue record.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import networkx as nx
from pysat.solvers import Solver
from pauli_realization_audit import decode_graph6, independent_witness, triangle_free


def main():
    source = (Path(__file__).parent/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines()[173]
    base = decode_graph6(source.decode()); cols = [0,1,6,7,8,9,10]
    assert all(((base[i]>>j)^(base[i^1]>>(j^1)))&1 == 0 for i,j in combinations(range(22),2))
    free = [(a,b,s) for a,b in combinations(cols,2) for s in (0,1)]
    ids = {k:i for i,k in enumerate(free,1)}
    clauses=set()
    for size,sign in ((3,-1),(7,1)):
        for subset in combinations(range(22),size):
            clause=set()
            for i,j in combinations(subset,2):
                key=(i//2,j//2,(i^j)&1)
                if key in ids: clause.add(sign*ids[key])
                elif (base[i]>>j&1)==(sign==1): break  # fixed literal true
            else: clauses.add(tuple(sorted(clause)))
    models=[]; classes=[]
    with Solver(name='glucose3',bootstrap_with=clauses) as solver:
        while solver.solve():
            pos={v for v in solver.get_model() if v>0}; rows=base[:]; changes=[]
            for k,(a,b,s) in enumerate(free,1):
                if (k in pos)==bool(base[2*a]>>(2*b+s)&1): continue
                changes.append((a,b,s,k in pos))
                for h in (0,1):
                    i,j=2*a+h,2*b+(h^s); rows[i]^=1<<j;rows[j]^=1<<i
            assert triangle_free(rows) and independent_witness(rows,7) is None
            g=nx.Graph();g.add_nodes_from(range(22));g.add_edges_from((i,j) for i,j in combinations(range(22),2) if rows[i]>>j&1)
            for idx,h in enumerate(classes):
                if nx.is_isomorphic(g,h):break
            else: idx=len(classes);classes.append(g)
            models.append((idx,changes));solver.add_clause([-k if k in pos else k for k in ids.values()])
    orig=next(i for i,c in models if not c); alt=min((c for i,c in models if i!=orig),key=len,default=None)
    print('clauses',len(clauses),'models',len(models),'uncolored classes',len(classes),'sizes',Counter(i for i,c in models));print('closest nonisomorphic changes',alt)
    for i,c in models:
        print('changed',c,'degree histogram',sorted(Counter(dict(classes[i].degree()).values()).items()))
    print('orbit variables taking both values',sum(any(any(t[:3]==f for t in c) for _,c in models) for f in free))

if __name__=='__main__': main()
