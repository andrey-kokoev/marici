"""Check all one-vertex extensions of the local 22-vertex catalogue."""
from itertools import combinations
from collections import Counter
from pathlib import Path
from pauli_realization_audit import decode_graph6,triangle_free,independent_witness


def main():
    path=Path(__file__).parent/'pauli-realization-catalogues/r37_22.g6'
    counts=Counter();records=0
    for code in path.read_text().splitlines():
        a=decode_graph6(code);assert len(a)==22 and triangle_free(a) and independent_witness(a,7) is None
        records+=1;eligible=[i for i,r in enumerate(a) if r.bit_count()<6]
        for d in (5,6):
            for t in combinations(eligible,d):
                m=sum(1<<i for i in t)
                if any(a[i]&m for i in t):continue
                counts[d]+=1
                assert independent_witness(a,6,((1<<22)-1)^m) is not None
    print(records, dict(counts))

if __name__=='__main__':main()
