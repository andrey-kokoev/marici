"""Two-squares obstruction by row/column profile. Run with python-sat.
Independently checks the combined UNSAT formula; finds countermodels for each
profile individually and each proper union of pairs containing the rectangle.
"""
from itertools import combinations
from tempfile import TemporaryDirectory
from pathlib import Path
import subprocess
from pysat.solvers import Solver
from ramsey_unsigned_route_split import build
from pauli_realization_audit import triangle_free,independent_witness

def main():
    ids,old=build(); base=old[:69];assert all(len(c)<=2 for c in base) and old[69][0]<0
    u,v=ids[6,10,1],ids[7,10,1];base=base+[[-u,v],[u,-v]]
    def constraints(vertices,sizes):
        out={s:[] for s in sizes}
        for n in {3,7}:
            for t in combinations(vertices,n):
                if t>tuple(sorted(i^1 for i in t)):continue
                k=-1 if n==3 else sum(i//2 in (0,1,2,10) for i in t)
                if k in sizes:out[k].append(sorted({(-1 if n==3 else 1)*ids[i//2,j//2,(i^j)&1] for i,j in combinations(t,2)}))
        return out
    def rows(vertices,model):
        pos=set(model);r=[0]*len(vertices)
        for a,b in combinations(range(len(vertices)),2):
            i,j=vertices[a],vertices[b]
            if ids[i//2,j//2,(i^j)&1] in pos:r[a]|=1<<b;r[b]|=1<<a
        return r
    allv=list(range(22));cs=constraints(allv,{-1,2,4});tri=base+cs[-1]
    for k in (2,4):
        with Solver(name='cadical195',bootstrap_with=tri+cs[k]) as s:
            assert s.solve();r=rows(allv,s.get_model());assert triangle_free(r)
            counts={2:0,4:0}
            for t in combinations(allv,7):
                h=sum(i//2 in (0,1,2,10) for i in t)
                if h in counts and all(not(r[i]>>j&1) for i,j in combinations(t,2)):counts[h]+=1
            assert counts[k]==0 and counts[6-k]>0;print('avoid profile',k,'counts',counts,flush=True)
    cnf=tri+cs[2]+cs[4]
    with Solver(name='cadical195',bootstrap_with=cnf,with_proof=True) as s:
        assert not s.solve();trace=s.get_proof()
    with TemporaryDirectory() as tmp:
        f=Path(tmp)/'profiles.cnf';p=f.with_suffix('.drat');f.write_text(f'p cnf {len(ids)} {len(cnf)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in cnf));p.write_text('\n'.join(trace)+'\n');subprocess.run([str(Path(__file__).parent/'drat-checker/target/release/ramsey-drat-checker'),str(f),str(p)],check=True)
    for drop in (0,1,3,4,5,8,9):
        verts=[i for i in allv if i//2!=drop];local=constraints(verts,set(range(-1,8)))
        with Solver(name='cadical195',bootstrap_with=base+sum(local.values(),[])) as s:
            assert s.solve();r=rows(verts,s.get_model());assert triangle_free(r) and independent_witness(r,7) is None
        print('both squares extend without pair','ABCabcuvdeZ'[drop])

if __name__=='__main__':main()
