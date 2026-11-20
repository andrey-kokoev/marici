"""Can the four local Seidel switch readings extend coherently? Count triangle-free switches, modulo complement of the switch set. Requires python-sat."""
from itertools import combinations
from collections import Counter
from pathlib import Path
from pysat.solvers import Solver
from exoo39_symbolic_relations import edges


def solve(n,E):
    clauses=[[-1],list(range(2,n+1))] # vertex 0 unswitched; nonempty switch only
    for tri in combinations(range(n),3):
        red=[(a,b) for a,b in combinations(tri,2) if (a,b) in E];assert len(red)<3
        if len(red)!=1:continue
        a,b=red[0];w=next(x for x in tri if x not in (a,b));a+=1;b+=1;w+=1
        clauses.extend(([a,b,-w],[-a,-b,w])) # forbid a,b on one side and w alone on the other
    with Solver(name='cadical195',bootstrap_with=clauses) as s:
        count=0
        while s.solve():
            model=set(s.get_model());A={i for i in range(n) if i+1 in model}
            def switched(i,j):return ((i,j) in E)^((i in A)!=(j in A))
            assert not any(switched(i,j) and switched(i,k) and switched(j,k) for i,j,k in combinations(range(n),3));count+=1;s.add_clause([-(i+1) if i in A else i+1 for i in range(n)])
    return count

def decode(l):
    n=l[0]-63;bits=''.join(f'{x-63:06b}' for x in l[1:]);return n,{(i,j) for i,j in combinations(range(n),2) if bits[j*(j-1)//2+i]=='1'}
if __name__=='__main__':
    for l in [set(),{(0,1)}]:print('3-vertex control',l,'nonidentity',solve(3,l))
    for n,k in [(17,6),(22,7)]:
        ls=Path(__file__).with_name('pauli-realization-catalogues').joinpath(f'r3{k}_{n}.g6').read_bytes().splitlines();print(k,'histogram of nonidentity switches',Counter(solve(*decode(l)) for l in ls))
    import gzip
    ls=gzip.decompress(Path(__file__).with_name('pauli-realization-catalogues').joinpath('r38_27.g6.gz').read_bytes()).splitlines();print(8,'record 1499 (1-based)',solve(*decode(ls[1498])))
    print(9,'35-circle',solve(35,{(i,j) for i,j in combinations(range(35),2) if (j-i)%35 in [1,7,11,16,19,24,28,34]}));print(10,'Exoo',solve(39,edges()))
