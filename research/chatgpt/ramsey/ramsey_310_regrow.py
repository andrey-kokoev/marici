"""Regrow a 39th vertex; the 38-seed comes from a stored witness, not the cyclic search."""
import csv
from pathlib import Path
from ramsey_hall_center_conjecture import independent
A=[sum(int(x)<<j for j,x in enumerate(r)) for r in csv.reader(Path(__file__).with_name('ramsey_3_10_witness_39.csv').read_text().splitlines()) if r]
v=35;A[v]=0;A=[a&~(1<<v) for a in A];I=[0]
for i,a in enumerate(A):
    if i!=v:I += [s|1<<i for s in I if not s&a]
assert max(s.bit_count() for s in I)==9
F=[s for s in I if s.bit_count()==9];hits=[s for s in I if all(s&t for t in F)];s=min(hits,key=int.bit_count);A[v]=s
for i in range(39):
    if s>>i&1:A[i]|=1<<v
assert all(not(A[i]&A[j]) for i in range(39) for j in range(i) if A[i]>>j&1) and not independent(A,(1<<39)-1,10)
print(len(F),len(hits),[i for i in range(39) if s>>i&1])
