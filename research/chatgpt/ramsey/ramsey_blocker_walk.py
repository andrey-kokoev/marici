"""Can a maximal-size independent-set query force a specified step?"""
import csv
from collections import Counter
from pathlib import Path
from ramsey_39_cyclic_constructor import graph
from ramsey_mutual_repair_conjecture import sevens
D=Path(__file__).parent
def load(name):return [sum(int(z)<<i for i,z in enumerate(row)) for row in csv.reader((D/name).read_text().splitlines()) if row]
for A,k in [(graph((1,7,11,16)),9),(load('ramsey_3_10_target_only_cyclic_38.csv'),10),(load('ramsey_3_10_witness_39.csv'),10)]:
    sets=list(sevens(A,k=k-1));unique=Counter();example=None
    for p,N in enumerate(A):
        for I in sets:
            if I>>p&1:continue
            hit=I&N;assert hit
            if hit.bit_count()==1:
                unique[p,hit.bit_length()-1]+=1
                if p==0 and hit==2 and example is None:example=[j for j in range(len(A)) if I>>j&1]
    print(len(A),'sets',len(sets),'forceable directed edges',len(unique),'of',sum(m.bit_count() for m in A),'example for 0->1',example)
