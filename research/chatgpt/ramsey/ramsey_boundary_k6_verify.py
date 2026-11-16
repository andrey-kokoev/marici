"""Independent, exact K6 dual obstruction checker for the two 34-edge controls."""
from itertools import combinations
import json
from ramsey_integer_diffusion_verify import decode, indep

data=json.load(open('/mnt/data/ramsey_boundary_k6_witnesses.json'))
for entry in data['records']:
    A=decode(entry['graph6']);assert sum(row.bit_count() for row in A)//2==34
    F=list(indep(A,5));ports=[sum(1<<v for v in S) for S in entry['ports']]
    assert len(set(ports))==6
    assert all(len(set(S))==5 and T in F for S,T in zip(entry['ports'],ports))
    # Every independent 5-set avoids at most one port: exact dual feasibility.
    assert all(sum((I&T)==0 for T in ports)<=1 for I in F)
    print('VERIFIED',entry['graph6'],'5-set count',len(F),'K6 dual weight=6')
print('Both examples disprove a universal <6 fractional inequality at 34 edges.')
