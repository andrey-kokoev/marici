"""Test route splitting with unsigned marks only. Run with uv run --with python-sat.
The first 3 pair types are A,B,C; columns a,b,c,u=AC,v=BC,d,e; last pair Z.
"""
from itertools import combinations,product
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
from pysat.solvers import Solver
from pauli_realization_audit import triangle_free,independent_witness,encode_graph6

def build():
    keys=sorted({(i//2,j//2,(i^j)&1) for i,j in combinations(range(22),2)})
    ids={k:i for i,k in enumerate(keys,1)}
    def edge(i,j):return ids[i//2,j//2,(i^j)&1]
    clauses=[]
    masks=[1,2,4,5,6,7,7]; supports={}
    for j,m in enumerate(masks,3):
        for r in range(3):supports[r,j]=bool(m>>r&1)
        supports[j,10]=bool(m&4)
    for r in range(3):supports[r,10]=False
    clauses.append([ids[10,10,1]])
    for (i,j),mark in supports.items():
        p,x=[ids[i,j,h] for h in (0,1)]
        clauses.extend([[p,x],[-p,-x]] if mark else [[-p],[-x]])
    # Gauge: switch each C-neighbor column to make its C edge parallel;
    # then switch Z to make Z-d parallel. These form a forest, not a cycle.
    for j in (5,6,7,8,9):clauses.append([ids[2,j,0]])
    clauses.append([ids[8,10,0]])
    for size,sign in [(3,-1),(7,1)]:
        for t in combinations(range(22),size):
            if tuple(sorted(v^1 for v in t))<t:continue
            clauses.append(sorted({sign*edge(i,j) for i,j in combinations(t,2)}))
    return ids,clauses

def main():
    ids,clauses=build();u,v=ids[6,10,1],ids[7,10,1]
    with Solver(name='cadical195',bootstrap_with=clauses) as solver:
        for b,c in product([0,1],repeat=2):
            sat=solver.solve(assumptions=[u if b else -u,v if c else -v]); print('AC,BC relative crossings',b,c,'SAT' if sat else 'UNSAT',flush=True)
            if sat:
                pos=set(solver.get_model()); rows=[0]*22
                for i,j in combinations(range(22),2):
                    if ids[i//2,j//2,(i^j)&1] in pos:rows[i]|=1<<j;rows[j]|=1<<i
                assert triangle_free(rows) and independent_witness(rows,7) is None
                print('verified',encode_graph6(rows))
    equal=clauses+[[-u,v],[u,-v]]
    with Solver(name='cadical195',bootstrap_with=equal,with_proof=True) as solver:
        if solver.solve():return
        trace=solver.get_proof()
    with TemporaryDirectory() as tmp:
        cnf=Path(tmp)/'equal.cnf';proof=cnf.with_suffix('.drat')
        cnf.write_text(f'p cnf {len(ids)} {len(equal)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in equal));proof.write_text('\n'.join(trace)+'\n')
        checker=Path(__file__).parent/'drat-checker/target/release/ramsey-drat-checker'
        subprocess.run([str(checker),str(cnf),str(proof)],check=True)

if __name__=='__main__':main()
