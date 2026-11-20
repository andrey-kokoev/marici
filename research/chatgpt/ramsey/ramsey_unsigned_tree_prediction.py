"""Test the preselected singleton trees on all joined-center completions.
uv run --with python-sat -- python <file>. No catalogue input.
"""
from itertools import combinations
from tempfile import TemporaryDirectory
from pathlib import Path
import subprocess
from pysat.solvers import Solver
from ramsey_unsigned_route_split import build
from pauli_realization_audit import triangle_free,independent_witness,encode_graph6


def main():
    ids,base=build(); L='ABCabcuvdeZ'; core='ABCuvZ'; square={'Cu','Cv','uZ','vZ'}
    def key(i,j):return tuple(sorted((L.index(i),L.index(j))))
    required={key(*k) for k in square|{'Au','Bv'}}
    missing=[]
    for col,row in [('a','A'),('b','B')]:
        allow=required|{key(row,col)}
        absent=[key(i,j) for i,j in combinations(core+col,2) if key(i,j) not in allow]
        missing.append([ids[i,j,h] for i,j in absent for h in (0,1)])
    for name,extra in [('consistent',[]),('a fails',missing[:1]),('b fails',missing[1:]),('both fail',missing)]:
        cnf=base+extra
        with Solver(name='cadical195',bootstrap_with=cnf,with_proof=(name=='both fail')) as s:
            ans=s.solve(); print(name,ans,flush=True)
            if ans:
                pos=set(s.get_model());rows=[0]*22
                for i,j in combinations(range(22),2):
                    if ids[i//2,j//2,(i^j)&1] in pos:rows[i]|=1<<j;rows[j]|=1<<i
                assert triangle_free(rows) and independent_witness(rows,7) is None
                print(encode_graph6(rows),'extra entries',[[k for k in ids if ids[k] in pos and ids[k] in clause] for clause in missing]);continue
            trace=s.get_proof()
        with TemporaryDirectory() as tmp:
            f=Path(tmp)/'test.cnf';p=f.with_suffix('.drat');f.write_text(f'p cnf {len(ids)} {len(cnf)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in cnf));p.write_text('\n'.join(trace)+'\n');subprocess.run([str(Path(__file__).parent/'drat-checker/target/release/ramsey-drat-checker'),str(f),str(p)],check=True)
if __name__=='__main__':main()
