"""Terminal blue-link shapes counted on four fixed witnesses, not family invariants."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import gzip
from exoo39_symbolic_relations import edges
from ramsey_clique_power_blowup import layers


def g6(line):
    n=line[0]-63
    bits=''.join(f'{x-63:06b}' for x in line[1:])
    return n,{(i,j) for i,j in combinations(range(n),2) if bits[j*(j-1)//2+i]=='1'}


def coordinates(k,n,E):
    adj=[sum(1<<j for j in range(n) if tuple(sorted((i,j))) in E) for i in range(n)]
    faces=layers(adj);assert all(a in faces for a in adj) and max(map(int.bit_count,faces))==k-1
    counts=Counter()
    for s in faces:
        if s.bit_count()!=k-2:continue
        available=((1<<n)-1)^s
        for i,a in enumerate(adj):
            if s>>i&1:available &= ~a
        assert available.bit_count()<=2
        counts[available.bit_count()]+=1
    print(k,n,[counts[i] for i in range(3)])


if __name__=='__main__':
    d=Path(__file__).with_name('pauli-realization-catalogues')
    coordinates(7,*g6((d/'r37_22.g6').read_bytes().splitlines()[0]))
    coordinates(8,*g6(gzip.decompress((d/'r38_27.g6.gz').read_bytes()).splitlines()[1498]))
    coordinates(9,35,{(i,j) for i,j in combinations(range(35),2) if j-i in (1,7,11,16,19,24,28,34)})
    coordinates(10,39,edges())
