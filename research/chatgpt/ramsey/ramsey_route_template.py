"""Relax the seed one whole incidence at a time; verify reusable parity template.
Run with uv run --with python-sat -- python <file>. Lashed labels are pair types.
"""
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
from pysat.solvers import Solver
from ramsey_unsigned_route_split import build
from pauli_realization_audit import encode_graph6,independent_witness,triangle_free

L='ABCabcuvdeZ'
def main():
    ids,old=build();ramsey=old[69:];assert len(ramsey)==770+85272
    # u,v are the two column pairs of the tested rectangle. Normalize THREE
    # edges on its spanning tree, never using any other mark for this gauge.
    core=[]
    for i,j in [(2,6),(2,7),(6,10),(7,10)]:
        p,x=[ids[i,j,h] for h in (0,1)];core.extend([[p,x],[-p,-x]])
        if (i,j)!=(7,10):core.append([p])
    odd=ids[7,10,1]; groups={};mask=[1,2,4,5,6,7,7]
    for j,m in enumerate(mask,3):
        for r in (0,1,2,10):
            i,k=sorted((r,j));p,x=[ids[i,k,h] for h in (0,1)]
            if (i,k) in [(2,6),(2,7),(6,10),(7,10)]:continue
            mark=bool(m & (4 if r==10 else 1<<r));groups[L[r]+L[j]]=([[p,x],[-p,-x]] if mark else [[-p],[-x]])
    for i in range(3):groups[L[i]+'Z']=[[-ids[i,10,h]] for h in (0,1)]
    groups['ZZ']=[[ids[10,10,1]]]; sel={k:len(ids)+i+1 for i,k in enumerate(groups)}
    formula=ramsey+core+[[*c,-sel[k]] for k,cc in groups.items() for c in cc]
    with Solver(name='cadical195',bootstrap_with=formula) as s:
        def solve(keep,par):return s.solve(assumptions=[par]+[sel[k] for k in keep])
        # Template found by greedy whole-cell relaxation; replay directly.
        keep='Bb Ac Bc Zc Bu Av Zd Ae Be Ze'.split()
        print('kept',keep,'free',sorted(groups.keys()-set(keep)),flush=True)
        # Additional phase normalization along a forest of guaranteed single marks.
        parent=list(range(11))
        def root(i):
            while parent[i]!=i:i=parent[i]
            return i
        for i,j in [(2,6),(2,7),(6,10)]:parent[root(i)]=root(j)
        for k in keep:
            if len(groups[k][0])!=2:continue
            i,j=sorted(map(L.index,k))
            if root(i)!=root(j):
                parent[root(i)]=root(j); c=[ids[i,j,0]];core.append(c);s.add_clause(c)
        def model():
            pos=set(s.get_model());rows=[0]*22
            for i,j in combinations(range(22),2):
                if ids[i//2,j//2,(i^j)&1] in pos:rows[i]|=1<<j;rows[j]|=1<<i
            assert triangle_free(rows) and independent_witness(rows,7) is None
            return encode_graph6(rows),rows
        assert solve(groups,odd);print('original',model()[0]);
        # Allow all relaxed entries to vary and seek a changed unsigned A/B/C mark.
        for key in sorted(groups.keys()-set(keep)):
            if 'Z' in key:continue
            i,j=sorted(map(L.index,key));p,x=[ids[i,j,h] for h in (0,1)];was=groups[key][0]==[p,x]
            modes=[[-p,-x]] if was else [[p,-x],[-p,x]]
            if any(s.solve(assumptions=[sel[k] for k in keep]+[odd]+mode) for mode in modes):
                code,rr=model();print('changed mark',key,code,'unsigned column weights',sorted(sum(bool(rr[2*r]>>(2*j)&3) for r in range(3)) for j in range(3,10)),flush=True);break
    cnf=ramsey+core+[c for k in keep for c in groups[k]]+[[-odd]]
    with Solver(name='cadical195',bootstrap_with=cnf,with_proof=True) as s:
        assert not s.solve();trace=s.get_proof()
    with TemporaryDirectory() as d:
        f=Path(d)/'even.cnf';p=f.with_suffix('.drat');f.write_text(f'p cnf {len(ids)} {len(cnf)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in cnf));p.write_text('\n'.join(trace)+'\n');subprocess.run([str(Path(__file__).parent/'drat-checker/target/release/ramsey-drat-checker'),str(f),str(p)],check=True)
if __name__=='__main__':main()
