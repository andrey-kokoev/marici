"""Check cyclic coordinate symmetry without prescribing a single edge.
Run with uv run --with python-sat -- python <file>. Build the local DRAT checker first.
"""
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
from pysat.solvers import Solver


def main():
    # Two copies of (A,B,C,a,b,c,ab,bc,ca,abc,Z).
    p=[base+i for base in (0,11) for i in (1,2,0,4,5,3,7,8,6,9,10)]
    ids={}; edge={}
    for i,j in combinations(range(22),2):
        k=min(tuple(sorted(pair)) for pair in ((i,j),(p[i],p[j]),(p[p[i]],p[p[j]])))
        edge[i,j]=ids.setdefault(k,len(ids)+1)
    clauses=sorted({tuple(sorted({sign*edge[t] for t in combinations(s,2)})) for n,sign in ((3,-1),(7,1)) for s in combinations(range(22),n)})
    with Solver(name='cadical195',bootstrap_with=clauses,with_proof=True) as solver:
        assert not solver.solve(); trace=solver.get_proof()
    with TemporaryDirectory() as d:
        f=Path(d)/'cycle.cnf';g=f.with_suffix('.drat');f.write_text(f'p cnf {len(ids)} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in clauses));g.write_text('\n'.join(trace)+'\n');subprocess.run([str(Path(__file__).parent/'drat-checker/target/release/ramsey-drat-checker'),str(f),str(g)],check=True)
    print(len(ids),'edge orbits')

if __name__=='__main__': main()
