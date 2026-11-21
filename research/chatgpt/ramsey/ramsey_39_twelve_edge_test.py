"""Strengthen the deficiency test with standard small Ramsey numbers and catalogue minima."""
from functools import lru_cache
from math import inf,ceil
from pathlib import Path
import gzip
R=[0,1,3,6,9,14,18,23,28,36];D=Path(__file__).parent/'pauli-realization-catalogues';mins={}
for k in range(4,9):
    p=next(D.glob(f'r3{k}_*'));data=gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes();n=R[k]-1
    vals=[sum((b-63).bit_count() for b in line[1:]) for line in data.splitlines() if line];mins[n,k]=min(vals)
@lru_cache(None)
def bound(n,k):
    if n<k:return 0
    if k<=9 and n>=R[k]:return inf
    ds=[(d,d*d+bound(n-d-1,k-1)) for d in range(min(k-1,n-1)+1)];dp={0:0}
    for _ in range(n):
        nxt={}
        for s,c in dp.items():
            for d,z in ds:
                if c+z<nxt.get(s+d,inf):nxt[s+d]=c+z
        dp=nxt
    lo=max(mins.get((n,k),0),ceil(n*bound(n-1,k)/(n-2)) if n>2 else 0)
    return min((s//2 for s,c in dp.items() if not s%2 and s//2>=lo and n*(s//2)>=c),default=inf)
if __name__=='__main__':print(mins,bound(39,10),[(n,bound(n,9)) for n in range(29,36)])
