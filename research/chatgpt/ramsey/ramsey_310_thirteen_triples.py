"""CEGAR for 13 free C3 orbits, no template restriction; uv run --with python-sat."""
from itertools import combinations
from collections import Counter
from time import monotonic
from pathlib import Path
import sys,json,gzip
from pysat.solvers import Solver
from ramsey_mutual_repair_conjecture import sevens

def var(i,j):
    a,x=divmod(i,3);b,y=divmod(j,3)
    if a==b:return 0  # one internal edge would generate a triangle
    if a>b:a,b,x,y=b,a,y,x
    return 1+3*(b*(b-1)//2+a)+(y-x)%3

def run(seconds):
    D=Path(__file__).with_suffix('.json.gz');cuts=set();tri=set()
    for t in combinations(range(39),3):
        c=tuple(sorted(-var(i,j) for i,j in combinations(t,2)))
        if 0 not in c:tri.add(c)
    with Solver(name='g4',bootstrap_with=tri) as solver:
        def q(a,b):return 235+(var(3*a,3*b)-1)//3
        for a,b in combinations(range(13),2):
            vs=[var(3*a,3*b+i) for i in range(3)];solver.add_clause([-q(a,b),*vs]);
            for v in vs:solver.add_clause([-v,q(a,b)])
            # An anticomplete pair cannot have three further common nonneighbor orbits:
            # those nine triangle-free vertices contain an independent four.
            for U in combinations(set(range(13))-{a,b},3):solver.add_clause([q(a,b)]+[q(i,u) for i in (a,b) for u in U])
        for U in combinations(range(13),4):solver.add_clause([q(i,j) for i,j in combinations(U,2)])
        if D.exists():
            with gzip.open(D,'rt') as fh:cuts.update(tuple(c) for c in json.load(fh));
            for c in cuts:solver.add_clause(c)
        start=monotonic();rounds=0;status='inconclusive'
        while monotonic()-start<seconds:
            solver.conf_budget(5000);ok=solver.solve_limited()
            if ok is None:continue
            if not ok:status='UNSAT';break
            pos=set(solver.get_model());A=[sum(1<<j for j in range(39) if var(i,j) in pos) for i in range(39)]
            # Sample violations from both ends of the vertex order using a rotating orbit ordering.
            order=[(i+3*(rounds%13))%39 for i in range(39)];B=[sum(1<<j for j,v in enumerate(order) if A[u]>>v&1) for u in order];cnt=0
            for m in sevens(B,k=10):
                U=[order[j] for j in range(39) if m>>j&1];c=tuple(sorted({var(i,j) for i,j in combinations(U,2)}-{0}));
                if c not in cuts:cuts.add(c);solver.add_clause(c);cnt+=1
                if cnt>=32:break
            if not cnt:status='SAT';print('witness',A);break
            rounds+=1
    with gzip.open(D,'wt',compresslevel=1) as fh:json.dump(sorted(cuts),fh,separators=(',',':'))
    print(status,'triangle clauses',len(tri),'ten-set cuts',len(cuts),'refined models',rounds)
if __name__=='__main__':run(float(sys.argv[1]) if len(sys.argv)>1 else 30)
