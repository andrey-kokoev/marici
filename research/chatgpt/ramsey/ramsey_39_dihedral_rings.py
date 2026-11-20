"""Test three 13-rings and thirteen 3-rings under simultaneous rotation and reflection.
No catalogue input. Lazy exact forbidden-set clauses; UNSAT rechecked on the generated CNF.
uv run --with python-sat -- python <file> --length 13
"""
import argparse,subprocess,tempfile
from itertools import combinations
from pathlib import Path
from pysat.solvers import Solver
from pauli_realization_audit import independent_witness,triangle_free

def run(L,budget,swap=False):
    n=39;assert n%L==0
    if swap and L!=13:raise ValueError('swap requires three 13-rings')
    def rotkey(i,j):
        i,j=sorted((i,j));a,b=i//L,j//L;d=(j-i)%L
        return a,b,min(d,L-d) if a==b else d
    def reflect(i):
        a,t=divmod(i,L)
        if swap and a<2:a=1-a
        return a*L+(-t)%L
    def key(i,j):return min(rotkey(i,j),rotkey(reflect(i),reflect(j)))
    # Verify the key partition directly against the 2L group images.
    def rotation(i,t):return (i//L)*L+(i%L+t)%L
    orbits={}
    for i,j in combinations(range(n),2):orbits.setdefault(key(i,j),set()).add((i,j))
    for group in orbits.values():
        i,j=min(group);assert group=={tuple(sorted((rotation(x,t),rotation(y,t)))) for x,y in ((i,j),(reflect(i),reflect(j))) for t in range(L)}
    keys=sorted({key(i,j) for i,j in combinations(range(n),2)});ids={k:t+1 for t,k in enumerate(keys)}
    def clause(T,sign):return tuple(sorted({sign*ids[key(i,j)] for i,j in combinations(sorted(T),2)}))
    clauses=set(clause(t,-1) for t in combinations(range(n),3));base=len(clauses)
    with Solver(name='cadical195',bootstrap_with=sorted(clauses)) as s:
        for step in range(budget):
            if not s.solve():break
            pos=set(s.get_model());rows=[0]*n
            for i,j in combinations(range(n),2):
                if ids[key(i,j)] in pos:rows[i]|=1<<j;rows[j]|=1<<i
            T=independent_witness(rows,10)
            if T is None:
                assert triangle_free(rows);print('SAT',keys,[k for k in keys if ids[k] in pos]);return
            # All relabelings of ring positions by a common unit preserve the ansatz.
            from math import gcd
            for u in range(1,L):
                if gcd(u,L)!=1:continue
                c=clause([v//L*L+v%L*u%L for v in T],1)
                if c not in clauses:s.add_clause(c);clauses.add(c)
        else:print('UNKNOWN iteration budget',budget,flush=True);return
    print('UNSAT',L,'variables',len(keys),'triangle clauses',base,'independent-set clauses',len(clauses)-base,flush=True)
    with Solver(name='cadical195',bootstrap_with=sorted(clauses),with_proof=True) as s:
        assert not s.solve();proof='\n'.join(s.get_proof())+'\n'
    with tempfile.TemporaryDirectory() as tmp:
        f=Path(tmp)/'rings.cnf';p=f.with_suffix('.drat');f.write_text(f'p cnf {len(keys)} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in sorted(clauses)));p.write_text(proof);subprocess.run([str(Path(__file__).parent/'drat-checker/target/release/ramsey-drat-checker'),str(f),str(p)],check=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--length',type=int,default=13);p.add_argument('--budget',type=int,default=5000);p.add_argument('--swap',action='store_true');args=p.parse_args();run(args.length,args.budget,args.swap)
