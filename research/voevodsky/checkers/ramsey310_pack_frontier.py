"""Write transient whitespace-separated inputs to the native side checker."""
from ramsey310_exclusive_census import index
from ramsey310_fixed_exclusive_kernel import residual,sets,F
from ramsey310_cached_kernel import bits
from pathlib import Path
import sys
n=int(sys.argv[1]);path=Path(sys.argv[2]);A=residual(n);S,dis,p=index(n);C=list(sets(A,F,7));N=len(S)
with path.open('w') as f:
    for vals in (A,S,C): print(len(vals),*vals,file=f)
    for i,row in enumerate(p):
        for j in bits(row):
            k=i*N+j;o=dis[i]&dis[j]
            for l in bits(o):
                if l>i:break
                for z in bits(p[l]&o):
                    q=l*N+z
                    if q<k:print(k,q,file=f)
