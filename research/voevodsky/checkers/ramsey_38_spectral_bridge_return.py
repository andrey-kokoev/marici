"""Build a polynomial transfer operator on signed bridge maps from a ring and candidate middle boundary, before selecting a strip. The z^n diagonal coefficient is a once-around seam. We store polynomial SUPPORT as bits: nonnegative coefficients prevent cancellation. Evaluate the ungraded nonzero-spectrum control by the directed support cycle test. Independently compare every candidate with the zipper checker. Only the first (explicitly marked) 11-ring is used; no successful middle boundary or successful pool is input."""
from collections import Counter
from ramsey_38_joint_annuli import load,bits,red,boundaries,zipone,D
import json

def mode(I,M,c):
    m,n=len(I),len(M);a=bits(I);b=bits(M);ok=[[red(x,y)==(u^v^c) for y,v in zip(M,b)] for x,u in zip(I,a)]
    # S[j,k] records attainable phase advances across a complete traversal of I starting at j, ending at k on M. F is initially the identity bridge map.
    F=[[int(j==k) for k in range(n)] for j in range(n)]
    for i in range(m):
        G=[[0]*n for _ in M];dest=ok[(i+1)%m]
        for k in range(n):
            for h in range(n):
                j=(k+h)%n
                if not ok[i][j]:break
                if dest[j]:
                    for start in range(n):G[start][j]|=F[start][k]<<h
        F=G
    trace=0
    for j in range(n):trace|=F[j][j]
    assert all(not(trace>>k&1) or k%n==0 for k in range(trace.bit_length()));wind=[k//n for k in range(trace.bit_length()) if trace>>k&1]
    # A finite nonnegative matrix has a nonzero eigenvalue iff its support has a directed cycle. Prune sinks until stable.
    live=set(range(n))
    while True:
        new={i for i in live if any(F[i][j] for j in live)}
        if new==live:break
        live=new
    return bool(live),wind

p,q=1,16;I=[17,13,14,20,7,5,2,10,23,11,19];N=set(range(27));h,=[u for u in N if red(u,p) and red(u,q)];Z=sorted(u for u in N-{p,q} if red(u,h));W=sorted(N-{p,q,h}-set(I+Z));counts=Counter();ex={};w_hist=Counter()
for M in boundaries(Z,W):
    res=[mode(I,outer,c) for outer in (M,M[::-1]) for c in (0,1)];nonzero=any(s for s,w in res);winds=sorted({v for s,w in res for v in w});one=1 in winds;assert one==bool(zipone(I,M));key='unit_winding' if one else 'spectral_only' if nonzero else 'nilpotent';counts[key]+=1;w_hist[tuple(winds)]+=1;ex.setdefault(key,dict(M=M,returns=res))
print(dict(counts),w_hist,ex);(D/'ramsey_38_spectral_bridge_return.json').write_text(json.dumps(dict(poles=[p,q],ring=I,counts=counts,winding_sets=[(k,v) for k,v in w_hist.items()],examples=ex),indent=2)+'\n')
